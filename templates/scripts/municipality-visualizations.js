/**
 *   Visualizations in the Municipaliy dashboard
 */

var svg    = d3.select("#municipality-visualizations");
var defs   = svg.append("defs");
var width  = svg.node().getBoundingClientRect().width;
var height = svg.node().getBoundingClientRect().height;
var config = ConfigurationService();
var root   = {};

var dot_marker = defs.append("marker")
                     .attr("id", "dot-marker")
                     .attr("viewBox", "0 0 10 10")
                     .attr("markerWidth", "10")
                     .attr("markerHeight", "10")
                     .attr("refX", "5")
                     .attr("refY", "5")
                     .append("circle")
                     .attr("r", 2)
                     .attr("cx", 5)
                     .attr("cy", 5);


d3.json('/api/test', function(response)
{
    config.setData(response);

    // Transform data into an object convertible into a tree
    root = config.getTree();
    // Configure and instantiate treemap
    d3.treemap().tile(d3.treemapResquarify).size([width, height]).round(true)(root);

    // Append cells to treemap
    var cell = svg.selectAll("g")
        .data(root.children)
        .enter().append("g")
        .attr("class", "first-level")
        .attr("transform", function(d) { return "translate(" + d.x0 + "," + d.y0 + ")"; });
      cell.append("rect")
          .attr("id", function(d) { return d.data.id; })
          .attr("width", function(d) { return d.x1 - d.x0; })
          .attr("height", function(d) { return d.y1 - d.y0; })
          .attr("fill", function(d, i) { return  config.color(i); })
          .attr("stroke", function(d, i) { return config.color(i); })
          .on("click", function(d, i){
              zoomTo(d.children, d.x0, d.y0, d.x1, d.y1, d.value, d.data.id, i, d.data.name);
          })
      cell.append("text")
          .selectAll("tspan")
          .data(function(d) { return d.data.name.split(" "); })
          .enter().append("tspan")
          .attr("x", 20)
          .attr("y", function(d, i) { return 30 + i * 18; })
          .text(function(d) { return d; });
      cell.append("text")
          .attr("class", "amount")
          .attr("x", function(d) { return d.x1 - d.x0 - 20; })
          .attr("y", function(d) { return d.y1 - d.y0 - 20; })
          .attr("text-anchor", "end")
          .text( function(d){ return config.currency(d.value) });

      // Update visualization title
      d3.select('.municipality-budgets__legend').html("<h3>"+root.data.name+"</h3><p>"+config.currency(root.value)+"</p>");
});

/**
 *  Zoom into children
 */
function zoomTo(children, x0, y0, x1, y1, sum, id, parent_i, label)
{
    svg.classed("showing-children", true);
    d3.select('.municipality-budgets__legend').html("<h3>"+ label + "</h3><p>" + config.currency(sum) + "</p>");
    var child = svg.append("g").attr("class", "selected-child")
        .selectAll("g")
        .data(children).enter()
        .append("g")
        .attr("transform", function(d) {
            return "translate(" + (d.x0-x0)*width/(x1-x0) + "," + (d.y0-y0)*height/(y1-y0) + ")";
         })
    child.append("rect")
        // Add treemap child
        .attr("class", "selected-child__text")
        .attr("id", function(d) { return d.data.id; })
        .attr("width", function(d) { return d.x1 - d.x0; })
        .attr("height", function(d) { return d.y1 - d.y0; })
        .attr("fill", function(d) { return config.color(parent_i) })
        .on("click", function(d){ removeChild(); })
        .transition().duration(500)
        .attr("width", function(d) { return (d.x1 - d.x0)*width/(x1-x0); })
        .attr("height", function(d) { return (d.y1 - d.y0)*height/(y1-y0); })
        .attr("fill", function(d,i) { return config.subcolor(parent_i); })
        .attr("stroke", function(d,i) { return config.color(parent_i); });
    // Add label
    child.append("text")
         .attr("x", function(d) { return (d.x0-x0)*width/(x1-x0) + 20; })
         .attr("y", function(d, i) { return (d.y0-y0)*height/(y1-y0) + 20 })
         .selectAll("tspan")
         .data(function(d) { return config.getSubcategoryLabel(d.data.name); })
         .enter().append("tspan")
         .attr("x", 20)
         .attr("y", function(d, i) { return 30 + i * 18; })
         .text(function(d) { return d; });
    // Add sparkline
    child.append("polyline")
         .attr("class", "sparkline")
         .attr("marker-start", "url(#dot-marker)")
         .attr("marker-end", "url(#dot-marker)")
         .attr("points", function(d){
              return config.getSparkline(d.data.name,
                  (d.x1 - d.x0)*width  / (x1-x0),
                  (d.y1 - d.y0)*height / (y1-y0)
              );
          });

    // Add amount
    child.append("text")
        .attr("x", function(d) { return (d.x1 - d.x0)*width/(x1-x0) - 20; })
        .attr("class", "amount")
        .attr("text-anchor", "end")
        .attr("y", function(d) { return (d.y1 - d.y0)*height/(y1-y0) - 20; })
        .text( function(d){ return config.currency(d.value) });

    child.transition().duration(500).style("fill-opacity", "1");
}

/**
 *  Zoom out
 */
function removeChild(){
    d3.select('.municipality-budgets__legend').html("<h3>" + root.data.name + "</h3>");
    svg.classed("showing-children", false);
    d3.select(".selected-child")
    .remove();
}
