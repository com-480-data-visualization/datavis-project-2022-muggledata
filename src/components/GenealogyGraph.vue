<template>
  <div id="genediv"></div>
</template>



<script>
import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5hierarchy from "@amcharts/amcharts5/hierarchy";

export default {
  name: 'GenealogyGraph',
  props: {},
  async mounted() {
    am5.ready(function() {

    // Create root element
    // https://www.amcharts.com/docs/v5/getting-started/#Root_element
    var root = am5.Root.new("genediv");


    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    root.setThemes([
      am5themes_Animated.new(root)
    ]);


    // Create wrapper container
    var container = root.container.children.push(am5.Container.new(root, {
      width: am5.percent(100),
      height: am5.percent(100),
      layout: root.verticalLayout
    }));


    // Create series
    // https://www.amcharts.com/docs/v5/charts/hierarchy/#Adding
    var series = container.children.push(am5hierarchy.Tree.new(root, {
      singleBranchOnly: false,
      downDepth: 1,
      initialDepth: 10,
      valueField: "value",
      categoryField: "name",
      childDataField: "children"
    }));

    /* am5.net.load("/data/Spells.csv").then(function(result) {
      series.data.setAll(am5.CSVParser.parse(result.response, {
        delimiter: ";",
        reverse: true,
        skipEmpty: true,
        useColumnNames: true
      }));
      console.log(result.response);
    }).catch(function(result) {
      // This gets executed if there was an error loading URL
      // ... handle error
      console.log("Error loading " + result.xhr.responseURL);
    });

    console.log(series.data); */


    // Generate and set data
    // https://www.amcharts.com/docs/v5/charts/hierarchy/#Setting_data
    var maxLevels = 3;
    var maxNodes = 3;
    var maxValue = 100;

    var data = {
      name: "Root",
      children: []
    }
    generateLevel(data, "", 0);

    series.data.setAll([data]);
    series.set("selectedDataItem", series.dataItems[0]);

    function generateLevel(data, name, level) {
      for (var i = 0; i < Math.ceil(maxNodes * Math.random()) + 1; i++) {
        var nodeName = name + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i];
        var child;
        if (level < maxLevels) {
          child = {
            name: nodeName + level
          }

          if (level > 0 && Math.random() < 0.5) {
            child.value = Math.round(Math.random() * maxValue);
          }
          else {
            child.children = [];
            generateLevel(child, nodeName + i, level + 1)
          }
        }
        else {
          child = {
            name: name + i,
            value: Math.round(Math.random() * maxValue)
          }
        }
        data.children.push(child);
      }

      level++;
      return data;
    }


    // Make stuff animate on load
    series.appear(1000, 100);

    }); // end am5.ready()

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

#genediv {
  width: 100%;
  height: 1100px;
}
</style>
