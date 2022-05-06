<template>
  <div id="spelldiv"></div>
</template>


<script>
import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5hierarchy from "@amcharts/amcharts5/hierarchy";

export default {
  name: 'SpellsChart',
  props: {},
  mounted(){
    am5.ready(function() {

    var root = am5.Root.new("spelldiv");
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
      initialDepth: 10,
      valueField: "value",
      categoryField: "name",
      childDataField: "children"
    }));

    series.get("colors").set("colors", [
      am5.color(0xC0C0C0),
      am5.color(0xAE0001),
      am5.color(0xD3A625),
      am5.color(0xEEBA30),
      am5.color(0x740001)
    ]);

    var maxValue = 100;

    var data = {
      name: "Spells",
      children: [],
    }
    generateLevel(data, "Spell ", 0);

    series.data.setAll([data]);
    series.set("selectedDataItem", series.dataItems[0]);

    function generateLevel(data) {

      let types = ['Charm', 'Jinx', 'Transfiguration'];
      types.forEach(type => {
        var value = Math.round(Math.random() * maxValue);
        var child = {
          name: type,
          value: value,
        }

        child.children = [
          {
            name: 'Spell 1',
            value: Math.round(Math.random() * maxValue)
          }, 
          {
            name: 'Spell 2',
            value: Math.round(Math.random() * maxValue)
          }, 
          {
            name: 'Spell 3',
            value: Math.round(Math.random() * maxValue)
          }, 
          {
            name: 'Spell 4',
            value: Math.round(Math.random() * maxValue)
          }, 
        ];
        data.children.push(child);
      });
     
      return data;
    }

    series.appear(1000, 100);

    });
  }
}



</script>


<style scoped>
#spelldiv {
  width: 100%;
  height: 1100px;
}
</style>
