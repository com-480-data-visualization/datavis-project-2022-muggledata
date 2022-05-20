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

    // sourceText = "kjwef wef qwefsd few f wef ww ef wef wef wef  fe f we dcas df"
    
    // Add series
    // https://www.amcharts.com/docs/v5/charts/word-cloud/
    var series = container.children.push(am5wc.WordCloud.new(root, {
      categoryField: "Word",
      valueField: "Count",
      calculateAggregates: true, // this is needed for heat rules to work
      legendLabelText: "legends",
    }));
    

    // Set up heat rules
    // https://www.amcharts.com/docs/v5/charts/word-cloud/#Via_heat_rules
    series.set("heatRules", [{
      target: series.labels.template,
      dataField: "value",
      // customFunction: function(sprite, min, max, value) {
      //   if (value < 50) {
      //       sprite.set("fill", am5.color(0xff0000));
      //     }
      //     else {
      //       sprite.set("fill", am5.color(0x00ff00));
      //     }
      //   },
      min: am5.color(0xFFCCCC),
      max: am5.color(0xFF0000),
      minValue: 0,
      maxValue: 1324 / 3,
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
    // series.data.setAll([
    //   { Word: "Harry", Count: 1300., legends: "2"},
    //   { Word: "Hermione", Count: 429. , legends: "1"},
    //   { Word: "Dumbeldore", Count: 35 , legends: "1"},
    //   { Word: "looked", Count: 33 , legends: "1"},
    //   { Word: "Proffessor", Count: 31, legends: "1"},
    //   { Word: "Hagrid", Count: 30.5, legends: "1"},
    //   { Word: "time", Count: 30.2, legends: "1"},
    //   { Word: "Snape", Count: 30.1, legends: "1"},
    //   { Word: "eyes", Count: 30.05, legends: "1"},
    //   { Word: "wand", Count: 29.9, legends: "1"},
    //   { Word: "Potter", Count: 29.8, legends: "1"},
    //   { Word: "face", Count: 29.5, legends: "1"},
    //   { Word: "Weasley", Count: 29.5, legends: "1"},
    //   { Word: "voice", Count: 29.5, legends: "1"},
    //   { Word: "again", Count: 29.5, legends: "2"},
    // ]);

    am5.net.load("/data/word_counting.csv").then(function(result) {
      // Parse data
      let data = am5.CSVParser.parse(result.response, {
        delimiter: ",",
        skipEmpty: true,
        useColumnNames: true
      });
      console.log(data);
      series.data.setAll([
        {"Word":"Harry","Count":1324},{"Word":"Ron","Count":429},{"Word":"Hagrid","Count":370},{"Word":"Hermione","Count":269},{"Word":"Professor","Count":179},{"Word":"Snape","Count":171},{"Word":"looked","Count":169},{"Word":"Dumbledore","Count":157},{"Word":"Dudley","Count":139},{"Word":"Malfoy","Count":128},{"Word":"uncle","Count":122},{"Word":"time","Count":120},{"Word":"yeh","Count":117},{"Word":"Neville","Count":117},{"Word":"Vernon","Count":116},{"Word":"Quirrell","Count":113},{"Word":"door","Count":106},{"Word":"eyes","Count":105},{"Word":"McGonagall","Count":100},{"Word":"head","Count":99},{"Word":"people","Count":96},{"Word":"Potter","Count":96},{"Word":"thought","Count":96},{"Word":"told","Count":93},{"Word":"good","Count":91},{"Word":"face","Count":91},{"Word":"room","Count":89},{"Word":"boy","Count":84},{"Word":"left","Count":82},{"Word":"Gryffindor","Count":82},{"Word":"stone","Count":80},{"Word":"ter","Count":78},{"Word":"house","Count":77},{"Word":"turned","Count":77},{"Word":"Hogwarts","Count":76},{"Word":"heard","Count":75},{"Word":"great","Count":72},{"Word":"long","Count":71},{"Word":"suddenly","Count":69},{"Word":"school","Count":69},{"Word":"hand","Count":68},{"Word":"bit","Count":67},{"Word":"aunt","Count":65},{"Word":"knew","Count":64},{"Word":"wand","Count":63},{"Word":"asked","Count":60},{"Word":"yer","Count":60},{"Word":"day","Count":59},{"Word":"voice","Count":59},{"Word":"dark","Count":59},{"Word":"don","Count":59},{"Word":"wood","Count":59},{"Word":"Quidditch","Count":59},{"Word":"cloak","Count":58},{"Word":"open","Count":57},{"Word":"Petunia","Count":57},{"Word":"Dursley","Count":55},{"Word":"black","Count":55},{"Word":"Filch","Count":54},{"Word":"years","Count":52},{"Word":"pulled","Count":52},{"Word":"large","Count":51},{"Word":"feet","Count":51},{"Word":"floor","Count":50},{"Word":"Dursleys","Count":49},{"Word":"mind","Count":49},{"Word":"night","Count":49},{"Word":"started","Count":49},{"Word":"hall","Count":49},{"Word":"felt","Count":49},{"Word":"Slytherin","Count":49},{"Word":"lot","Count":48},{"Word":"moment","Count":48},{"Word":"wizard","Count":48},{"Word":"air","Count":47},{"Word":"magic","Count":47},{"Word":"Weasley","Count":47},{"Word":"wanted","Count":46},{"Word":"mirror","Count":46},{"Word":"fell","Count":46},{"Word":"walked","Count":46},{"Word":"letter","Count":46},{"Word":"high","Count":45},{"Word":"sat","Count":45},{"Word":"bed","Count":45},{"Word":"table","Count":45},{"Word":"called","Count":44},{"Word":"owl","Count":44},{"Word":"points","Count":44},{"Word":"books","Count":43},{"Word":"read","Count":42},{"Word":"hat","Count":40},{"Word":"remember","Count":39},{"Word":"Percy","Count":39},{"Word":"caught","Count":38},{"Word":"hair","Count":38},{"Word":"life","Count":38},{"Word":"man","Count":37},{"Word":"stood","Count":37},{"Word":"Voldemort","Count":37},{"Word":"reached","Count":37},{"Word":"troll","Count":37},{"Word":"wall","Count":36},{"Word":"Madam","Count":36},{"Word":"forest","Count":36},{"Word":"dragon","Count":36},{"Word":"stared","Count":35},{"Word":"whispered","Count":35},{"Word":"father","Count":35},{"Word":"ground","Count":34},{"Word":"place","Count":34},{"Word":"hands","Count":34},{"Word":"coming","Count":34},{"Word":"broom","Count":34},{"Word":"Fred","Count":34},{"Word":"standing","Count":33},{"Word":"white","Count":33},{"Word":"train","Count":33},{"Word":"Peeves","Count":33},{"Word":"small","Count":32},{"Word":"window","Count":32},{"Word":"morning","Count":32},{"Word":"sir","Count":32},{"Word":"silver","Count":32},{"Word":"mother","Count":32},{"Word":"hear","Count":32},{"Word":"nose","Count":31},{"Word":"year","Count":31},{"Word":"red","Count":31},{"Word":"happened","Count":31},{"Word":"minutes","Count":30},{"Word":"suppose","Count":30},{"Word":"hard","Count":30},{"Word":"lost","Count":30},{"Word":"corridor","Count":30},{"Word":"noticed","Count":29},{"Word":"funny","Count":29},{"Word":"shouted","Count":29},{"Word":"stopped","Count":29},{"Word":"family","Count":29},{"Word":"dog","Count":29},{"Word":"green","Count":29},{"Word":"gold","Count":29},{"Word":"talking","Count":29},{"Word":"fer","Count":29},{"Word":"students","Count":29},{"Word":"George","Count":29},{"Word":"team","Count":29},{"Word":"big","Count":28},{"Word":"work","Count":28},{"Word":"trouble","Count":28},{"Word":"light","Count":27},{"Word":"bad","Count":27},{"Word":"Gringotts","Count":27},{"Word":"Flamel","Count":27},{"Word":"broomstick","Count":27},{"Word":"set","Count":26},{"Word":"sitting","Count":26},{"Word":"robes","Count":26},{"Word":"holding","Count":26},{"Word":"sort","Count":26},{"Word":"Norbert","Count":26},{"Word":"corner","Count":25},{"Word":"sight","Count":25},{"Word":"snapped","Count":25},{"Word":"straight","Count":25},{"Word":"heart","Count":25},{"Word":"cold","Count":25},{"Word":"feeling","Count":25},{"Word":"rest","Count":25},{"Word":"Christmas","Count":25},{"Word":"library","Count":25},{"Word":"Granger","Count":25},{"Word":"cat","Count":24},{"Word":"passed","Count":24},{"Word":"dead","Count":24},{"Word":"nice","Count":24},{"Word":"catch","Count":24},{"Word":"week","Count":24},{"Word":"famous","Count":24},{"Word":"giant","Count":24},{"Word":"parents","Count":24},{"Word":"stay","Count":24},{"Word":"match","Count":24},{"Word":"Goyle","Count":24},{"Word":"strange","Count":23},{"Word":"owls","Count":23},{"Word":"finally","Count":23},{"Word":"common","Count":23},{"Word":"staring","Count":23},{"Word":"arms","Count":23},{"Word":"class","Count":23},{"Word":"began","Count":23},{"Word":"shut","Count":23},{"Word":"note","Count":23},{"Word":"book","Count":23},{"Word":"unicorn","Count":23},{"Word":"twins","Count":23},{"Word":"Charlie","Count":23},{"Word":"blood","Count":23}
      ]);

      // books = ['1': {[
      //   { Word: "Harry", Count: 1300.},
      //                { Word: "Harry", Count: 1300.},
      //                { Word: "Harry", Count: 1300.},
      //                { Word: "Harry", Count: 1300.}],
      //                }
      //                ]

      // var book1 = [];
      // for(d in data){
      //   if (d['Book'] == 1){
      //     book1.concat(d);
      //   }
      // }
      // series.data.setAll([data[2]['Count'], data[3], data[4], data[5]]);
      // console.log(book1);
    }).catch(function(result) {
      // This gets executed if there was an error loading URL
      // ... handle error
      console.log("Error loading " + result.xhr.responseURL);
    });

    // console.log(series.data.getIndex(0))

    // var legend = series.children.push(am5.Legend.new(root, {
    //   nameField: "legends",
    //   x: am5.percent(50),
    //   centerX: am5.percent(50),
    //   layout: am5.GridLayout.new(root, {
    //     maxColumns: 4,
    //     fixedWidthGrid: true
    //   })
    // }));
    // legend.data.setAll(series.data.values);

    // var legend = container.children.push(am5.Legend.new(root, {
    //   nameField: "legends",
    //   centerX: am5.percent(50),
    //   x: am5.percent(50),
    // }));
    // legend.data.setAll(series.dataItems);

    }); // end am5.ready()
  }
}
</script>
