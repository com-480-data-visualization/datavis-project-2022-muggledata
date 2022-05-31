<template>
  <div id="spelldiv"></div>
  <div id="spellchart"></div>
</template>


<script>
import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5hierarchy from "@amcharts/amcharts5/hierarchy";
import * as am5xy from "@amcharts/amcharts5/xy"

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
        strokeWidth: 1,
        strokeOpacity: 1,
      });
      
      series.labels.template.setAll({
        fontSize: 20,
        fill: am5.color(0xFFFFFF),
        text: "{category}"
      });





      // Create root element
      // https://www.amcharts.com/docs/v5/getting-started/#Root_element
      var root2 = am5.Root.new("spellchart");

      // Set themes
      // https://www.amcharts.com/docs/v5/concepts/themes/
      root2.setThemes([
        am5themes_Animated.new(root2)
      ]);
      root2.interfaceColors.set("grid", am5.color(0xffffff))

      // Create chart
      // https://www.amcharts.com/docs/v5/charts/xy-chart/
      var chart = root2.container.children.push(
        am5xy.XYChart.new(root2, {
          panX: true,
          panY: true,
          wheelX: "panX",
          wheelY: "zoomX",
          layout: root2.verticalLayout,
          pinchZoomX:true
        })
      );
      chart.get("colors").set("colors", [
        am5.color(0xffffff),
        am5.color(0xf00fff),
        am5.color(0xfff00f),
      ]);

      // Add cursor
      // https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
      var cursor = chart.set("cursor", am5xy.XYCursor.new(root2, {
        behavior: "none"
      }));
      cursor.lineY.set("visible", false);

      // The data
      // var data2 = [
      //   {
      //     year: "1930",
      //     italy: -5,
      //     germany: 5,
      //     uk: 3
      //   },
      //   {
      //     year: "1934",
      //     italy: 1,
      //     germany: 2,
      //     uk: 6
      //   },
      //   {
      //     year: "1938",
      //     italy: 2,
      //     germany: 3,
      //     uk: 1
      //   }
      // ];
      var data2 = [{"book": "Book1", "Stunning Spell": 2, "Killing Curse": 3, "Apparition": 1, "Summoning Charm": 1, "Shield Charm": 2, "Imperius Curse": 1}, {"book": "Book2", "Stunning Spell": 2, "Killing Curse": 4, "Apparition": 2, "Summoning Charm": 1, "Shield Charm": 1, "Imperius Curse": 5, "Disarming Charm": 1}, {"book": "Book3", "Stunning Spell": 8, "Killing Curse": 4, "Apparition": 1, "Summoning Charm": 4, "Shield Charm": 1, "Imperius Curse": 1, "Disarming Charm": 1, "Cruciatus Curse": 1}, {"book": "Book4", "Stunning Spell": 10, "Killing Curse": 9, "Apparition": 9, "Summoning Charm": 15, "Shield Charm": 2, "Imperius Curse": 18, "Disarming Charm": 3, "Cruciatus Curse": 15, "Fidelius Charm": 3, "Wand-Lighting Charm": 2, "Disillusionment Charm": 1, "Severing Charm": 28, "Water-Making Spell": 1, "Muffliato Charm": 3, "Revulsion Jinx": 2, "Taboo": 1, "Dark Mark": 1}, {"book": "Book5", "Stunning Spell": 11, "Killing Curse": 2, "Apparition": 14, "Summoning Charm": 11, "Shield Charm": 6, "Imperius Curse": 9, "Disarming Charm": 8, "Cruciatus Curse": 7, "Fidelius Charm": 3, "Wand-Lighting Charm": 3, "Disillusionment Charm": 1, "Severing Charm": 1, "Water-Making Spell": 6, "Muffliato Charm": 1, "Revulsion Jinx": 1, "Taboo": 3, "Dark Mark": 9, "Blasting Curse": 2, "Hover Charm": 3, "Patronus Charm": 4, "Caterwauling Charm": 1, "Confundus Charm": 2, "Levitation Charm": 9}, {"book": "Book6", "Stunning Spell": 1, "Killing Curse": 6, "Apparition": 34, "Summoning Charm": 3, "Shield Charm": 4, "Imperius Curse": 9, "Disarming Charm": 2, "Cruciatus Curse": 3, "Fidelius Charm": 3, "Wand-Lighting Charm": 1, "Disillusionment Charm": 1, "Severing Charm": 14, "Water-Making Spell": 3, "Muffliato Charm": 1, "Revulsion Jinx": 14, "Taboo": 1, "Dark Mark": 1, "Blasting Curse": 4, "Hover Charm": 3, "Patronus Charm": 6, "Caterwauling Charm": 5, "Confundus Charm": 1, "Levitation Charm": 5, "Tergeo": 1}, {"book": "Book7", "Stunning Spell": 21, "Killing Curse": 18, "Apparition": 17, "Summoning Charm": 15, "Shield Charm": 13, "Imperius Curse": 9, "Disarming Charm": 8, "Cruciatus Curse": 7, "Fidelius Charm": 6, "Wand-Lighting Charm": 6, "Disillusionment Charm": 5, "Severing Charm": 4, "Water-Making Spell": 4, "Muffliato Charm": 4, "Revulsion Jinx": 4, "Taboo": 4, "Dark Mark": 4, "Blasting Curse": 3, "Hover Charm": 3, "Patronus Charm": 3, "Caterwauling Charm": 3, "Confundus Charm": 2, "Levitation Charm": 2, "Tergeo": 2, "Descendo": 2, "General Counter-Spell": 2, "Meteolojinx Recanto": 2, "Mending Charm": 2, "Stinging Jinx": 2, "Fiendfyre": 2, "Impediment Jinx": 1, "Sectumsempra": 1, "Extension Charm": 1, "Expulso Curse": 1, "Full Body-Bind Curse": 1, "Memory Charm": 1, "Tongue-Tying Curse": 1, "Permanent Sticking Charm": 1, "Unlocking Charm": 1, "Impervius Charm": 1, "Doubling Charm": 1, "Muggle-Repelling Charm": 1, "Erecto": 1, "Obscuro": 1, "Engorgement Charm": 1, "Shrinking Charm": 1, "Bedazzling Hex": 1, "Deprimo": 1, "Cushioning Charm": 1, "Flagrante Curse": 1, "Levicorpus": 1, "Liberacorpus": 1, "Gouging Spell": 1, "Locomotion Charm": 1, "Piertotum Locomotor": 1, "Glisseo": 1, "Hardening Charm": 1, "Wand-Extinguishing Charm": 1, "Silencing Charm": 1, "Supersensory Charm": 1}];

      // Create axes
      // https://www.amcharts.com/docs/v5/charts/xy-chart/axes/
      var xRenderer = am5xy.AxisRendererX.new(root2, {});
      xRenderer.grid.template.set("location", 0.5);
      xRenderer.labels.template.setAll({
        location: 0.5,
        multiLocation: 0.5,
        fill: am5.color(0xffffff)
      });

      var xAxis = chart.xAxes.push(
        am5xy.CategoryAxis.new(root2, {
          categoryField: "book",
          renderer: xRenderer,
          tooltip: am5.Tooltip.new(root2, {})
        })
      );

      xAxis.data.setAll(data2);

      var yRenderer = am5xy.AxisRendererY.new(root2, {});
      yRenderer.grid.template.set("location", 0.5);
      yRenderer.labels.template.setAll({
        location: 0.5,
        multiLocation: 0.5,
        fill: am5.color(0xffffff),
      });

      var yAxis = chart.yAxes.push(
        am5xy.ValueAxis.new(root2, {
          maxPrecision: 0,
          renderer: yRenderer,
          min: 0
        })
      );

      // Add series
      // https://www.amcharts.com/docs/v5/charts/xy-chart/series/

      function createSeries(name, field) {
        var series = chart.series.push(
          am5xy.LineSeries.new(root2, {
            name: name,
            xAxis: xAxis,
            yAxis: yAxis,
            valueYField: field,
            categoryXField: "book",
            tooltip: am5.Tooltip.new(root2, {
              pointerOrientation: "horizontal",
              labelText: "[bold]{name}[/]\n{categoryX}: {valueY}"
            })
          })
        );


        series.bullets.push(function() {
          return am5.Bullet.new(root2, {
            sprite: am5.Circle.new(root2, {
              radius: 5,
              fill: series.get("fill")
            })
          });
        });

        // create hover state for series and for mainContainer, so that when series is hovered,
        // the state would be passed down to the strokes which are in mainContainer.
        series.set("setStateOnChildren", true);
        series.states.create("hover", {});

        series.mainContainer.set("setStateOnChildren", true);
        series.mainContainer.states.create("hover", {});

        series.strokes.template.states.create("hover", {
          strokeWidth: 4
        });

        series.data.setAll(data2);
        series.appear(1000);
      }
      const spells = new Set();
      data2.forEach(function(item){
        const keys = Object.keys(item);
        spells.push(keys);
      });

      spells.forEach(function(item){
        createSeries(item.toString(), item.toString());
      });

      // createSeries("Stunning Spell", "Stunning Spell");
      // createSeries("Killing Curse", "Killing Curse");

      // Add scrollbar
      // https://www.amcharts.com/docs/v5/charts/xy-chart/scrollbars/
      chart.set("scrollbarX", am5.Scrollbar.new(root2, {
        orientation: "horizontal",
        marginBottom: 20
      }));

      var legend = chart.children.push(
        am5.Legend.new(root2, {
          centerX: am5.p50,
          x: am5.p50,
        }),
      );

      // Make series change state when legend item is hovered
      legend.itemContainers.template.states.create("hover", {});

      legend.itemContainers.template.events.on("pointerover", function(e) {
        e.target.dataItem.dataContext.hover();
      });
      legend.itemContainers.template.events.on("pointerout", function(e) {
        e.target.dataItem.dataContext.unhover();
      });

      legend.data.setAll(chart.series.values);

      // Make stuff animate on load
      // https://www.amcharts.com/docs/v5/concepts/animations/
      chart.appear(1000, 100);
    });
  }
}



</script>


<style scoped>
#spellchart {
  width: 80%;
  height: 700px;
}

#spelldiv {
  width: 100%;
  height: 1100px;
}
</style>
