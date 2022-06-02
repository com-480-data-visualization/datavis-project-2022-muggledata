<!-- HTML -->
<template>
  <div id="chartdiv">
    <div id="bookselector">
      <form>
        <div class="radio-group">
          <input type="radio" checked id="option-0" name="selector"><label for="option-0">Harry Potter and the Philosophers Stone</label>
          <input type="radio" id="option-1" name="selector"><label for="option-1">Harry Potter and the Chamber of Secrets</label>
          <input type="radio" id="option-2" name="selector"><label for="option-2">Harry Potter and the Prisoner of Azkaban</label>
          <input type="radio" id="option-3" name="selector"><label for="option-3">Harry Potter and the Goblet of Fire</label>
          <input type="radio" id="option-4" name="selector"><label for="option-4">Harry Potter and the Order of the Phoenix</label>
          <input type="radio" id="option-5" name="selector"><label for="option-5">Harry Potter and the Half Blood Prince</label>
          <input type="radio" id="option-6" name="selector"><label for="option-6">Harry Potter and the Deathly Hallows</label>
        </div>
      </form>
    </div>
    <div  id="gramselector">  
      <div class="wrap">
        <div class="RadioBtnsWrap">
          <input type="radio" name="radio1" checked id="radio11" class="Radio" />
          <label for="radio11">1-Gram</label>

          <input type="radio" name="radio1" id="radio12" class="Radio" />
          <label  for="radio12">2-Grams</label>

          <input type="radio" name="radio1" id="radio13" class="Radio" />
          <label  for="radio13">3-Grams</label>
          
          <input type="radio" name="radio1" id="radio14" class="Radio" />
          <label  for="radio14">4-Grams</label>
        </div>
      </div>
    </div>
  </div>
  <div id="spelltextbox">
    <h1 style="text-align: center; color: var(--light_silver); font-family: 'Harry Potter', sans-serif;"> Spell Graph</h1>
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

<!-- Styles -->
<style scoped>
#chartdiv {
  width: 80%;
  height: 1100px;
  margin-right: 20%;
  margin-left: 1%;
  border-radius: 10px;
  background-color: rgb(0, 0, 0, 0.6);
}
#spelltextbox {
  margin-left: 70%;
  color: var(--light_silver);
  margin-top: -1100px;
  height: 1000px;
  z-index: 500;
  background-color: var(--navbar_background);
  padding: 50px;
  margin-right: 50px;
  border-radius: 10px;
  text-align: justify;
  margin-bottom: 100px;
  overflow: scroll;
}
#gramselector {
  margin-right: 30%;
  right: 0px;
  color: var(--light_silver);
  position: absolute;
  z-index: 300;
}
#gramselector body,
html {
  margin: 0;
  height: 100%;
  width: 100%;
  text-align: center;
  display: table;
  font-family: Helvetica;
  color: white;
  font-weight: bold;
}
#gramselector body {
  background: #092756;
  background: -moz-radial-gradient(0% 100%, ellipse cover, rgba(104, 128, 138, 0.4) 10%, rgba(138, 114, 76, 0) 40%), -moz-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%), -moz-linear-gradient(-45deg, #670d10 0%, #092756 100%);
  background: -webkit-radial-gradient(0% 100%, ellipse cover, rgba(104, 128, 138, 0.4) 10%, rgba(138, 114, 76, 0) 40%), -webkit-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%), -webkit-linear-gradient(-45deg, #670d10 0%, #092756 100%);
  background: -o-radial-gradient(0% 100%, ellipse cover, rgba(104, 128, 138, 0.4) 10%, rgba(138, 114, 76, 0) 40%), -o-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%), -o-linear-gradient(-45deg, #670d10 0%, #092756 100%);
  background: -ms-radial-gradient(0% 100%, ellipse cover, rgba(104, 128, 138, 0.4) 10%, rgba(138, 114, 76, 0) 40%), -ms-linear-gradient(top, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%), -ms-linear-gradient(-45deg, #670d10 0%, #092756 100%);
  background: -webkit-radial-gradient(0% 100%, ellipse cover, rgba(104, 128, 138, 0.4) 10%, rgba(138, 114, 76, 0) 40%), linear-gradient(to bottom, rgba(57, 173, 219, 0.25) 0%, rgba(42, 60, 87, 0.4) 100%), linear-gradient(135deg, #670d10 0%, #092756 100%);
}
#gramselector .wrap {
  display: table-cell;
  vertical-align: middle;
}
#gramselector .wrap .RadioBtnsWrap {
  display: inline-block;
  position: relative;
  width: 140px;
}
#gramselector .wrap .RadioBtnsWrap label {
  display: inline-block;
  position: relative;
  margin-left: 40px;
  text-align: left;
  height: 40px;
  line-height: 40px;
  min-width: 100px;
  font-size: 16px;
}
#gramselector .wrap .RadioBtnsWrap label:not(:nth-of-type(1)) {
  margin-top: 17px;
}
#gramselector .wrap .Radio {
  -webkit-appearance: none;
  height: 0;
  width: 0;
  opacity: 0;
  margin: 0;
  padding: 0;
  outline: 0;
  border: none;
}
#gramselector .wrap .RadioBtnsWrap label::after {
  content: "x";
  color: transparent;
  position: absolute;
  left: -44px;
  top: 0;
  bottom: 0;
  margin: auto;
  width: 10px;
  height: 10px;
  background-color: var(--navbar_background);
  display: inline-block;
  border-bottom-left-radius: 40px;
  border-bottom-right-radius: 40px;
  border-top-left-radius: 40px;
  border-top-right-radius: 40px;
  border-color: var(--light_silver);
  border-style: solid;
  border-width: 8px;
  transition: background-color 0.6s, border-width 0.4s, width 0.6s, height 0.6s, left 0.6s;
  -webkit-transition: background-color 0.6s, border-width 0.4s, width 0.6s, height 0.6s, left 0.6s;
  -webkit-box-shadow: 0px 2px 3px -1px rgba(0, 0, 0, 0.75);
  box-shadow: 0px 2px 3px -1px rgba(0, 0, 0, 0.75);
}
#gramselector .wrap .Radio:checked + label::after {
  background-color:#944141;
  width: 20px;
  height: 20px;
  left: -47px;
  border-width: 6px;
  -webkit-box-shadow: 0px 2px 3px -1px rgba(0, 0, 0, 0.75), inset 0px 0px 5px 1px rgba(0, 0, 0, 0.75);
  box-shadow: 0px 2px 3px -1px rgba(0, 0, 0, 0.75), inset 0px 0px 5px 1px rgba(0, 0, 0, 0.75);
}
#gramselector .wrap .RadioBtnsWrap label:not(:nth-of-type(1))::before {
  content: "";
  position: absolute;
  left: -35px;
  height: 57px;
  width: 8px;
  display: inline-block;
  background-color: var(--light_silver);
  -webkit-box-shadow: 1px 4px 2px 1px rgba(0, 0, 0, 0.25);
  box-shadow: 1px 4px 2px 1px rgba(0, 0, 0, 0.25);
  z-index: -1;
}
#gramselector .wrap .RadioBtnsWrap label::before {
  bottom: 28px;
}
#gramselector .wrap .Radio:checked + label + input + label::before {
  height: 52px;
  transition: height 0s linear 0.3s;
  -webkit-transition: height 0s linear 0.3s;
}
#bookselector {
  position: absolute;
  width: 55%;
  z-index: 300;
}
#bookselector body {
  background: #332f35;
}

#bookselector input[type=radio] {
  position: absolute;
  visibility: hidden;
  display: none;
}

#bookselector label {
  color: var(--light_silver);
  display: table-cell;
  cursor: pointer;
  font-weight: bold;
  padding: 5px 20px;
  background: var(--navbar_background);
}

#bookselector input[type=radio]:checked + label {
  color: var(--light_silver);
  background: #675f6b;
}

#bookselector label + input[type=radio] + label {
  border-left: solid 3px #675f6b;

}

#bookselector .radio-group {
  border: solid 3px #675f6b;
  display: inline-block;
  margin: 20px;
  border-radius: 10px;
  overflow: hidden;
  font-size: 12px;
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

      // add listener on each option
      switchStates.forEach(x => {
        document.getElementById("radio1"+x.toString()).addEventListener('change', function () {
            switchState = x;
            am5.net.load("./data/"+switchState.toString()+"_gram/"+switchState.toString()+"_gram_words_specific_book" + (book_state + 1) + ".json").then(function(result) {
              series.data.setAll(am5.JSONParser.parse(result.response));
            }).catch(function(result) {
              // This gets executed if there was an error loading URL
              // ... handle error
              console.log("Error loading " + result.xhr.responseURL);
            })
          })
      })
      

      var book_state = 0

      for (let book_id = 0; book_id < 7; book_id++) {
        document.getElementById("option-"+book_id.toString()).addEventListener('change', function () {
            book_state = book_id;
            am5.net.load("./data/"+switchState.toString()+"_gram/"+switchState.toString()+"_gram_words_specific_book" + (book_state + 1) + ".json").then(function(result) {
              series.data.setAll(am5.JSONParser.parse(result.response));
            }).catch(function(result) {
              // This gets executed if there was an error loading URL
              // ... handle error
              console.log("Error loading " + result.xhr.responseURL);
            })
          })
      }

      
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
