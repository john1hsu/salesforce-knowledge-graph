(function () {
  "use strict";
  var data = JSON.parse(document.getElementById("kg-data").textContent);
  var el = document.getElementById("graph");
  var cap = document.getElementById("graph-cap");
  var defaultCap = cap.innerHTML;

  // ---------- search filters the list and the map together ----------
  var q = document.getElementById("q");
  var nores = document.getElementById("nores");
  var bySlug = {};
  (data.search || []).forEach(function (r) {
    bySlug[r.s] = (r.t + " " + r.a + " " + r.m).toLowerCase();
  });
  var matches = null; // null = no filter
  function applyFilter() {
    var term = q.value.trim().toLowerCase();
    matches = term ? {} : null;
    var any = false;
    document.querySelectorAll(".domain").forEach(function (sec) {
      var shown = 0;
      sec.querySelectorAll("li").forEach(function (li) {
        var hit = !term || bySlug[li.dataset.s].indexOf(term) !== -1;
        li.hidden = !hit;
        if (hit) { shown++; if (term) matches[li.dataset.s] = true; }
      });
      sec.hidden = shown === 0;
      if (shown) any = true;
    });
    nores.hidden = any;
    if (window.__kgDim) window.__kgDim();
  }
  if (q) q.addEventListener("input", applyFilter);

  // ---------- the map ----------
  if (!window.d3) { el.innerHTML = ""; el.style.display = "none"; return; }

  var colour = {};
  document.querySelectorAll("[data-domain]").forEach(function (sec) {
    if (!colour[sec.dataset.domain]) colour[sec.dataset.domain] = getComputedStyle(sec).getPropertyValue("--dc").trim() || "#888";
  });

  var nodes = data.nodes.map(function (n) {
    // ox/oy: the hover-spread offset now; tox/toy: where it is easing to; s: entrance scale.
    return { id: n.id, t: n.t, d: n.d, u: !!n.u, fresh: !!n.n, deg: 0, ox: 0, oy: 0, tox: 0, toy: 0, s: 0 };
  });
  var idx = {};
  nodes.forEach(function (n) { idx[n.id] = n; });
  var links = data.links.map(function (l) { return { source: l.s, target: l.t, p: 0 }; });
  var nbr = {};
  links.forEach(function (l) {
    idx[l.source].deg++; idx[l.target].deg++;
    (nbr[l.source] = nbr[l.source] || {})[l.target] = true;
    (nbr[l.target] = nbr[l.target] || {})[l.source] = true;
  });
  var r = function (n) { return n.u ? 3.5 : 4 + Math.sqrt(n.deg) * 1.6; };
  // Labels: the best-connected few at first; more appear as you zoom in.
  var ranked = nodes.filter(function (n) { return !n.u; }).sort(function (a, b) { return b.deg - a.deg; });
  var baseLabels = data.labels || 6;

  var w = el.clientWidth, h = el.clientHeight;
  var svg = d3.select(el).append("svg").attr("viewBox", [-w / 2, -h / 2, w, h]).attr("aria-hidden", "true");
  var root = svg.append("g");
  var vb = { x: -w / 2, y: -h / 2, w: w, h: h }; // current viewBox, set by fit()
  var curK = 1;                                  // current zoom scale

  var sim = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(function (d) { return d.id; }).distance(46).strength(0.35))
    .force("charge", d3.forceManyBody().strength(-120))
    .force("collide", d3.forceCollide().radius(function (d) { return r(d) + 2; }))
    .force("x", d3.forceX().strength(0.06))
    .force("y", d3.forceY().strength(0.09));

  var link = root.append("g").selectAll("line").data(links).join("line").attr("class", "link");
  var node = root.append("g").selectAll("g").data(nodes).join("g").attr("class", "node")
    .style("color", function (d) { return d.u ? null : colour[d.d]; });
  // A larger invisible circle makes small dots easy to grab.
  node.append("circle").attr("class", "hit").attr("r", function (d) { return r(d) + 7; });
  // Newest articles get a soft pulsing ring behind the dot, out of step with each other.
  node.filter(function (d) { return d.fresh && !d.u; }).append("circle").attr("class", "ring").attr("r", r)
    .attr("fill", function (d) { return colour[d.d]; })
    .style("animation-delay", function () { return (-Math.random() * 2.6).toFixed(2) + "s"; });
  node.append("circle").attr("class", function (d) { return "dot" + (d.u ? " unwritten-node" : ""); }).attr("r", r)
    .attr("fill", function (d) { return d.u ? "none" : colour[d.d]; });
  var label = node.append("text").attr("y", 4).text(function (d) { return d.t; });

  function px(d) { return d.x + d.ox; }
  function py(d) { return d.y + d.oy; }

  // ---------- animation loop: entrance + hover spread share one timer ----------
  var timer = null, last = 0;
  var entering = false, t0 = 0, entranceEnd = 0;
  function kick() {
    if (timer) return;
    last = performance.now();
    timer = d3.timer(frame);
  }
  function frame() {
    var now = performance.now(), dt = Math.min(now - last, 64);
    last = now;
    var busy = false;
    if (entering) {
      var t = now - t0;
      nodes.forEach(function (n) { n.s = d3.easeBackOut(clamp01((t - n.delay) / 420)); });
      links.forEach(function (l) { l.p = d3.easeCubicOut(clamp01((t - l.delay) / 460)); });
      if (t >= entranceEnd) {
        entering = false;
        nodes.forEach(function (n) { n.s = 1; });
        links.forEach(function (l) { l.p = 1; });
      } else busy = true;
    }
    // Ease every offset toward its target (frame-rate independent).
    var f = 1 - Math.exp(-dt / 85);
    nodes.forEach(function (n) {
      var ex = n.tox - n.ox, ey = n.toy - n.oy;
      if (Math.abs(ex) > 0.02 || Math.abs(ey) > 0.02) { n.ox += ex * f; n.oy += ey * f; busy = true; }
      else { n.ox = n.tox; n.oy = n.toy; }
    });
    draw();
    if (!busy) { timer.stop(); timer = null; }
  }
  function clamp01(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }

  // ---------- staggered entrance: areas pop in one after another, hubs first, then links draw ----------
  function planEntrance() {
    var groups = {}, order = [];
    nodes.forEach(function (n) {
      var g = n.u ? "￿" : n.d; // unwritten topics come last
      if (!groups[g]) { groups[g] = []; order.push(g); }
      groups[g].push(n);
    });
    order.sort(function (a, b) { return groups[b].length - groups[a].length || (a < b ? -1 : 1); });
    var step = Math.min(170, 1300 / Math.max(order.length, 1));
    order.forEach(function (g, gi) {
      groups[g].sort(function (a, b) { return b.deg - a.deg; })
        .forEach(function (n, i) { n.delay = gi * step + Math.min(i * 14, 420); });
    });
    var end = 0;
    links.forEach(function (l) {
      // Each link grows out of whichever end appeared first, once both ends are visible.
      var a = l.source, b = l.target;
      if (a.delay > b.delay) { l.from = b; l.to = a; } else { l.from = a; l.to = b; }
      l.delay = l.to.delay + 260;
      end = Math.max(end, l.delay + 460);
    });
    nodes.forEach(function (n) { end = Math.max(end, n.delay + 420); });
    entranceEnd = end;
  }
  function startEntrance() {
    entering = true;
    t0 = performance.now();
    kick();
  }

  // ---------- hover: highlight neighbours and spread nearby dots apart ----------
  var SPREAD_RADIUS = 120, SPREAD_PUSH = 40; // in screen pixels
  var dragging = null, focused = null, unspreadTimer = null;
  function unitsPerPx() { return vb.w / (el.clientWidth || vb.w) / curK; }
  function spread(d) {
    clearTimeout(unspreadTimer);
    var u = unitsPerPx(), R = SPREAD_RADIUS * u, push = SPREAD_PUSH * u;
    var cx = px(d), cy = py(d);
    nodes.forEach(function (o) {
      if (o === d) { o.tox = o.ox; o.toy = o.oy; return; } // the hovered dot stays under the pointer
      var dx = o.x - cx, dy = o.y - cy, dist = Math.sqrt(dx * dx + dy * dy);
      if (dist > 0.01 && dist < R) {
        var m = push * (1 - dist / R) / dist; // closer dots move further; order never flips since push < R
        o.tox = dx * m; o.toy = dy * m;
      } else { o.tox = 0; o.toy = 0; }
    });
    kick();
  }
  function unspread(now) {
    clearTimeout(unspreadTimer);
    var go = function () { nodes.forEach(function (o) { o.tox = 0; o.toy = 0; }); kick(); };
    // A short grace period lets the pointer travel to a neighbour without the map snapping back first.
    if (now) go(); else unspreadTimer = setTimeout(go, 180);
  }

  function focus(d) {
    el.classList.add("focusing");
    node.classed("dim", function (o) { return o !== d && !(nbr[d.id] && nbr[d.id][o.id]); })
        .classed("nb", function (o) { return o !== d && !!(nbr[d.id] && nbr[d.id][o.id]); })
        .classed("hot", function (o) { return o === d; });
    link.classed("hot", function (l) { return l.source === d || l.target === d; });
    var n = Object.keys(nbr[d.id] || {}).length;
    var next = d.u ? "" : (focused === d ? " Click again to open it." : " Click to zoom in, then click again to open it.");
    cap.innerHTML = d.u
      ? "<strong></strong> isn’t written yet; " + n + (n === 1 ? " article links" : " articles link") + " to it."
      : "<strong></strong> connects to " + n + (n === 1 ? " topic." : " topics.") + next +
        (d.fx != null ? " Double-click to let it settle back." : "");
    cap.querySelector("strong").textContent = d.t;
  }
  function blur() {
    if (dragging) return;
    el.classList.remove("focusing");
    node.classed("hot", false).classed("nb", false);
    link.classed("hot", false);
    cap.innerHTML = defaultCap;
    dimToFilter();
    unspread();
  }
  function dimToFilter() {
    node.classed("dim", function (o) { return matches !== null && !matches[o.id]; });
  }
  window.__kgDim = dimToFilter;

  // ---------- click to zoom into a dot's neighbourhood; click it again to open it ----------
  function zoomTo(d) {
    var pts = [d].concat(Object.keys(nbr[d.id] || {}).map(function (id) { return idx[id]; }));
    var xs = pts.map(function (p) { return p.x; }), ys = pts.map(function (p) { return p.y; });
    var x0 = Math.min.apply(null, xs), x1 = Math.max.apply(null, xs);
    var y0 = Math.min.apply(null, ys), y1 = Math.max.apply(null, ys);
    var bw = Math.max(x1 - x0, 80), bh = Math.max(y1 - y0, 80);
    var k = Math.max(1.3, Math.min(4, 0.8 * Math.min(vb.w / bw, vb.h / bh)));
    // Centre on the clicked dot, nudged toward its neighbours.
    var cx = (d.x * 2 + (x0 + x1) / 2) / 3, cy = (d.y * 2 + (y0 + y1) / 2) / 3;
    var t = d3.zoomIdentity.translate(vb.x + vb.w / 2 - cx * k, vb.y + vb.h / 2 - cy * k).scale(k);
    svg.transition().duration(750).ease(d3.easeCubicInOut).call(zoom.transform, t);
  }
  function setFocused(d) {
    focused = d;
    node.classed("focused", function (o) { return o === d; });
  }
  function zoomOut() {
    setFocused(null);
    svg.transition().duration(650).ease(d3.easeCubicInOut).call(zoom.transform, d3.zoomIdentity);
  }

  // A single click waits briefly so a double-click (which releases a moved dot) can cancel it.
  var openTimer = null;
  var base = data.base != null ? data.base : "a/";
  node.on("pointerenter", function (e, d) { if (!dragging) { focus(d); spread(d); } })
      .on("pointerleave", blur)
      .on("click", function (e, d) {
        e.stopPropagation();
        if (e.defaultPrevented) return;
        clearTimeout(openTimer);
        openTimer = setTimeout(function () {
          if (focused === d && !d.u) { window.location.href = base + d.id + ".html"; return; }
          setFocused(d);
          zoomTo(d);
          if (node.filter(function (o) { return o === d; }).node().matches(":hover")) focus(d);
        }, 260);
      })
      .on("dblclick", function (e, d) {
        e.preventDefault(); e.stopPropagation();
        clearTimeout(openTimer);
        if (d.fx == null) return;
        d.fx = null; d.fy = null;
        d3.select(this).classed("pinned", false);
        sim.alpha(0.08).restart();
      });
  // Clicking empty space zooms back out (a pan doesn't count as a click).
  svg.on("click", function (e) { if (focused && !e.defaultPrevented) zoomOut(); });

  // Dragging moves only the node you hold; it stays where you drop it. Mouse and pen only:
  // on touch screens one finger scrolls the page and two fingers zoom, even over a dot.
  node.call(d3.drag()
    .filter(function (e) { return e.type === "mousedown" && !e.button; })
    .subject(function (e, d) { return { x: px(d), y: py(d) }; })
    .on("start", function (e, d) {
      sim.stop();
      // Bake the spread offset into the dot so it doesn't jump, then let the others settle back.
      d.x += d.ox; d.y += d.oy; d.ox = d.oy = d.tox = d.toy = 0;
      dragging = d; focus(d); unspread(true);
    })
    .on("drag", function (e, d) { d.x = d.fx = e.x; d.y = d.fy = e.y; draw(); })
    .on("end", function (e, d) {
      dragging = null;
      d3.select(this).classed("pinned", true);
      if (!this.matches(":hover")) blur(); else focus(d);
    }));

  // Scroll wheel or pinch / two-finger drag zooms and pans; one finger scrolls the page.
  var zoom = d3.zoom().scaleExtent([0.5, 8])
    .filter(function (e) {
      if (e.type === "wheel") return true;
      if (e.type.indexOf("touch") === 0) return e.touches && e.touches.length >= 2;
      return !e.button;
    })
    .on("zoom", function (e) { root.attr("transform", e.transform); relabel(e.transform.k); });
  svg.call(zoom).on("dblclick.zoom", null);

  function relabel(k) {
    curK = k;
    var count = Math.round(baseLabels * k * k);
    ranked.forEach(function (n, i) { n.label = i < count; });
    node.classed("label", function (d) { return !!d.label; });
    // Dots grow more slowly than the map so neighbours separate as you zoom in.
    var g = 1 / Math.sqrt(k);
    node.select(".dot").attr("r", function (d) { return r(d) * g; });
    node.select(".ring").attr("r", function (d) { return r(d) * g; });
    node.select(".hit").attr("r", function (d) { return r(d) * g + 7 / k; });
    label.attr("font-size", 11 / k).attr("stroke-width", 3 / k)
      .attr("x", function (d) { return r(d) * g + 4 / k; });
  }

  function draw() {
    link.attr("x1", function (d) { var a = d.from || d.source; return px(a); })
        .attr("y1", function (d) { var a = d.from || d.source; return py(a); })
        .attr("x2", function (d) { var a = d.from || d.source, b = d.to || d.target; return px(a) + (px(b) - px(a)) * d.p; })
        .attr("y2", function (d) { var a = d.from || d.source, b = d.to || d.target; return py(a) + (py(b) - py(a)) * d.p; });
    node.attr("transform", function (d) {
      return "translate(" + px(d) + "," + py(d) + ")" + (d.s < 1 ? " scale(" + Math.max(d.s, 0) + ")" : "");
    });
  }
  // Settle the layout before showing it, so the map appears already composed.
  sim.stop();
  for (var i = 0; i < 320; i++) sim.tick();
  planEntrance();
  draw();
  fit();
  relabel(1);
  sim.on("tick", draw);

  // Play the entrance when the map scrolls into view.
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      if (entries.some(function (en) { return en.isIntersecting; })) { io.disconnect(); startEntrance(); }
    }, { threshold: 0.25 });
    io.observe(el);
  } else startEntrance();

  function fit() {
    var xs = nodes.map(function (n) { return n.x; }), ys = nodes.map(function (n) { return n.y; });
    var x0 = Math.min.apply(null, xs) - 30, x1 = Math.max.apply(null, xs) + 120;
    var y0 = Math.min.apply(null, ys) - 30, y1 = Math.max.apply(null, ys) + 30;
    var vw = x1 - x0, vh = y1 - y0, ar = w / h;
    if (vw / vh > ar) { var nh = vw / ar; y0 -= (nh - vh) / 2; vh = nh; }
    else { var nw = vh * ar; x0 -= (nw - vw) / 2; vw = nw; }
    vb = { x: x0, y: y0, w: vw, h: vh };
    svg.attr("viewBox", [x0, y0, vw, vh]);
  }
})();
