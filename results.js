// global variable
var isVampire = true;

// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

var chart;
var data;
var options;
var humans = 0;
var vampires = 0;

// called for threshold results
function showResults(sum){
	
	var div = document.getElementById("namespace");

	if(sum > 6){
		document.getElementById("replace").innerHTML="A Vampire!";
		document.getElementById("result_image").src="src/vampire.png";
		isVampire =true;
		vampires +=1;
		addToChart();
		createTableRow();
	}
	else {
		document.getElementById("replace").innerHTML="Not A Vampire!";
		document.getElementById("result_image").src="src/human.jpg";
		isVampire = false;
		human +=1;
		addToChart();
		createTableRow();
	}
}

//called for random results
function randomGuess() {
	var div = document.getElementById("namespace");
	var ask = document.createElement("p");
	var input = document.createElement("input");
	var enter = document.createElement("button");
	ask.innerText = "Enter Classmate's Name: ";
	enter.innerText = "Enter";
	ask.setAttribute("id", "ask");
	input.setAttribute("id", "name");
	enter.setAttribute("id", "enter");

	
	div.appendChild(ask);
	div.appendChild(input);
	div.appendChild(enter);
	
	enter.addEventListener("click", getRandom);
}

// gets random decision
function getRandom() {
	var num = getRandomInt(6);
	var name = document.getElementById("name").value;
	document.getElementById("ask").remove();
	document.getElementById("name").remove();
	document.getElementById("enter").remove();
	
	if(num >= 4){
		document.getElementById("replace").innerHTML="A Vampire!";
		document.getElementById("result_image").src="src/vampire.png";
		isVampire = true;
		vampires +=1;
		addToChart();
		createTableRow(name, "Random");
	}
	else {
		document.getElementById("replace").innerHTML="Not A Vampire!";
		document.getElementById("result_image").src="src/human.jpg";
		isVampire = false;
		humans +=1;
		addToChart();
		createTableRow(name, "Random");
	}

}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

// creates a row in the table
function createTableRow(name, method) {
	var table = document.getElementById("vampire_table");
	var row_count = table.rows.length;
	var row = table.insertRow(row_count);
	var cell1 = row.insertCell(0);
	var cell2 = row.insertCell(1);
	var cell3 = row.insertCell(2);
	
	cell1.innerText = name;
	cell2.innerText = method;
	
	if(isVampire == true){
		cell3.innerHTML = "<img src='src/vampire_icon.jpg' width = '30' />";	
	}
	else {
		cell3.innerHTML = "<img src='src/human.jpg' width='30'/>";
	}
}

// Creates pie chart
function drawChart() {

    // Create the data table.
    data = new google.visualization.DataTable();
    data.addColumn('string', 'Element');
    data.addColumn('number', 'Number');
    data.addRows([
        ['Human', humans],
        ['Vampire', vampires]
    ]);

    // Set chart options
    options = {'title':'How many vampires in the class?',
                    'width':400,
                    'height':300};

    // Instantiate and draw our chart, passing in some options.
    chart = new google.visualization.PieChart(document.getElementById('pie_chart'));
    chart.draw(data, options);
}

function addToChart() {
	data.removeRow(1);
    data.removeRow(0);
    data.insertRows(0, [['Human', humans]]);
    data.insertRows(1, [['Vampire', vampires]]);
    chart.draw(data, options);
}

// resets page
function reset(){
	document.getElementById("replace").
		innerHTML="------------------------------";
	document.getElementById("result_image").src="src/question_mark.jpeg";
	var table = document.getElementById("vampire_table");
	var row_count = table.rows.length;
	table.deleteRow(row_count-1);

	if(isVampire == true) {
		vampires -= 1;
		addToChart();
	}
	else {
		humans -= 1;
		addToChart();
	}	
}