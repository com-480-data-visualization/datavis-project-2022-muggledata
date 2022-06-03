<template>
  <div id="sentiment_analysis_graph"></div>
  <div id="sentiment_analysis_textbox">
    <h1 style="text-align: center; color: var(--light_silver); font-family: 'Harry Potter', sans-serif;"> Sentiment Analysis</h1>
    We performed a sentiment analysis of each book to easily grasp the evolution of the script.  <br><br>
    The legend allows to select each book separately and show the evolution of sentiment (higher the happiest) along the parts of the book. 
     <br><br>[Spoiler Alert]<br>Try hovering some bullets to get an insight of what happens in the book !
    <br>
  </div>
</template>


<script>
import * as am5 from "@amcharts/amcharts5";
import am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5xy from "@amcharts/amcharts5/xy"

export default {
  name: 'SentimentAnalysisGraph',
  mounted(){
    am5.ready(function() {
      // Create root element
      var root = am5.Root.new("sentiment_analysis_graph");

      // Set themes
      root.setThemes([
        am5themes_Animated.new(root)
      ]);

      // Set grid color
      root.interfaceColors.set("grid", am5.color(0xd6d6d7))

      // Create chart
      var chart = root.container.children.push(
        am5xy.XYChart.new(root, {
          layout: root.verticalLayout,
        })
      );

      // Create axes
      var xRenderer = am5xy.AxisRendererX.new(root, {minGridDistance: 10});
      xRenderer.grid.template.set("location", 0.5);
      xRenderer.grid.template.set("gridCount", 10);
      xRenderer.labels.template.setAll({
        fill: am5.color(0xd6d6d7),
      });

      var xAxis = chart.xAxes.push(
        am5xy.CategoryAxis.new(root, {
          categoryField: "part",
          renderer: xRenderer,
        })
      );

      var yRenderer = am5xy.AxisRendererY.new(root, {});
      yRenderer.labels.template.setAll({
        location: 0.5,
        multiLocation: 0.5,
        fill: am5.color(0xd6d6d7),
      });

      var yAxis = chart.yAxes.push(
        am5xy.ValueAxis.new(root, {
          maxPrecision: 0,
          renderer: yRenderer,
          min: -51,
          max: 51,
          strictMinMax: true,
        })
      );

      // Set xAxis categories
      am5.net.load("./data/sentiment_analysis_with_descriptions.json").then(function(result) {
        let data = am5.JSONParser.parse(result.response)
        xAxis.data.setAll(data[0]["data"]);
      }).catch(function(result) {
        console.log("Error loading " + result.xhr.responseURL);
      })

      // Setup Legend
      var legend = chart.children.push(
        am5.Legend.new(root, {
          centerX: am5.p50,
          x: am5.p50,
          layout: root.gridLayout,
          background: am5.RoundedRectangle.new(root, {
            fill: am5.color(0x606060),
            fillOpacity: 1
          })
        })
      );

      // Set chart colors
      chart.get("colors").set("colors", [
        am5.color(0x106080),
        am5.color(0x095256),
        am5.color(0x087f8c),
        am5.color(0x5aaa95),
        am5.color(0x86a873),
        am5.color(0x8aaf93),
        am5.color(0xacc1b3),
      ]);

      // Create series function
      function createSeries(name, field, data, visible) {
        var series = chart.series.push(
          am5xy.LineSeries.new(root, {
            name: name,
            xAxis: xAxis,
            yAxis: yAxis,
            valueYField: field,
            categoryXField: "part",
            valueField : "description",
            tooltip: am5.Tooltip.new(root, {
              pointerOrientation: "horizontal",
              labelText: "{value}",
            }),
            visible: visible,
          })
        );
        series.strokes.template.setAll({
          strokeWidth: 4,
        })

        // Add bullets
        series.bullets.push(function() {
          return am5.Bullet.new(root, {
            sprite: am5.Circle.new(root, {
              radius: 7,
              fill: series.get("fill"),
            })
          });
        });

        // Set series and legend data
        series.data.setAll(data);
        legend.data.push(series);

        if(!visible){
          series.hide()
        }
        
        // Define visible function callback
        series.on("visible", function(visible, target) {
          if (visible) {
            chart.series.each(function(series) {
              if (series !== target) {
                series.set("visible", false);
                series.hide();
              } else {
                series.show();
              }
            });
          }
        });
      }

      // Set cursor
      chart.set("cursor", am5xy.XYCursor.new(root, {
        behavior: "none",
      }));

      // Load data
      am5.net.load("./data/sentiment_analysis_with_descriptions.json").then(function(result) {
        am5.JSONParser.parse(result.response).forEach(function(item){
          if(item["book"] == "Book 1"){
            console.log("AAAAAAAAAA")
            createSeries(item["book"], "count", item["data"], true);
          } else {
            createSeries(item["book"], "count", item["data"], false);
          }
        });
      }).catch(function(result) {
        console.log("Error loading " + result.xhr.responseURL);
      })
    });
  }
}

</script>


<style scoped>
#sentiment_analysis_graph {
  width: 67%;
  height: 700px;
  margin-left: 30%;
  margin-right: 50px;
  background-color: rgb(0, 0, 0, 0.7);
  border-radius: 10px;
}

#sentiment_analysis_textbox {
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
  font-family: 'Fantasy';
  font-size: 22px;
  overflow: scroll;
  margin-bottom: 50px;
}
</style>
