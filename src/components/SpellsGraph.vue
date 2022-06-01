<template>
  <div id="spells_graph"></div>
</template>


<script>
import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5xy from "@amcharts/amcharts5/xy"

export default {
  name: 'SpellsGraph',
  props: {},
  mounted(){
    am5.ready(function() {
      // Create root element
      // https://www.amcharts.com/docs/v5/getting-started/#Root_element
      var root2 = am5.Root.new("spells_graph");

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
      am5.net.load("./data/spells_book2.json").then(function(result) {
        xAxis.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {

        console.log("Error loading " + result.xhr.responseURL);
      })

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
          min: 0,
          //max: 6
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
        am5.net.load("./data/spells_book2.json").then(function(result) {
          series.data.setAll(am5.JSONParser.parse(result.response));
        }).catch(function(result) {
          // This gets executed if there was an error loading URL
          // ... handle error
          console.log("Error loading " + result.xhr.responseURL);
        })
        //series.data.setAll(data2);
        series.appear(1000);
      }
      const spells = new Set();
      am5.net.load("./data/spells_book2.json").then(function(result) {
        am5.JSONParser.parse(result.response).forEach(function(k){
          const keys = Object.keys(k);
          keys.forEach(k => spells.add(k))
        });
        spells.delete("book")

        spells.forEach(function(item){
          //console.log(item);
          createSeries(item.toString(), item.toString());
        });
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      })

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
          forceHidden: true
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
#spells_graph {
  width: 80%;
  height: 700px;
}
</style>
