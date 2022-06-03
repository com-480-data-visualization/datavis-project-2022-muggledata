<template>
  <div id="spells_circle_chart"></div>
  <div id="spelltextbox">
    <h1 style="text-align: center; color: var(--light_silver); font-family: 'Harry Potter', sans-serif;"> Bubble Chart</h1>
    In this bubble chart, you see the popularity of each spells that appear in all Harry Potter's books.
    <br><br>The first bubbles are the types of spell, bigger are the number of different spells of this type, the bigger is the
    bubble. By clicking on them, you can see every different spells of this particular type and the bigger they are
    , the more they are used in the book.
  </div>
</template>

<script>

import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5hierarchy from "@amcharts/amcharts5/hierarchy";

export default {
  name: 'SpellsCircleChart',
  mounted(){
    am5.ready(function() {
      // Create root
      var root = am5.Root.new("spells_circle_chart");
      root.setThemes([
        am5themes_Animated.new(root)
      ]);

      // Create container
      var container = root.container.children.push(am5.Container.new(root, {
        width: am5.percent(100),
        height: am5.percent(100),
        layout: root.verticalLayout,
      }));

      // Create series
      var series = container.children.push(am5hierarchy.Pack.new(root, {
        singleBranchOnly: false,
        downDepth: 1,
        initialDepth: 1,
        valueField: "value",
        categoryField: "name",
        childDataField: "children",
      }));

      // Set series colors
      series.get("colors").set("colors", [
        am5.color(0x106080),
        am5.color(0x095256),
        am5.color(0x087f8c),
        am5.color(0x5aaa95),
        am5.color(0x86a873),
        am5.color(0x86a830),
        am5.color(0x095256),
        am5.color(0x087f8c),
        am5.color(0x5aaa95),
        am5.color(0x86a873),
        am5.color(0xbb9f06)
      ]);

      // Load data
      am5.net.load("./data/spells.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        console.log("Error loading " + result.xhr.responseURL);
      })

      // Set selected
      series.set("selectedDataItem", series.dataItems[0]);

      // Set nodes tooltip
      series.nodes.template.set("tooltipText", "{name}");

      // Set circle sprites parameters
      series.circles.template.setAll({
        fillOpacity: 1,
        strokeWidth: 1,
        strokeOpacity: 1,
      });
      
      // Set labels parameters
      series.labels.template.setAll({
        fontSize: 15,
        fill: am5.color(0xFFFFFF),
        text: "{category}",
      });
    });
  }
}

</script>


<style scoped>
#spells_circle_chart {
  width: 68%;
  height: 1100px;
  margin-left: 50px;
  background-color: rgb(0, 0, 0, 0.7);
  border-radius: 10px;
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
  font-family: 'Fantasy';
  font-size: 22px;
  overflow: scroll;
}

p {
  font-family: 'Harry Potter', sans-serif;
  font-size: smaller;
  display: inline-block;
}

h1 {
  font-size: xx-large;
  font-family: 'Harry Potter', sans-serif;
}

h2 {
  font-family: 'Fantasy';
  font-size: 35px;
  background-color: rgb(0, 0, 0, 0.7);
}
</style>
