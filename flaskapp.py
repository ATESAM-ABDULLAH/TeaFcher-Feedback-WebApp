from flask import Flask , render_template , url_for , request 

# main app 
app=Flask(__name__)

# Routes to diff pages
@app.route("/",methods=["GET","POST"])
@app.route("/login",methods=["GET","POST"])
def login():
    print(request.form)
    return render_template('./login/login.html')

@app.route("/signup",methods=["GET","POST"])
def signup():
    print(request.form)
    return render_template('./signup/signup.html')

@app.route("/student",methods=["GET","POST"])
def student():
    print(request.form)
    return render_template('./student/feedback.html')

@app.route("/faculty",methods=["GET","POST"])
def teacher():
    print(request.form)
    return render_template('./teacher/control.html')

@app.route("/admin",methods=["GET","POST"])
def faculty():
    print(request.form)
    return render_template('./adminstrator/view.html')

# Run using python instead of flask
if(__name__ == '__main__'):
    app.run(debug=True)