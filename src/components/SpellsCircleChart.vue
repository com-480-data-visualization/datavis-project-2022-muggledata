<template>
  <div id="spells_circle_chart"></div>
  <div id="spelltextbox">
    <h1 style="text-align: center; color: var(--light_silver); font-family: 'Harry Potter', sans-serif;"> Bubble Chart</h1>
    Here we put the explanation of the bubble chart. <br><br>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. <br>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. <br>
  </div>
</template>

<script>

import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5hierarchy from "@amcharts/amcharts5/hierarchy";

export default {
  name: 'SpellsCircleChart',
  props: {},
  mounted(){
    am5.ready(function() {
      //document.getElementById("spelltextbox").textContent += "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. "

      var root = am5.Root.new("spells_circle_chart");
      root.setThemes([
        am5themes_Animated.new(root)
      ]);

      var container = root.container.children.push(am5.Container.new(root, {
        width: am5.percent(100),
        height: am5.percent(100),
        layout: root.verticalLayout
      }));

      var series = container.children.push(am5hierarchy.Pack.new(root, {
        singleBranchOnly: false,
        downDepth: 1,
        initialDepth: 1,
        valueField: "value",
        categoryField: "name",
        childDataField: "children",
      }));

      // series.get("colors").set("colors", [

      //   // am5.color(0x202124),
      //   // am5.color(0x9c1203),
      //   // am5.color(0x340601),
      //   // am5.color(0x680C02),
      //   // am5.color(0xe3a000),
      //   // am5.color(0x97C000),
      //   // am5.color(0x4BE000),
      //   // am5.color(0x033807),
      //   // am5.color(0x0112AD),
      //   // am5.color(0x02255A),
      //   // am5.color(0x00165e),
      //   // am5.color(0x000774),
      //   // am5.color(0x000EEA),
      //   // am5.color(0x2d004d),
      //   // am5.color(0x0F0019),
      //   // am5.color(0x1E0034),
      //   // am5.color(0x000034),
      //   // am5.color(0x639112),
      //   // am5.color(0x810293),
      // ]);

      series.set("heatRules", [{
        target: series.circles.template,
        dataField: "value",
        // min: am5.color(0xffcccc),
        // max: am5.color(0xff5555),
        // minValue: 60,
        // maxValue: 70,
        customFunction: function(sprite, min, max, value) {
          let color_min = new Color("white")
          let color_max = new Color("red")
          let gradient = color_min.range(color_max)
          if (value < 20) {
            sprite.set("fill", am5.color(0xff0000));
          }
          else {
            sprite.set("fill", am5.color(0x00ff00));
          }
        },
        key: "fill"
      }]);

      // var maxValue = 100;

      am5.net.load("./data/spells.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      })

      series.set("selectedDataItem", series.dataItems[0]);
      series.nodes.template.set("tooltipText", null);

      series.circles.template.setAll({
        fillOpacity: 1,
        strokeWidth: 1,
        strokeOpacity: 1,
      });
      
      series.labels.template.setAll({
        fontSize: 20,
        fill: am5.color(0xFFFFFF),
        text: "{category}"
      });
    });
  }
}



</script>


<style scoped>
#spells_circle_chart {
  width: 70%;
  height: 1100px;
}

#spelltextbox {
  margin-left: 70%;
  color: var(--light_silver);
  margin-top: -1100px;
  height: 1000px;
  z-index: 500;
  background-color: var(--navbar_background);
  padding: 50px;
  margin-right: 50px;
  border-radius: 10px;
  text-align: justify;
  margin-bottom: 100px;
}
</style>
