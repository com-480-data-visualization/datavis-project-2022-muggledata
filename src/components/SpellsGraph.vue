<template>
  <div id="spells_graph"></div>
  <div id="spelltextbox">
    <h1 style="text-align: center; color: var(--light_silver); font-family: 'Harry Potter', sans-serif;"> Spell Graph</h1>
    On this graph, you can see the evolution of the popularity of different through books. 
    <br><br>For each book, we took the top five spells and order them such that the top 1 is above the 2 and so on. 
     <br><br>The dots that are not connected to 
    other mean that they appear to be on the top 5 in only one book.
  </div>
</template>


<script>
import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5xy from "@amcharts/amcharts5/xy"

export default {
  name: 'SpellsGraph',
  mounted(){
    am5.ready(function() {
      // Create root element
      var root = am5.Root.new("spells_graph");

      // Set themes
      root.setThemes([
        am5themes_Animated.new(root)
      ]);
      root.interfaceColors.set("grid", am5.color(0xffffff))

      // Create chart
      var chart = root.container.children.push(
        am5xy.XYChart.new(root, {
          layout: root.verticalLayout,
          pinchZoomX:true
        })
      );

      // Add cursor
      var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
        behavior: "none"
      }));
      cursor.lineY.set("visible", false);

      // Create axes
      var xRenderer = am5xy.AxisRendererX.new(root, {});
      xRenderer.grid.template.set("location", 0.5);
      xRenderer.labels.template.setAll({
        location: 0.5,
        multiLocation: 0.5,
        fill: am5.color(0xffffff),
      });

      var xAxis = chart.xAxes.push(
        am5xy.CategoryAxis.new(root, {
          categoryField: "book",
          renderer: xRenderer,
          tooltip: am5.Tooltip.new(root, {})
        })
      );

      var yRenderer = am5xy.AxisRendererY.new(root, {inversed: true});
      yRenderer.grid.template.set("location", 0.5);
      yRenderer.labels.template.setAll({
        location: 0.5,
        multiLocation: 0.5,
        fill: am5.color(0xffffff),
      });

      var yAxis = chart.yAxes.push(
        am5xy.ValueAxis.new(root, {
          maxPrecision: 0,
          renderer: yRenderer,
          min: 0.5,
          max: 5.5,
          strictMinMax: true,
        })
      );

      // Load xAxis categories
      am5.net.load("./data/spells_book2.json").then(function(result) {
        xAxis.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {

        console.log("Error loading " + result.xhr.responseURL);
      })

      // Add series
      function createSeries(name, field) {
        var series = chart.series.push(
          am5xy.LineSeries.new(root, {
            name: name,
            xAxis: xAxis,
            yAxis: yAxis,
            valueYField: field,
            categoryXField: "book",
            tooltip: am5.Tooltip.new(root, {
              pointerOrientation: "horizontal",
              labelText: "[bold]{name}[/]\n{categoryX}: {valueY}"
            })
          })
        );

        series.bullets.push(function() {
          return am5.Bullet.new(root, {
            sprite: am5.Circle.new(root, {
              radius: 5,
              fill: series.get("fill")
            })
          });
        });

        // Load data
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

      // Create series
      const spells = new Set();
      am5.net.load("./data/spells_book2.json").then(function(result) {
        am5.JSONParser.parse(result.response).forEach(function(k){
          const keys = Object.keys(k);
          keys.forEach(k => spells.add(k))
        });
        spells.delete("book")
        spells.forEach(function(item){
          createSeries(item.toString(), item.toString());
        });
      }).catch(function(result) {
        console.log("Error loading " + result.xhr.responseURL);
      })

      // Setup legend
      var legend = chart.children.push(
        am5.Legend.new(root, {
          centerX: am5.p50,
          x: am5.p50,
          forceHidden: true
        }),
      );

      legend.data.setAll(chart.series.values);

      // Make stuff animate on load
      chart.appear(1000, 100);
    });
  }
}
</script>


<style scoped>
#spells_graph {
  width: 68%;
  height: 700px;
  margin-left: 30%;
  background-color: rgb(0, 0, 0, 0.7);
  margin-right: 50px;
  border-radius: 10px;
}

#spelltextbox {
  color: var(--light_silver);
  margin-top: -700px;
  height: 600px;
  width: 22%;
  z-index: 500;
  background-color: var(--navbar_background);
  padding: 50px;
  margin-left: 50px;
  border-radius: 10px;
  text-align: justify;
  margin-bottom: 50px;
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
</style>
