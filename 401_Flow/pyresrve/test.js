window.onload = function() {
    // Parse the DOT syntax into a graphlib object.
    var g = graphlibDot.parse(
      'digraph {\n' +
      '    a -> b;\n' +
      '    }'
    )
  
    // Render the graphlib object using d3.
    var renderer = new dagreD3.Renderer();
    renderer.run(g, d3.select("svg g"));
  
  
    // Optional - resize the SVG element based on the contents.
    var svg = document.querySelector('#graphContainer');
    var bbox = svg.getBBox();
    svg.style.width = bbox.width + 40.0 + "px";
    svg.style.height = bbox.height + 40.0 + "px";
  }