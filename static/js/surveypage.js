//change page function to change the page
//PARAMETER: url
function changePage(url) {
  //open url with window.open command
    window.open(url, "_self");
  }
  //change page after set period of time function
  function changePageAfter5sec(url) {
    setTimeout(function() {
        //call change page function after time interval of 5000
      changePage(url)
    }, 2500);
  }

const survey = new Survey.Model(json);
survey.onComplete.add((sender, options) => {
    console.log(JSON.stringify(sender.data, null, 3));
    //switch html to the index with the change page function
    changePageAfter5sec("../pages/home.html")

});

$("#surveyElement").Survey({ model: survey });