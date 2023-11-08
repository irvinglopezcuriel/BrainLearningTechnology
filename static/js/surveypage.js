//change page function to change the page
function changePage(url) {
    window.open(url, "_self");
  }
  //change page after set period of time function
  function changePageAfter5sec(url) {
    setTimeout(function() {
        //call change page function
      changePage(url)
    }, 5000);
  }
  
const survey = new Survey.Model(json);
survey.onComplete.add((sender, options) => {
    console.log(JSON.stringify(sender.data, null, 3));
    //switch html to the index
    changePageAfter5sec("file:///C:/Users/jrami/OneDrive/Desktop/Github/370repo/BrainLearningTechnology/static/pages/index.html")

});

$("#surveyElement").Survey({ model: survey });