from flask import Flask,render_template
app=Flask(__name__)

# @app.route("/play")
# def Level1():
#     return render_template("play.html")

@app.route("/play")
@app.route("/play/<int:num>")
@app.route("/play/<int:num>/<color>")
def allLevels(num=3,color="#9fc5f8"):
    return render_template("play.html",NUM=num,COLOR=color)

if __name__=="__main__":
    app.run(debug=True)