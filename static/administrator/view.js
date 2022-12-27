//Store list of distinct courses
var course_list = [];
//Get list from DB>Python>HTML
function fetch_courses(course) {
    course_list = course;
}


var course_selected = '';
function update_course_selected(course) {
    console.log('updating course')
    course_selected = course;
}


//!!! CALL to DB at before page loads
document.addEventListener("DOMContentLoaded", populate_dropdown

);

//Populate dropdown
function populate_dropdown() {
    for (const i in course_list) {

        var course = course_list[i];//course in list

        //new option to be added
        var new_option = "<option value='" + course + "' id='" + course + "')>" + course + "</option>";

        //Add option into dropdown
        $("#dropdown").append(new_option);
    }
}

//Graph data - template
var graph_data = {
    header: ["Question #", "Avg answer"],
    rows: [
        //Add course avergae data here
    ]
};

//Update graph_data using received list
function update_graph_data(avg_list) {
    graph_data.rows.push(['Q1'], avg_list[0]);
    graph_data.rows.push(['Q2'], avg_list[1]);
    graph_data.rows.push(['Q3'], avg_list[2]);
    graph_data.rows.push(['Q4'], avg_list[3]);
    graph_data.rows.push(['Q5'], avg_list[4]);
    graph_data.rows.push(['Q6'], avg_list[5]);
    graph_data.rows.push(['Q7'], avg_list[6]);
    graph_data.rows.push(['Q8'], avg_list[7]);
    graph_data.rows.push(['Q9'], avg_list[8]);
    graph_data.rows.push(['Q10'], avg_list[9]);
    graph_data.rows.push(['Q11'], avg_list[10]);
    graph_data.rows.push(['Rating'], avg_list[11]);

};

// Create graph
function make_chart(DB_data) {

    console.log('Making graph')

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

    if (course_selected != '') {
        make_chart(graph_data)
    }
    console.log('nothing selected')
}

//function to reset graph and course data
function reset_data() {
    //erase course data
    document.getElementById("teacher").innerHTML = "____";
    document.getElementById("course").innerHTML = "____";
    //erase previous graph if any
    document.getElementById("graph-container").innerHTML = "";
}