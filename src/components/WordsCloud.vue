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
      width: am5.percent(80),
      height: am5.percent(10),
      //layout: root.verticalLayout,
      layout: root.horizontalLayout
    }));

    var container_cloud = root.container.children.push(am5.Container.new(root, {
      width: am5.percent(80),
      height: am5.percent(80),
      //layout: root.verticalLayout,
      layout: root.horizontalLayout
    }));


    // Add chart title
    // var title = container.children.push(am5.Label.new(root, {
    //   text: "Most popular languages on StackOverflow",
    //   fontSize: 20,
    //   x: am5.percent(50),
    //   centerX: am5.percent(50)
    // }));

    let button1 = container.children.push(am5.Button.new(root, {
      dx: 10,
      dy: 10,
      label: am5.Label.new(root, {
        text: "Harry Potter and \n the Philosophers Stone",
        textAlign: "center",
        marginLeft: -10,
        marginRight: -10,
        fontSize: 12,
      }),
    }));
    console.log(button1.width())
    button1.events.on("click", function(ev) {
      console.log(ev)
      am5.net.load("/data/2_gram_words_specific_book1.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });
    });
    let button2 = container.children.push(am5.Button.new(root, {
      dx: 10,
      dy: 10,
      label: am5.Label.new(root, {
        text: "Harry Potter and \n the Chamber of Secrets",
        textAlign: "center",
        marginLeft: -10,
        marginRight: -10,
        fontSize: 12,
      }),
    }));
    button2.events.on("click", function(ev) {
      console.log(ev)
      am5.net.load("/data/2_gram_words_specific_book2.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });
    });
    let button3 = container.children.push(am5.Button.new(root, {
      dx: 10,
      dy: 10,
      label: am5.Label.new(root, {
        text: "Harry Potter and \n the Prisoner of Azkaban",
        textAlign: "center",
        marginLeft: -10,
        marginRight: -10,
        fontSize: 12,
      }),
    }));
    button3.events.on("click", function(ev) {
      console.log(ev)
      am5.net.load("/data/2_gram_words_specific_book3.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });
    });
    let button4 = container.children.push(am5.Button.new(root, {
      dx: 10,
      dy: 10,
      label: am5.Label.new(root, {
        text: "Harry Potter and \n the Goblet of Fire",
        textAlign: "center",
        marginLeft: -10,
        marginRight: -10,
        fontSize: 12,
      }),
    }));
    button4.events.on("click", function(ev) {
      console.log(ev)
      am5.net.load("/data/2_gram_words_specific_book4.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });
    });
    let button5 = container.children.push(am5.Button.new(root, {
      dx: 10,
      dy: 10,
      label: am5.Label.new(root, {
        text: "Harry Potter and \n the Order of the Phoenix",
        textAlign: "center",
        marginLeft: -10,
        marginRight: -10,
        fontSize: 12,
      }),
    }));
    button5.events.on("click", function(ev) {
      console.log(ev)
      am5.net.load("/data/2_gram_words_specific_book5.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });
    });
    let button6 = container.children.push(am5.Button.new(root, {
      dx: 10,
      dy: 10,
      label: am5.Label.new(root, {
        text: "Harry Potter and \n the Half Blood Prince",
        textAlign: "center",
        marginLeft: -10,
        marginRight: -10,
        fontSize: 12,
      }),
    }));
    button6.events.on("click", function(ev) {
      console.log(ev)
      am5.net.load("/data/2_gram_words_specific_book6.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });
    });
    let button7 = container.children.push(am5.Button.new(root, {
      dx: 10,
      dy: 10,
      label: am5.Label.new(root, {
        text: "Harry Potter and \n the Deathly Hallows",
        textAlign: "center",
        marginLeft: -10,
        marginRight: -10,
        fontSize: 12,
      }),
    }));
    button7.events.on("click", function(ev) {
      console.log(ev)
      am5.net.load("/data/2_gram_words_specific_book7.json").then(function(result) {
        series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });
    });
    
    // Add series
    // https://www.amcharts.com/docs/v5/charts/word-cloud/
    var series = container_cloud.children.push(am5wc.WordCloud.new(root, {
      categoryField: "Words",
      valueField: "Count",
      calculateAggregates: true, // this is needed for heat rules to work
      legendLabelText: "legends",
      minFontSize: 15,
      maxFontSize: 60,
      marginTop: 100,
      layout: root.verticalLayout,
    }));
    

    // Set up heat rules
    // https://www.amcharts.com/docs/v5/charts/word-cloud/#Via_heat_rules
    series.set("heatRules", [{
      target: series.labels.template,
      dataField: "value",
      min: am5.color(0xFFCCCC),
      max: am5.color(0xFF0000),
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
      window.open("https://fr.wikipedia.org/wiki/" + encodeURIComponent(category));
    });

    }); // end am5.ready()
  }
}
</script>
