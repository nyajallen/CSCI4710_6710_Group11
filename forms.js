include("results.js");


function calculateSum() {
  var sum = 0;
  var name = document.getElementById("inputName").value;
  var shadowInput = document.getElementById("inputShadow").value;
  var garlicInput = document.getElementById("inputGarlic").value;
  var paleInput = document.getElementById("inputPale").value;
  var yes = /yes/i;
  var no = /no/i;

  if(shadowInput == shadowInput.match(no)){
    sum += 4;
  }

  if(garlicInput == garlicInput.match(yes)){
    sum +=3;
  }

  if(paleInput == paleInput.match(yes)) {
    sum +=3;
  }

  if (typeof(Storage) !== "undefined") {
    // Store
    sessionStorage.setItem("Sum", sum);
    sessionStorage.setItem("Name", name);
  }

  window.location.href = "results_page.html";

}
