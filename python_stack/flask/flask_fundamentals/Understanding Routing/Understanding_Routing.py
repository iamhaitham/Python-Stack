from flask import Flask 
app=Flask(__name__)

@app.route("/")
def greetings():
    return "Hello World"

@app.route("/dojo")
def dojo():
    return "Dojo"

@app.route("/say/<var>")
def say(var):
    return "Hi {}".format(var)

@app.route("/repeat/<number>/<word>")
def repeat(number,word):
    return f"{word}"*int(number)

#NINJA BONUS
@app.route("/repeat2/<int:number>/<word>")
def repeat2(number,word):
    return f"{word}"*number

#SENSEI BONUS
@app.route("/<other>")
def other(other):
    return "Sorry! No response. Try again"

if __name__=="__main__":
    app.run(debug=True)