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
  var labelled = nodes.filter(function (n) { return !n.u; }).sort(function (a, b) { return b.deg - a.deg; }).slice(0, data.labels || 6);
  labelled.forEach(function (n) { n.label = true; });

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
  var node = root.append("g").selectAll("g").data(nodes).join("g")
    .attr("class", function (d) { return "node" + (d.label ? " label" : ""); });
  node.append("circle").attr("r", r)
    .attr("class", function (d) { return d.u ? "unwritten-node" : null; })
    .attr("fill", function (d) { return d.u ? "none" : colour[d.d]; });
  node.append("text").attr("x", function (d) { return r(d) + 4; }).attr("y", 4).text(function (d) { return d.t; });

  function focus(d) {
    node.classed("dim", function (o) { return o !== d && !(nbr[d.id] && nbr[d.id][o.id]); })
        .classed("hot", function (o) { return o === d; });
    link.classed("hot", function (l) { return l.source === d || l.target === d; });
    var n = Object.keys(nbr[d.id] || {}).length;
    cap.innerHTML = d.u
      ? "<strong></strong> isn’t written yet; " + n + (n === 1 ? " article links" : " articles link") + " to it."
      : "<strong></strong> connects to " + n + (n === 1 ? " topic." : " topics.") + " Click to open it.";
    cap.querySelector("strong").textContent = d.t;
  }
  function blur() {
    node.classed("hot", false);
    link.classed("hot", false);
    cap.innerHTML = defaultCap;
    dimToFilter();
  }
  function dimToFilter() {
    node.classed("dim", function (o) { return matches !== null && !matches[o.id]; });
  }
  window.__kgDim = dimToFilter;

  node.on("pointerenter", function (e, d) { focus(d); })
      .on("pointerleave", blur)
      .on("click", function (e, d) { if (!d.u && !e.defaultPrevented) window.location.href = (data.base || "") + d.id + ".html"; });

  node.call(d3.drag()
    .on("start", function (e, d) { if (!e.active) sim.alphaTarget(0.25).restart(); d.fx = d.x; d.fy = d.y; })
    .on("drag", function (e, d) { d.fx = e.x; d.fy = e.y; })
    .on("end", function (e, d) { if (!e.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));

  svg.call(d3.zoom().scaleExtent([0.4, 4]).filter(function (e) {
    return e.type === "wheel" ? e.ctrlKey || e.metaKey : !e.button;
  }).on("zoom", function (e) { root.attr("transform", e.transform); }));

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
