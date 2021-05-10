from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
@app.route("/<int:x>/<int:y>")
@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def checker(x=8,y=8,color1="black",color2="red"):
    return render_template("index.html",X=x,Y=y,color1=color1,color2=color2)


@app.route("/4")
def checker2():
    return render_template("index.html",X=8,Y=4,color1="red",color2="black")


if __name__=="__main__":
    app.run(debug=True)
    