from flask import Flask,render_template,request,redirect
from datetime import date
TODAY=date.today()
app=Flask(__name__)

@app.route("/")
def function1():
    return render_template("index.html")


@app.route("/checkout",methods=["POST"])
def function2():
    first_name=request.form["first_name"]
    last_name=request.form["last_name"]
    student_id=request.form["student_id"]
    strawberry=request.form["strawberry"]
    raspberry=request.form["raspberry"]
    apple=request.form["apple"]
    sum=int(strawberry)+int(raspberry)+int(apple)
    return render_template("checkout.html",first_name=first_name,last_name=last_name,student_id=student_id,strawberry=int(strawberry),raspberry=int(raspberry),apple=int(apple),sum=sum,TODAY=TODAY)


@app.route("/Fruits.html")
def function3():
    return render_template("Fruits.html")

if __name__=="__main__":
    app.run(debug=True)