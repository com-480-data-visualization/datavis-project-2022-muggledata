<template>
  <div id="sentiment_analysis_graph"></div>
  <div id="sentiment_analysis_textbox">
    <h1 style="text-align: center; color: var(--light_silver); font-family: 'Harry Potter', sans-serif;"> Sentiment Analysis</h1>
    Here we put the explanation of the spell graph. <br><br>
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
import * as am5xy from "@amcharts/amcharts5/xy"

export default {
  name: 'SentimentAnalysisGraph',
  props: {},
  mounted(){
    am5.ready(function() {
      // Create root element
      // https://www.amcharts.com/docs/v5/getting-started/#Root_element
      var root = am5.Root.new("sentiment_analysis_graph");

      // Set themes
      // https://www.amcharts.com/docs/v5/concepts/themes/
      root.setThemes([
        am5themes_Animated.new(root)
      ]);
      root.interfaceColors.set("grid", am5.color(0xff0000))

      // Create chart
      // https://www.amcharts.com/docs/v5/charts/xy-chart/
      var chart = root.container.children.push(
        am5xy.XYChart.new(root, {
          panX: true,
          panY: true,
          wheelX: "panX",
          wheelY: "zoomX",
          layout: root.verticalLayout,
          pinchZoomX:true
        })
      );

      // Create axes
      var xRenderer = am5xy.AxisRendererX.new(root, {});
      xRenderer.grid.template.set("location", 0.5);
      xRenderer.labels.template.setAll({
        location: 0.5,
        multiLocation: 0.5,
        fill: am5.color(0xd6d6d7),
        
      });

      var xAxis = chart.xAxes.push(
        am5xy.CategoryAxis.new(root, {
          categoryField: "part",
          renderer: xRenderer,
          //tooltip: am5.Tooltip.new(root, {})
        })
      );

      am5.net.load("./data/sentiment_analysis.json").then(function(result) {
        let data = am5.JSONParser.parse(result.response)
        xAxis.data.setAll(data[0]["data"]);
      }).catch(function(result) {
        console.log("Error loading " + result.xhr.responseURL);
      })

      var yRenderer = am5xy.AxisRendererY.new(root, {});
      yRenderer.grid.template.set("location", 0.5);
      yRenderer.labels.template.setAll({
        location: 0.5,
        multiLocation: 0.5,
        fill: am5.color(0xd6d6d7),
      });

      var yAxis = chart.yAxes.push(
        am5xy.ValueAxis.new(root, {
          maxPrecision: 0,
          renderer: yRenderer,
        })
      );

      var legend = chart.children.push(
        am5.Legend.new(root, {
          centerX: am5.p50,
          x: am5.p50,
          layout: root.horizontalLayout,
        })
      );

      // Create series
      function createSeries(name, field, data, visible) {
        var series = chart.series.push(
          am5xy.LineSeries.new(root, {
            name: name,
            xAxis: xAxis,
            yAxis: yAxis,
            valueYField: field,
            categoryXField: "part",
            //categoryYField: "description",
            //valueField : "description",
            // tooltip: am5.Tooltip.new(root, {
            //   pointerOrientation: "horizontal",
            //   labelText: "{value}",
            //   visible: visible
            // }),
            visible: visible
          })
        );

        series.bullets.push(function() {
          return am5.Bullet.new(root, {
            sprite: am5.Circle.new(root, {
              radius: 5,
              fill: series.get("fill"),
            })
          });
        });

        // create hover state for series and for mainContainer, so that when series is hovered,
        // the state would be passed down to the strokes which are in mainContainer.
        series.set("setStateOnChildren", visible);
        series.states.create("hover", {});

        series.mainContainer.set("setStateOnChildren", visible);
        series.mainContainer.states.create("hover", {});

        series.data.setAll(data);
        legend.data.push(series);

        series.on("visible", function(visible, target) {
          if (visible) {
            chart.series.each(function(series) {
              if (series !== target) {
                series.set("visible", false);
                //series.get("tooltip").set("visible", false)
              }
            });
          }
        });
        series.appear(1000)
      }

      // Add cursor
      // https://www.amcharts.com/docs/v5/charts/xy-chart/cursor/
      // var cursor = chart.set("cursor", am5xy.XYCursor.new(root, {
      //   behavior: "none",
      // }));
      // cursor
      chart.set("cursor", am5xy.XYCursor.new(root, {
        behavior: "none",
      }));

      var first = true;
      am5.net.load("./data/sentiment_analysis.json").then(function(result) {
        am5.JSONParser.parse(result.response).forEach(function(item){
          if(first){
            first = false;
            createSeries(item["book"], "count", item["data"], true);
          } else {
            createSeries(item["book"], "count", item["data"], false);
          }
        });
      }).catch(function(result) {
        console.log("Error loading " + result.xhr.responseURL);
      })

      chart.appear(1000, 100);
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
  background-color: rgb(0, 0, 0, 0.6);
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
  margin-bottom: 50px;
}
</style>
