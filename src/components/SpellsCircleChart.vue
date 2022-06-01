<template>
  <div id="spells_circle_chart"></div>
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
        childDataField: "children"
      }));

      // series.get("colors").set("colors", [
      //   am5.color(0x202020),
      //   am5.color(0xAE0001),
      //   am5.color(0xD3A625),
      //   am5.color(0xEEBA30),
      //   am5.color(0x740001),
      //   am5.color(0x639112),
      //   am5.color(0x810293),
      // ]);

      // series.set("heatRules", [{
      //   target: series.circles.template,
      //   dataField: "value",
      //   min: am5.color(0xAE0001),
      //   max: am5.color(0xD3A625),
      //   minValue: 0,
      //   maxValue: 50,
      //   key: "fill"
      // }]);

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
  width: 100%;
  height: 1100px;
}
</style>
