<!-- HTML -->
<template>
  <div id="chartdiv"></div>
</template>

<!-- Styles -->
<style>
#chartdiv {
  width: 100%;
  height: 1100px;
}
</style>

<!-- Resources -->
<!-- <script src="https://cdn.amcharts.com/lib/5/index.js"></script>
<script src="https://cdn.amcharts.com/lib/5/wc.js"></script>
<script src="https://cdn.amcharts.com/lib/5/themes/Animated.js"></script> -->

<!-- Chart code -->
<script>
import * as am5 from "@amcharts/amcharts5";
// import * as am5themes_Animated from "@amcharts/amcharts5/themes/Animated";
import * as am5wc from "@amcharts/amcharts5/wc";

export default {
  name: 'WordsCloud',
  props: {},
  mounted(){
    //import * as am5hierarchy from "@amcharts/amcharts5/hierarchy";
    am5.ready(function() {

    // Create root element
    // https://www.amcharts.com/docs/v5/getting-started/#Root_element
    var root = am5.Root.new("chartdiv");


    // Set themes
    // https://www.amcharts.com/docs/v5/concepts/themes/
    // root.setThemes([
    //   am5themes_Animated.new(root)
    // ]);


    // Add wrapper container
    var container = root.container.children.push(am5.Container.new(root, {
      width: am5.percent(100),
      height: am5.percent(100),
      layout: root.verticalLayout
    }));


    // Add chart title
    // var title = container.children.push(am5.Label.new(root, {
    //   text: "Most popular languages on StackOverflow",
    //   fontSize: 20,
    //   x: am5.percent(50),
    //   centerX: am5.percent(50)
    // }));


    // Add series
    // https://www.amcharts.com/docs/v5/charts/word-cloud/
    var series = container.children.push(am5wc.WordCloud.new(root, {
      categoryField: "tag",
      valueField: "weight",
      calculateAggregates: true // this is needed for heat rules to work
    }));


    // Set up heat rules
    // https://www.amcharts.com/docs/v5/charts/word-cloud/#Via_heat_rules
    series.set("heatRules", [{
      target: series.labels.template,
      dataField: "value",
      min: am5.color(0xFFD4C2),
      max: am5.color(0xFF621F),
      key: "fill"
    }]);


    // Configure labels
    series.labels.template.setAll({
      paddingTop: 5,
      paddingBottom: 5,
      paddingLeft: 5,
      paddingRight: 5,
      fontFamily: "Courier New",
      cursorOverStyle: "pointer"
    });


    // Add click event on words
    // https://www.amcharts.com/docs/v5/charts/word-cloud/#Events
    series.labels.template.events.on("click", function(ev) {
      const category = ev.target.dataItem.get("category");
      window.open("https://stackoverflow.com/questions/tagged/" + encodeURIComponent(category));
    });


    // Data from:
    // https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-programming-scripting-and-markup-languages
    series.data.setAll([
      { tag: "Harry", weight: 70. },
      { tag: "Hermione", weight: 50. },
      { tag: "Dumbeldore", weight: 35 },
      { tag: "looked", weight: 33 },
      { tag: "Proffessor", weight: 31},
      { tag: "Hagrid", weight: 30.5},
      { tag: "time", weight: 30.2},
      { tag: "Snape", weight: 30.1},
      { tag: "eyes", weight: 30.05},
      { tag: "wand", weight: 29.9},
      { tag: "Potter", weight: 29.8},
      { tag: "face", weight: 29.5},
      { tag: "Weasley", weight: 29.5},
      { tag: "voice", weight: 29.5},
      { tag: "again", weight: 29.5},
    ]);

    }); // end am5.ready()
  }
}
</script>
