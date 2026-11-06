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

  var nodes = data.nodes.map(function (n) { return { id: n.id, t: n.t, d: n.d, u: !!n.u, deg: 0 }; });
  var idx = {};
  nodes.forEach(function (n) { idx[n.id] = n; });
  var links = data.links.map(function (l) { return { source: l.s, target: l.t }; });
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

  var sim = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(function (d) { return d.id; }).distance(46).strength(0.35))
    .force("charge", d3.forceManyBody().strength(-120))
    .force("collide", d3.forceCollide().radius(function (d) { return r(d) + 2; }))
    .force("x", d3.forceX().strength(0.06))
    .force("y", d3.forceY().strength(0.09));

  var link = root.append("g").selectAll("line").data(links).join("line").attr("class", "link");
  var node = root.append("g").selectAll("g").data(nodes).join("g").attr("class", "node");
  // A larger invisible circle makes small dots easy to grab.
  node.append("circle").attr("class", "hit").attr("r", function (d) { return r(d) + 7; });
  node.append("circle").attr("class", function (d) { return "dot" + (d.u ? " unwritten-node" : ""); }).attr("r", r)
    .attr("fill", function (d) { return d.u ? "none" : colour[d.d]; });
  var label = node.append("text").attr("y", 4).text(function (d) { return d.t; });

  var dragging = null;
  function focus(d) {
    node.classed("dim", function (o) { return o !== d && !(nbr[d.id] && nbr[d.id][o.id]); })
        .classed("hot", function (o) { return o === d; });
    link.classed("hot", function (l) { return l.source === d || l.target === d; });
    var n = Object.keys(nbr[d.id] || {}).length;
    cap.innerHTML = d.u
      ? "<strong></strong> isn’t written yet; " + n + (n === 1 ? " article links" : " articles link") + " to it."
      : "<strong></strong> connects to " + n + (n === 1 ? " topic." : " topics.") + " Click to open it." +
        (d.fx != null ? " Double-click to let it settle back." : "");
    cap.querySelector("strong").textContent = d.t;
  }
  function blur() {
    if (dragging) return;
    node.classed("hot", false);
    link.classed("hot", false);
    cap.innerHTML = defaultCap;
    dimToFilter();
  }
  function dimToFilter() {
    node.classed("dim", function (o) { return matches !== null && !matches[o.id]; });
  }
  window.__kgDim = dimToFilter;

  // Single click opens the article; a double-click releases a node you moved instead.
  var openTimer = null;
  var base = data.base != null ? data.base : "a/";
  node.on("pointerenter", function (e, d) { if (!dragging) focus(d); })
      .on("pointerleave", blur)
      .on("click", function (e, d) {
        if (e.defaultPrevented || d.u) return;
        clearTimeout(openTimer);
        openTimer = setTimeout(function () { window.location.href = base + d.id + ".html"; }, 260);
      })
      .on("dblclick", function (e, d) {
        e.preventDefault(); e.stopPropagation();
        clearTimeout(openTimer);
        if (d.fx == null) return;
        d.fx = null; d.fy = null;
        d3.select(this).classed("pinned", false);
        sim.alpha(0.08).restart();
      });

  // Dragging moves only the node you hold; it stays where you drop it. Mouse and pen only:
  // on touch screens one finger scrolls the page and two fingers zoom, even over a dot.
  node.call(d3.drag()
    .filter(function (e) { return e.type === "mousedown" && !e.button; })
    .on("start", function (e, d) { sim.stop(); dragging = d; focus(d); })
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
    var count = Math.round(baseLabels * k * k);
    ranked.forEach(function (n, i) { n.label = i < count; });
    node.classed("label", function (d) { return !!d.label; });
    // Dots grow more slowly than the map so neighbours separate as you zoom in.
    var g = 1 / Math.sqrt(k);
    node.select(".dot").attr("r", function (d) { return r(d) * g; });
    node.select(".hit").attr("r", function (d) { return r(d) * g + 7 / k; });
    label.attr("font-size", 11 / k).attr("stroke-width", 3 / k)
      .attr("x", function (d) { return r(d) * g + 4 / k; });
  }

  function draw() {
    link.attr("x1", function (d) { return d.source.x; }).attr("y1", function (d) { return d.source.y; })
        .attr("x2", function (d) { return d.target.x; }).attr("y2", function (d) { return d.target.y; });
    node.attr("transform", function (d) { return "translate(" + d.x + "," + d.y + ")"; });
  }
  // Settle the layout before showing it, so the map appears already composed.
  sim.stop();
  for (var i = 0; i < 320; i++) sim.tick();
  draw();
  fit();
  relabel(1);
  sim.on("tick", draw);

  function fit() {
    var xs = nodes.map(function (n) { return n.x; }), ys = nodes.map(function (n) { return n.y; });
    var x0 = Math.min.apply(null, xs) - 30, x1 = Math.max.apply(null, xs) + 120;
    var y0 = Math.min.apply(null, ys) - 30, y1 = Math.max.apply(null, ys) + 30;
    var vw = x1 - x0, vh = y1 - y0, ar = w / h;
    if (vw / vh > ar) { var nh = vw / ar; y0 -= (nh - vh) / 2; vh = nh; }
    else { var nw = vh * ar; x0 -= (nw - vw) / 2; vw = nw; }
    svg.attr("viewBox", [x0, y0, vw, vh]);
  }
})();
