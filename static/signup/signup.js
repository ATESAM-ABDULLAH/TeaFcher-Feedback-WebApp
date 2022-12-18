// Makes extra inputs availaible as per user
function show_extra(x) {
    if (x == "student") {

        document.getElementById("ch-regno").style.display = "block";
        document.getElementById("ch-course").style.display = "none";
    }
    else if (x == "teacher") {
        document.getElementById("ch-course").style.display = "block";
        document.getElementById("ch-regno").style.display = "none";
    }
    else {
        document.getElementById("ch-regno").style.display = "none";
        document.getElementById("ch-course").style.display = "none";
    }
    console.log(x);
}


//check password validity
var check_pass = function () {
    if (document.getElementById('password').value == document.getElementById('con-password').value) {
        document.getElementById('message').style.color = 'green';
        document.getElementById('message').innerHTML = 'OK';
        document.getElementById('submit').disabled = false;
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = 'XX';
        document.getElementById('submit').disabled = true;
    }
    console.log("x");
}

