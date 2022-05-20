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

      var data = {
        name: "",
        children: [{"name": "Charm", "value": 38, "children": [{"name": "Stunning Spell", "value": 21}, {"name": "Summoning Charm", "value": 15}, {"name": "Shield Charm", "value": 13}, {"name": "Disarming Charm", "value": 8}, {"name": "Fidelius Charm", "value": 6}, {"name": "Wand-Lighting Charm", "value": 6}, {"name": "Disillusionment Charm", "value": 5}, {"name": "Severing Charm", "value": 4}, {"name": "Water-Making Spell", "value": 4}, {"name": "Muffliato Charm", "value": 4}, {"name": "Hover Charm", "value": 3}, {"name": "Patronus Charm", "value": 3}, {"name": "Caterwauling Charm", "value": 3}, {"name": "Confundus Charm", "value": 2}, {"name": "Levitation Charm", "value": 2}, {"name": "Tergeo", "value": 2}, {"name": "Descendo", "value": 2}, {"name": "Mending Charm", "value": 2}, {"name": "Extension Charm", "value": 1}, {"name": "Memory Charm", "value": 1}, {"name": "Permanent Sticking Charm", "value": 1}, {"name": "Unlocking Charm", "value": 1}, {"name": "Impervius Charm", "value": 1}, {"name": "Doubling Charm", "value": 1}, {"name": "Muggle-Repelling Charm", "value": 1}, {"name": "Erecto", "value": 1}, {"name": "Engorgement Charm", "value": 1}, {"name": "Shrinking Charm", "value": 1}, {"name": "Deprimo", "value": 1}, {"name": "Cushioning Charm", "value": 1}, {"name": "Gouging Spell", "value": 1}, {"name": "Locomotion Charm", "value": 1}, {"name": "Piertotum Locomotor", "value": 1}, {"name": "Glisseo", "value": 1}, {"name": "Hardening Charm", "value": 1}, {"name": "Wand-Extinguishing Charm", "value": 1}, {"name": "Silencing Charm", "value": 1}, {"name": "Supersensory Charm", "value": 1}]}, {"name": "Curse", "value": 12, "children": [{"name": "Killing Curse", "value": 18}, {"name": "Imperius Curse", "value": 9}, {"name": "Cruciatus Curse", "value": 7}, {"name": "Taboo", "value": 4}, {"name": "Dark Mark", "value": 4}, {"name": "Blasting Curse", "value": 3}, {"name": "Fiendfyre", "value": 2}, {"name": "Sectumsempra", "value": 1}, {"name": "Expulso Curse", "value": 1}, {"name": "Full Body-Bind Curse", "value": 1}, {"name": "Tongue-Tying Curse", "value": 1}, {"name": "Flagrante Curse", "value": 1}]}, {"name": "Transportation", "value": 1, "children": [{"name": "Apparition", "value": 17}]}, {"name": "Conjuration", "value": 2, "children": [{"name": "Water-Making Spell", "value": 4}, {"name": "Obscuro", "value": 1}]}, {"name": "Jinx", "value": 4, "children": [{"name": "Revulsion Jinx", "value": 4}, {"name": "Stinging Jinx", "value": 2}, {"name": "Impediment Jinx", "value": 1}, {"name": "Levicorpus", "value": 1}]}, {"name": "Counter-spell", "value": 1, "children": [{"name": "General Counter-Spell", "value": 2}]}, {"name": "Counter-charm", "value": 1, "children": [{"name": "Meteolojinx Recanto", "value": 2}]}, {"name": "Hex", "value": 2, "children": [{"name": "Stinging Jinx", "value": 2}, {"name": "Bedazzling Hex", "value": 1}]}, {"name": "Counter-jinx", "value": 1, "children": [{"name": "Liberacorpus", "value": 1}]}],
      }


      series.data.setAll([data]);
      series.set("selectedDataItem", series.dataItems[0]);
      series.nodes.template.set("tooltipText", null);

      series.circles.template.setAll({
        fillOpacity: 1,
        strokeWidth: .5,
        strokeOpacity: 1,
      });
      
      series.labels.template.setAll({
        fontSize: 20,
        fill: am5.color(0xFFFFFF),
        text: "{category}"
      });

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
