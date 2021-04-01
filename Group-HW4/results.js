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

// Use JSON Data for example Classmates
var classmates = {
         "students": [
             {
                 "name": "Emily Jane",
                 "method": "JSON Data",
                 "isVampire": "No"

             },
             {
							 "name": "Brice Williams",
							 "method": "JSON Data",
							 "isVampire": "Yes"
             },
             {
							 "name": "Peter McCallister",
							 "method": "JSON Data",
							 "isVampire": "Yes"
             }
         ]
}

// Add sample JSON data to table
function loadJSONData() {
	var name;
	var method;
	for (i in classmates.students) {
	        if(classmates["students"][i]["isVampire"] == "Yes"){
	          vampires ++;
						isVampire = true;
						addToChart();
						name = classmates["students"][i]["name"];
						method = classmates["students"][i]["method"];
						createTableRow(name , method);

	        }
	        else{
	          humans ++;
						isVampire =false;
						addToChart();
						name = classmates["students"][i]["name"];
						method = classmates["students"][i]["method"];
						createTableRow(name, method);
	        }
	}
}

// called for threshold results
function showResults(){

	var sum = sessionStorage.getItem("Sum");
	var name = sessionStorage.getItem("Name");

	if(sum > 6){
		document.getElementById("replace").innerHTML="A Vampire!";
		document.getElementById("result_image").src="src/vampire.png";
		isVampire =true;
		vampires +=1;
		addToChart();
		createTableRow(name, "Threshold");
	} else if(sum === null) {
    window.alert("Must fill out form");
  } else {
		document.getElementById("replace").innerHTML="Not A Vampire!";
		document.getElementById("result_image").src="src/human.jpg";
		isVampire = false;
		humans +=1;
		addToChart();
		createTableRow(name, "Threshold");
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
	document.getElementById("replace").
		innerHTML="------------------------------";
	document.getElementById("result_image").src="src/question_mark.jpeg";


	div.appendChild(ask);
	div.appendChild(input);
	div.appendChild(enter);

	enter.addEventListener("click", getRandom);
}

// gets random decision
function getRandom() {
	var num = getRandomInt(21);
	var name = document.getElementById("name").value;
	document.getElementById("ask").remove();
	document.getElementById("name").remove();
	document.getElementById("enter").remove();

	if(num % 2 != 0){
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
	humans = 0;
	vampires =0;
	addToChart();

	while(table.rows.length > 1) {
		table.deleteRow(table.rows.length - 1)
	}
}
