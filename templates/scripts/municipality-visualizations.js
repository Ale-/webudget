/**
 *   Visualizations in the Municipaliy dashboard
 */

var svg    = d3.select("#municipality-visualizations");
var width  = svg.node().getBoundingClientRect().width;
var height = svg.node().getBoundingClientRect().height;
var data   = {};


var first_level = [
  { k: 'ps', v : 'General public services' },
  { k: 'de', v : 'Defence' },
  { k: 'po', v : 'Public order and safety' },
  { k: 'ea', v : 'Economic affairs' },
  { k: 'ep', v : 'Environmental protection' },
  { k: 'ho', v : 'Housing and community amenities' },
  { k: 'he', v : 'Health'  },
  { k: 're', v : 'Recreation, culture and religion' },
  { k: 'ed', v : 'Education'  },
  { k: 'so', v : 'Social protection' },
];

var second_level = {
  'concept_ps_1' : ['Executive and','legislative organs','financial and','fiscal affairs,', 'external affairs'],
  'concept_ps_2' : ['Foreign','economic aid'],
  'concept_ps_3' : ['General','services'],
  'concept_ps_4' : ['Basic','research'],
  'concept_ps_5' : ['R&D general','public services'],
  'concept_ps_6' : ['General public','services','(not classified)'],
  'concept_ps_7' : ['Public debt','transactions'],
  'concept_ps_8' : ['Transfers of a general','character between','different levels','of government'],
  'concept_de_1' : ['Military defence'],
  'concept_de_2' : ['Civil defence'],
  'concept_de_3' : ['Foreign military aid'],
  'concept_de_4' : ['R&D defence'],
  'concept_de_5' : ['Defence','(not classified)'],
  'concept_po_1' : ['Police','services'],
  'concept_po_2' : ['Fire-protection','services'],
  'concept_po_3' : ['Law courts'],
  'concept_po_4' : ['Prisons'],
  'concept_po_5' : ['R&D public order','and safety'],
  'concept_po_6' : ['Public order','and safety','(not classified)'],
  'concept_ea_1' : ['General economic,','commercial','and labour affairs'],
  'concept_ea_2' : ['Agriculture,','forestry,','fishing and hunting'],
  'concept_ea_3' : ['Fuel and energy'],
  'concept_ea_4' : ['Mining, manufacturing','and construction'],
  'concept_ea_5' : ['Transport'],
  'concept_ea_6' : ['Communication'],
  'concept_ea_7' : ['Other industries'],
  'concept_ea_8' : ['R&D economic','affairs'],
  'concept_ea_9' : ['Economic affairs','(not classified)'],
  'concept_ep_1' : ['Waste','management'],
  'concept_ep_2' : ['Waste','water management'],
  'concept_ep_3' : ['Pollution','abatement'],
  'concept_ep_4' : ['Protection of biodiversity','and landscape'],
  'concept_ep_5' : ['R&D environmental protection'],
  'concept_ep_6' : ['Environmental','protection','(not classified)'],
  'concept_ho_1' : ['Housing','development'],
  'concept_ho_2' : ['Community','development'],
  'concept_ho_3' : ['Water','supply'],
  'concept_ho_4' : ['Street','lighting'],
  'concept_ho_5' : ['R&D housing','and community','amenities'],
  'concept_ho_6' : ['Housing','and community','amenities','(not classified)'],
  'concept_he_1' : ['Medical products,','appliances and equipment'],
  'concept_he_2' : ['Outpatient','services'],
  'concept_he_3' : ['Hospital','services'],
  'concept_he_4' : ['Public health','services'],
  'concept_he_5' : ['R&D health'],
  'concept_he_6' : ['Health','(not classified)'],
  'concept_re_1' : ['Recreational','and sporting','services'],
  'concept_re_2' : ['Cultural','services'],
  'concept_re_3' : ['Broadcasting','and publishing','services'],
  'concept_re_4' : ['Religious and','other community services'],
  'concept_re_5' : ['R&D recreation,','culture and religion'],
  'concept_re_6' : ['Recreation,','culture','and religion (not classified)'],
  'concept_ed_1' : ['Pre-primary','and primary','education'],
  'concept_ed_2' : ['Secondary education'],
  'concept_ed_3' : ['Post-secondary','non-tertiary education'],
  'concept_ed_4' : ['Tertiary','education'],
  'concept_ed_5' : ['Education','not definable','by level'],
  'concept_ed_6' : ['Subsidiary','services','to education'],
  'concept_ed_7' : ['R&D','education'],
  'concept_ed_8' : ['Education','(not classified)'],
  'concept_so_1' : ['Sickness','and disability'],
  'concept_so_2' : ['Old age'],
  'concept_so_3' : ['Survivors'],
  'concept_so_4' : ['Family','and children'],
  'concept_so_5' : ['Unemployment'],
  'concept_so_6' : ['Housing'],
  'concept_so_7' : ['Social','exclusion','(not classified)'],
  'concept_so_8' : ['R&D social','protection'],
  'concept_so_9' : ['Social','protection','(not classified)'],
};

var currency = d3.formatLocale ({
  "decimal": ".",
  "thousands": " ",
  "currency": ["", " M. €"],
  "grouping": [3],
});

var colors = [ '#ed4040', '#eda640', '#ceed40', '#69ed40', '#40ed7d', '#40ede3', '#4091ed', '#5440ed', '#ba40ed', '#ed40ba' ];

var fader = function(color) { return d3.interpolateRgb(color, "#fff")(0.1); };
var color = d3.scaleOrdinal(d3.schemeCategory20.map(fader));
var format = d3.format(",d");

var treemap = d3.treemap()
   .tile(d3.treemapResquarify)
   .size([width, height])
   .round(true);

var defs = svg.append("defs");
var dot_marker = defs.append("marker").attr("id", "dot-marker")
                 .attr("viewBox", "0 0 10 10").attr("markerWidth", "10").attr("markerHeight", "10")
                 .attr("refX", "5").attr("refY", "5");
dot_marker.append("circle").attr("r", 2).attr("cx", 5).attr("cy", 5);

  //  <marker id="Triangle" viewBox="0 0 10 10" refX="1" refY="5"
  //          markerWidth="6" markerHeight="6" orient="auto">
  //        <path d="M 0 0 L 10 5 L 0 10 z" />
  //      </marker>

d3.json('/api/test', function(response){
    data = response;
    var treedata = tree(data);

    var root = d3.hierarchy(treedata)
        .eachBefore(function(d) { d.data.id = (d.parent ? d.parent.data.id + "." : "") + d.data.name; })
        .sum(function(d) { return d.value; })
        .sort(function(a, b) { return b.height - a.height || b.value - a.value; });
    treemap(root);
    var cell = svg.selectAll("g")
        .data(root.children)
        .enter().append("g")
        .attr("class", "first-level")
        .attr("transform", function(d) { return "translate(" + d.x0 + "," + d.y0 + ")"; });
      cell.append("rect")
          .attr("id", function(d) { return d.data.id; })
          .attr("width", function(d) { return d.x1 - d.x0; })
          .attr("height", function(d) { return d.y1 - d.y0; })
          .attr("fill", function(d, i) { return colors[i]; })
          .attr("stroke", function(d, i) { return colors[i]; })
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
          .text( function(d){ return currency.format("$d")(d.value/1e6) });

      var title = d3.select('.municipality-budgets__title');
      title.text( title.text() + root.data.name );
});

function zoomTo(children, x0, y0, x1, y1, sum, id, parent_i, label){

    svg.classed("showing-children", true);
    d3.select('.municipality-budgets__legend').html("<h3>"+ label + "</h3><p>" + currency.format("$d")(sum/1e6) + "</p>");
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
        .attr("fill", function(d) { return colors[parent_i] })
        .on("click", function(d){ console.log((d.x1 - d.x0)*width  / (x1-x0)); removeChild(); })
        .transition().duration(500)
        .attr("width", function(d) { return (d.x1 - d.x0)*width/(x1-x0); })
        .attr("height", function(d) { return (d.y1 - d.y0)*height/(y1-y0); })
        .attr("fill", function(d,i) { return d3.interpolateRgb(colors[parent_i], "#fff")(.2 + Math.random()*.1); })
        .attr("stroke", function(d,i) { return colors[parent_i]; });
    // Add label
    child.append("text")
         .attr("x", function(d) { return (d.x0-x0)*width/(x1-x0) + 20; })
         .attr("y", function(d, i) { return (d.y0-y0)*height/(y1-y0) + 20 })
         .selectAll("tspan")
         .data(function(d) { return second_level[d.data.name]; })
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
              return drawSparkline(d.data.name,
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
        .text( function(d){ return currency.format("$d")(d.value/1e6) });

    child.transition().duration(500).style("fill-opacity", "1");
}


function removeChild(){
    d3.select('.municipality-budgets__legend').html("");
    svg.classed("showing-children", false);
    d3.select(".selected-child")
    .remove();
}

/**
 *  Creates a hierarchical tree of data from a budgets list
 */
var tree = function(data)
{
    /// Get fields
    var total = {};
    var exceptions = [ 'year' ];
    for(field in data[0])
        if(exceptions.indexOf(field) == -1)
            total[field] = data[0][field];
    for(var i = 1; i < data.length; i++)
        for(field in total)
            total[field] += data[i][field];
    var graph = { "name" : "Total budget allocation during period " + data[0].year + "-" + data[data.length-1].year, children: [] }
    for(var category in first_level){
        var first_level_child = {
            'name'     : first_level[category].v,
            'children' : [],
        };
        var leafs = Object.keys(total).filter(label => label.indexOf("concept_" + first_level[category].k) > -1);
        for(i in leafs){
            first_level_child.children.push({
                'name' : leafs[i],
                'value' : total[leafs[i]],
            });
        };
        graph.children.push( first_level_child );
    };
    return graph;
}

/**
 *  Time series
 */
var timeseries = function(concept){
    var timeseries = [];
    for(var i in data){
        timeseries.push( data[i][concept] );
    }
    return timeseries;
}

var drawSparkline = function(category, w, h){
    var padding = 20;
    var points = "";
    var timeline_data = timeseries(category);
    var y_scale = d3.scaleLinear().domain([2e6, 20e6]).range([h*.75, h*.25]);
    var slot = w*.8 / timeline_data.length+1;
    for(var i in timeline_data){
        var x = w*.1 + slot*i;
        var y = d3.format("d")(y_scale(timeline_data[i]));
        points += [x, y].join(",") + " ";
    }
    return points;
}
