//Get list from DB
var course_list = ['CS 232', 'CS 101', 'MT 201', 'ES 101', 'CE 112'];

course_l=document.getElementById('script_data').innerHTML;

console.log(course_l);

//Store selected course
var course_selected = 'N/A';


//!!! CALL to DB at before page loads
document.addEventListener("DOMContentLoaded", populate_dropdown

);

//Populate dropdown
function populate_dropdown() {
    for (const i in course_list) {

        var course = course_list[i];//course in list

        //console.log(course);//work

        //new option to be added
        var new_option = "<option value='" + course + "' id='" + course + "')>" + course + "</option>";

        //Add option into dropdown
        $("#dropdown").append(new_option);
    }
}

//temporary -> graph data
var graph_data = {
    header: ["Question #", "Avg answer"],
    rows: [
        // get data from function random_data()
    ]
};

//temporary -> create random values for graph_data
function random_data(obj)//
{
    for (let i = 0; i < 12; i++) {
        var randint = Math.random() * 5;
        // console.log(randint);

        // 10 normal questions 0-9 
        if (i < 11) {
            obj.rows.push(["q" + (i + 1) + "", randint]);
        }

        //Teacher rating question 10
        if (i == 11) {
            obj.rows.push(["Teacher Rating", randint]);
        }

        console.log(obj.rows[i]);
    }

    return obj;
};

// Create graph
function make_chart(DB_data) {

    // get data -> used DB in future
    var data = DB_data;

    // declare chart type
    var chart = anychart.column();

    // add the data
    chart.data(data);

    //div id for graaph
    chart.container("graph-container");

    //draw chart
    chart.draw();


    //Axis labels
    chart.xAxis().title("Questions");
    chart.yAxis().title("Avg Score");

    //set Y-Axis max values
    chart.yScale().maximum(5);

    //enable labels
    var labels = chart.labels();

    labels.enabled(true);
    labels.fontColor('#F44336');
    labels.fontSize(12);
    labels.fontWeight(600);

    //enable grid
    chart.yGrid().enabled(true);
    chart.yMinorGrid().enabled(true);

    //enable animation
    chart.animation(true);
};



//MAIN function for calling data + making graph
function callChart() {

    //get the drop down 
    const dropdown = document.getElementById("dropdown");
    value = dropdown.value;//value is the value of dropdown selected


    if (value != "")//if an option is selected
    {
        //update course_selected
        course_selected = value;

        // course data 
        document.getElementById("teacher").innerHTML = "DB data";//get data from db here
        document.getElementById("course").innerHTML = course_selected;

        //erase previous graph if any
        document.getElementById("graph-container").innerHTML = "";

        // Call data from database here
        var data = random_data(graph_data);//currently random data

        //create chart
        make_chart(data);
    }
}

//function to reset graph and course data
function reset_data() {
    //erase course data
    document.getElementById("teacher").innerHTML = "____";
    document.getElementById("course").innerHTML = "____";
    //erase previous graph if any
    document.getElementById("graph-container").innerHTML = "";
}