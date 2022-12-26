//List of enrolled courses
var course_list = [];

//fetch courses from feedback
function fetch_courses(course) {
    course_list = course;
}

//Store selected course
var course_selected = 'N/A';

//!!! CALL to DB at before page loads
document.addEventListener("DOMContentLoaded", populate_dropdown

);

//Populate dropdown
function populate_dropdown() {
    for (const i in course_list) {

        var course = course_list[i];//course in list

        //new option to be added
        var new_option = "<option value='" + course + "' id='" + course + "' onclick='update_course()')>" + course + "</option>";

        //Add option into dropdown
        $("#dropdown").append(new_option);
    }
}

//update course_selected variable
function update_course() {
    //get the drop down 
    const dropdown = document.getElementById("dropdown");
    value = dropdown.value;//value is the value of dropdown selected

    if (value != "") {
        //update course_selected
        course_selected = value;
        console.log(course_selected);
    }
}

