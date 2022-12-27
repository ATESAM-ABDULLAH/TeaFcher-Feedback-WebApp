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


//MAIN function for calling data + making graph
function callChart(graph_data) {

    if (course_selected != '') {

        const ctx = document.getElementById('graph');

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Rating'],
                datasets: [{
                    label: 'Questions (1-5)',
                    data: graph_data,
                    borderWidth: 2
                }
                ]
            },
            options: {
                scales: {
                    x: {
                        ticks: {
                            color: "white",
                            font: {
                                size: 16
                            }
                        },
                        grid: {
                            display: false
                        }
                    },
                    y: {
                        ticks: {
                            color: "white",
                            font: {
                                size: 16
                            }
                        },
                        grid: {
                            display: true,
                            color: '#fff'
                        },
                        beginAtZero: true
                    }
                }
            }

        });


    }
    console.log('nothing selected');
}

//function to reset graph and course data
function reset_data() {
    //erase course data
    document.getElementById("teacher").innerHTML = "____";
    document.getElementById("course").innerHTML = "____";
    //erase previous graph if any
    document.getElementById("graph").innerHTML = "";
}