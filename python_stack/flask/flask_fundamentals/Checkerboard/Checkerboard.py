from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
@app.route("/<int:x>/<int:y>/")
@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def checker(x=8,y=8,color1="black",color2="red"):
    return render_template("index.html",x=x,y=y,color1=color1,color2=color2)

@app.route("/<int:z>")
def checker2(z):
    return render_template("index.html",x=8,y=z,color1="black",color2="red")

if __name__=="__main__":
    app.run(debug=True)