

var nodes = JSON.parse(document.getElementById('decrete').textContent);



nodes = nodes.filter(function( obj ) {
  return (typeof obj.name === "string") && (obj.subtype !== "scenic") && (obj.subtype !== "activities")
});
// console.log("---------nodes----------")

nodes = nodes.map(function(obj) {
  var o = Object.assign({}, obj);
  if (obj.type === "house"){ o.image = "static/images/sweet_home.png";}
  else{ o.image = "";}
  return o; 
})
console.log(nodes)

// make house_facility link dict
var redundant_node_Set = new Set();
var link_dict = {}
var edges = nodes.map(function(e){
  if (e["type"] === 'facility'){
    var sc, tg; 
    var s = e["id"].split("_");
    sc = Number(s[0]);
    
    if (e["name"] in link_dict){
      redundant_node_Set.add(e["id"]); // record for current node removement
      tg = link_dict[e["name"]];
    }else{
      link_dict[e["name"]] = e["id"];
      tg = e["id"];
    }
    return {id:0, source:sc, target:tg, type:'near'};
  }
}).filter(item => typeof item != "undefined");
// console.log("---------the new edges-----------------");
// console.log(link_dict);
// console.log(edges);


nodes = nodes.filter(function( obj ) {
  return !redundant_node_Set.has(obj.id)
});

//defining the chart
var myChart = familyChart().nodes(nodes)
                           .links(edges);

//defining the width and height of the svg
var width = window.innerWidth, // default width
   height = window.innerHeight; 

//drawing the svg and calling the familyChart opject.
var svg = d3.select('#forces').append("svg")
            .attr("width", "100%")
            .attr("height", "100%")
            .attr("background-color","yellow")
            .call(myChart);




// legend
var data = ["Police Office", "Park", "Hospital", "Place of Worship", "University", "Senior High School", "Junior High School", "Elementary School", "MRT Station"];
var clr = ["#8CABD9", "Plum", "LightCoral", "BurlyWood", "#F1EC7A", "LightPink", "Lavender", "MediumTurquoise", "#8EC31C"];

var colors = d3.scaleOrdinal(d3.schemeCategory10);
var local = d3.local();
var legend = svg.selectAll(null)
  .data(data)
  .enter()
  .append("g");

legend.append("text")
  .text(String)
  .style("font-size","13px")
  .attr("x", 40)
  .attr("y", function(d, i) {
    // local.set(this.parentNode, this.getComputedTextLength())
    return (i-1)*25 + 50;
  });

legend.append("rect")
  .style("fill", function(d, i) {
    return clr[i]
  })
  .attr("x", 10)
  .attr("y", function(d, i) {
    return (i-1)*25 + 35;
  })
  .attr("width", 20)
  .attr("height", 20);


var counter = 0;

legend.each(function(d, i) {
  if (i) {
    d3.select(this).attr("transform", "translate(" + (counter += local.get(this.previousSibling) + 36) + ",0)")
  }
})





function familyChart() {

  var nodes = [],
      links = [] // default height

  function my(svg) {

    //set the radius of the family nodes
    var family_radius = 22; 

    //set the repel force - may need to be tweaked for multiple data
    //the lower the strength the more they will repel away from each other 
    //the larger the distance, the more apart they will be
    var repelForce = d3.forceManyBody().strength(-2500).distanceMax(350)
                       .distanceMin(50);


    var simulation = d3.forceSimulation()
                      // .alphaDecay(0.04)
                      // .velocityDecay(0.4) 
                      // .force("center", d3.forceCenter(width / 2, height / 2))
                       .force("xAxis",d3.forceX(width/2).strength(0.4))
                       .force("yAxis",d3.forceY(height/2).strength(0.7))
                       .force("repelForce",repelForce)
                       .force("link", d3.forceLink().id(function(d) { return d.id }).distance(dist).strength(1.5)) //1.5
                       // .force("collide",d3.forceCollide().radius(function(d) { return d.r * 20; }).iterations(10).strength(1));

    function dist(d){
      //used by link force
      return 70
    }

    //define the linkssss
    var links = svg.selectAll("foo")
        .data(edges)
        .enter()
        .append("line")
        .attr("stroke-width",function(d){
          //stroke width - thicker if married/divorced
          if (d.type == 'near'){
            return "1px"
          }
        })
      .attr("stroke", function(d){ 
        if(d.type === "near"){
          return "grey"
        }
      });

    //define tooltip
    var tooltip = d3.select("#forces")
      .append("div")
      .attr("class", "tooltip")
      .html("");

    //draw the nodes with drag functionality
    var node = svg.selectAll("foo")
        .data(nodes)
        .enter()
        .append("g")
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));


    //define defs and patterns - for the images
    var defs = node.append("defs");


    defs.append('pattern')
        .attr("id", function(d,i){return "my_image" + i})
        .attr("width", 1)
        .attr("height", 1)
        .append("svg:image")
        .attr("xlink:href", function(d) {return d.image})
        .attr("height", "44")
        .attr("width", "44")
        .attr("x", 0)
        .attr("y", 0);

    //append circles 
    var circles = node.append("circle")
                      .attr("class","circle")
                      .attr("r", function(d){
                          if (d.type == "house"){
                            return family_radius;
                          } else{return 15;}}) //40 
                       .attr("fill",function(d,i){ 
                         if(d.type == "house"){return "url(#my_image" + i + ")"}
                         else if (d.type == "facility"){
                           if (d.subtype === "police"){return "#8CABD9"}
                           else if (d.subtype === "park"){return "Plum"}
                           else if (d.subtype === "religious"){return "BurlyWood"}
                           else if (d.subtype === "hospital"){return "LightCoral"}
                           else if (d.subtype === "university"){return "#F1EC7A"}
                           else if (d.subtype === "senior"){return "LightPink"}
                           else if (d.subtype === "junior"){return "Lavender"}
                           else if (d.subtype === "elementary"){return "MediumTurquoise"}
                           else if (d.subtype === "mrt"){return "#8EC31C"}
                            console.log(d.subtype);
                            console.log(d.name);
                         }
                         else{return "grey"}})
                        .attr("stroke", function(d){ 
                          //different borders for family, male and female
                          if (d.type == "house"){return "grey";
                          } else{ 
                            // if(d.sex == "m"){return "blue"} 
                            // else {  return "pink"}
                          }})
                          .attr("stroke-width","2px")
                          .on("mouseover", function(d){
                            if(d.type === "house"){
                              //sets tooltip.  t_text = content in html
                              t_text = "<strong>" + titleCase(d.name) + "</strong>"
                              t_text += "<br>ID: " + d.id;
                              t_text += "<br>Type: " + d.b_type;
                              t_text += "<br>Price: " + d.price;
                              t_text += "<br>Age: " + d.age;
                              t_text += "<br>Area: " + d.ping +" ping";
                              if(d.b_type !== 'Townhouse'){
                                t_text += "<br>Floor: " + d.trans_floor + " th";
                              }else{
                                t_text += "<br>Floor: " + d.total_floor;
                              }
                              tooltip.html(t_text);
                              return tooltip.style("visibility", "visible").style("opacity", "100");
                            }  })
                           .on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
                           .on("mouseout", function(){return tooltip.style("visibility", "hidden");});


    //title case function used by tooltip and labels
    function titleCase(str) {
        // console.log(str)
        str = str.toLowerCase().split(' ');
        for (var i = 0; i < str.length; i++) {
            str[i] = str[i].charAt(0).toUpperCase() + str[i].slice(1);
        }
        return str.join(' '); // text below the circle
    }

    // append labels
    var texts = node.append("text")
        .style("fill", "black")
        .attr("dx", 0)
        .attr("dy", 25)
        .attr("text-anchor","middle")
        .text(function(d) {
          if (d.type==="facility"){
            return d.name;
          }
        });

    //finally - attach the nodes and the links to the simulation
    simulation.nodes(nodes);
    simulation.force("link")
              .links(edges);

    //and define tick functionality
   simulation.on("tick", function() {

        links.attr("x1", function(d) {return d.source.x;})
             .attr("y1", function(d) {return d.source.y;})
             .attr("x2", function(d) {return d.target.x;})
             .attr("y2", function(d) {return d.target.y;})

        node.attr("transform", function(d){ return "translate(" + d.x + "," + d.y + ")"})
    });


    function dragstarted(d) {

       if (!d3.event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
      if(d.type == 'family'){
        //stickiness - toggles the class to fixed/not-fixed to trigger CSS
        var my_circle = d3.select(this).selectAll('circle')
        if(my_circle.attr('class') == 'fixed'){
          my_circle.attr("class","not-fixed")
        }else{
          my_circle.attr("class","fixed")
        }
      }
    }

    function dragged(d) {
        d.fx = d3.event.x;
        d.fy = d3.event.y;
    }

    function dragended(d) {
       if (!d3.event.active) simulation.alphaTarget(0);
       //stickiness - unfixes the node if not-fixed or a person
       var my_circle = d3.select(this).selectAll('circle')
       if(my_circle.attr('class') == 'not-fixed'  || d.type !== 'family'){
         d.fx = null; 
         d.fy = null;
       }

    }

    function polarToCartesian(centerX, centerY, radius, angleInDegrees) {
        var angleInRadians = (angleInDegrees-90) * Math.PI / 180.0;

      return {
        x: centerX + (radius * Math.cos(angleInRadians)),
        y: centerY + (radius * Math.sin(angleInRadians))
      };
    }

    function describeArc(x, y, radius, startAngle, endAngle){
      //for arcs - from excellent link - http://jsbin.com/quhujowota/1/edit?html,js,output

        var start = polarToCartesian(x, y, radius, endAngle);
        var end = polarToCartesian(x, y, radius, startAngle);

        var largeArcFlag = endAngle - startAngle <= 180 ? "0" : "1";

        var d = [
            "M", start.x, start.y,
            "A", radius, radius, 0, largeArcFlag, 0, end.x, end.y
        ].join(" ");

        return d;
    }


  }

  my.width = function(value) {
    if (!arguments.length) return width;
    width = value;
    return my;
  };

  my.nodes = function(value) {
    if (!arguments.length) return nodes;
    nodes = value;
    return my;
  };

  my.links = function(value) {
    if (!arguments.length) return links;
    links = value;
    return my;
  };

  my.height = function(value) {
    if (!arguments.length) return height;
    height = value;
    return my;
  };

  return my;
}
