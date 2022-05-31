<!-- HTML -->
<template>
<div>
  <div id="switchbtn"></div>
  <div id="chartdiv"></div>
</div>
  
</template>

<!-- Styles -->
<style>
#chartdiv {
  width: 80%;
  height: 1100px;
  margin-right: 20%;
  margin-left: 0;
}
#switchbtn {
  width: 20%;
  float: right;
  padding: 2.5em 0em;
  text-align: center;
  color: white;
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
        height: am5.percent(100),
        //layout: root.verticalLayout,
        layout: root.verticalLayout
      }));

      var container_cloud = root.container.children.push(am5.Container.new(root, {
        width: am5.percent(80),
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


      /**
       * TODO 
       * 
       */
      // let slider = container_cloud.children.push(am5.Slider.new(root, {
      //   orientation: "horizontal",
      //   start: 0,
      //   width: am5.percent(20),
      //   centerY: am5.p50,
      //   centerX: am5.p50,
      //   x: am5.percent(15),
      // }))

      // slider.events.on("rangechanged", function() {
      //   var sliderPosition = slider.get("start");
      //   console.log(sliderPosition)
      // })
      var switchState = 1;
      const switchStates = [1, 2, 3, 4]
      const group = document.querySelector("#switchbtn");
      group.innerHTML = switchStates
          .map(
            (state) => `<div>
                          <input type="radio" name="state" value="${state}">
                          <switchbtn for="${state}">${state}-gram words</label>
                        </div>`
          )
          .join(' ');
      const switchbtns = document.querySelectorAll('input[name="state"]');
      for(const switchbtn of switchbtns){
          switchbtn.addEventListener('change', function () {
            switchState = this.value;
            am5.net.load("./data/"+this.value.toString()+"_gram/"+this.value.toString()+"_gram_words_specific_book" + (book_state + 1) + ".json").then(function(result) {
              series.data.setAll(am5.JSONParser.parse(result.response));
            }).catch(function(result) {
              // This gets executed if there was an error loading URL
              // ... handle error
              console.log("Error loading " + result.xhr.responseURL);
            })
          });
      }


      var book_state = 0
      function buttons(book_nb) {
        let button = container.children.push(am5.Button.new(root, {
          label: am5.Label.new(root, {
            text: books_name[book_nb],
            textAlign: "center",
            marginLeft: -10,
            marginRight: -10,
            fontSize: 12,
            width: 150
          }),
          y: 50,
        }));
        button.set("x",  button.get("label").get("width") * book_nb)
        button.set("width", button.get("label").get("width"))
        button.get("background").setAll({
          fill: am5.color(0xFFCCCC - book_nb * 0x002222),
          fillOpacity: 0.6,
        })
        button.get("background").states.create("hover", {}).setAll({
          fill: button.get("background").get("fill"),
          fillOpacity: 0.8,
        });
        button.get("background").states.create("active", {}).setAll({
          fill: button.get("background").get("fill"),
          fillOpacity: 1.,
        });
        // if (button.isHover()) {
        //   button.get("background").setAll({
        //     fill: am5.color(0xffff0f),
        //     fillOpacity: 1.,
        //   })
        button.events.on("click", function() {
          book_state = book_nb
          am5.net.load("./data/"+switchState.toString()+"_gram/"+switchState.toString()+"_gram_words_specific_book" + (book_nb + 1) + ".json").then(function(result) {
            series.data.setAll(am5.JSONParser.parse(result.response));
          }).catch(function(result) {
            // This gets executed if there was an error loading URL
            // ... handle error
            console.log("Error loading " + result.xhr.responseURL);
          });
        });
        return button;
      }

      let books_name = ["Harry Potter and \n the Philosophers Stone",
                        "Harry Potter and \n the Chamber of Secrets",
                        "Harry Potter and \n the Prisoner of Azkaban",
                        "Harry Potter and \n the Goblet of Fire",
                        "Harry Potter and \n the Order of the Phoenix",
                        "Harry Potter and \n the Half Blood Prince",
                        "Harry Potter and \n the Deathly Hallows"];
      buttons(0);
      buttons(1);
      buttons(2);
      buttons(3);
      buttons(4);
      buttons(5);
      buttons(6);
      
      // Add series
      // https://www.amcharts.com/docs/v5/charts/word-cloud/
      var series = container_cloud.children.push(am5wc.WordCloud.new(root, {
        categoryField: "Words",
        valueField: "Count",
        calculateAggregates: true, // this is needed for heat rules to work
        legendLabelText: "legends",
        minFontSize: 15,
        maxFontSize: 50 - 5 * switchState,
        angles: 0
      }));

      series.animate

      am5.net.load("./data/1_gram/1_gram_words_specific_book1.json").then(function(result) {
            series.data.setAll(am5.JSONParser.parse(result.response));
      }).catch(function(result) {
        // This gets executed if there was an error loading URL
        // ... handle error
        console.log("Error loading " + result.xhr.responseURL);
      });

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
        cursorOverStyle: "pointer",
        tooltipText: "'{category}' appear {value} time in the book",
        tooltipPosition: "pointer"
      });


      // Add click event on words
      // https://www.amcharts.com/docs/v5/charts/word-cloud/#Events
      series.labels.template.events.on("click", function(ev) {
        const category = ev.target.dataItem.get("category");
        window.open("https://fr.wikipedia.org/wiki/" + encodeURIComponent(category));
      });
      // series.labels.template.events.on("hover", function(ev) {
      //   const value = ev.target.dataItem.get("value");
      //   window;
      // });

      }); // end am5.ready()
    }
  }
</script>
