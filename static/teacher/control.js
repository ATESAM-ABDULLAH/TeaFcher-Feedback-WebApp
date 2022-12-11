// get data from DB
var name = "";
var course = "";

//empty list to store all students
var list_students = [];

////reset t_students=0 when page loads -> cookies often store old value
document.addEventListener("DOMContentLoaded", () => { $('#t_students').val(1) });

//add a student input field on click of button
function add() {

    //increase + store and read count from t_students
    var count = parseInt($('#t_students').val()) + 1;

    if (count < 51)//max student per course = 50
    {
        console.log(count);//works

        //new html item
        var new_input =
            "<li id='grp-" + count + "'>\
            <label for='std-" + count + "' id='label-" + count + "'>\
            Reg #\
            </label>\
            <input type='number' name='std-" + count + "' id='std-" + count + "' min='2019000'\
             max='2022999' placeholder='2021197'>\
        </li> ";

        //Append item to list
        $("#list-std").append(new_input);

        //feed new count back into #t_students
        $('#t_students').val(count);
    }

}

//remove a student input field on click of button   
function remove() {

    var count = parseInt($('#t_students').val());

    if (count > 1)//atleast 1 student always exists
    {
        console.log("-" + count);//works

        //remove element 
        $("#grp-" + count + "").remove();

        //decrease and store count back in t_students
        $('#t_students').val(count - 1);
    }
}

//Create a list of students and post to database
function sendData() {

    //size of students list in html
    var size = parseInt($('#t_students').val());
    console.log("Size: " + size);

    //copy data from inputs to our list
    for (let i = 1; i <= size; i++) {
        var student = $("#std-" + i + "").val();
        list_students.push(student);//push into list
    }

    ////print list
    for (let i = 0; i < size; i++) {
        console.log(list_students[i]);
    }
}