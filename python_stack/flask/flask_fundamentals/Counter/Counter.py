from flask import Flask,render_template,request,redirect,session
app=Flask(__name__)
app.secret_key="Keep it a secret"


#Adding the counter and adding the actual counter
@app.route("/")
def showIndex():
    if "counter" not in session:
        session["counter"]=0
    else:
        session["counter"]+=1

    if "actual_counter" not in session:
        session["actual_counter"]=0
    else:
        session["actual_counter"]+=1

    print(session)
    return render_template("index.html",counter=session["counter"],actual_counter=session["actual_counter"])


#Destroying the session
@app.route("/destroy_session",methods=["POST","GET"])
def destroySession():
    session.pop("counter")
    print(session)
    return redirect("/")


#Secret method to destroy both the counter and actual counter 
@app.route("/destroy_all")
def destroy_all():
    session.clear()
    return redirect("/")


#Increment By 2
@app.route("/incrementByTwo",methods=["POST"])
def incrementByTwo():
    session["counter"]+=1 #Because the "/" will already add 1 when we are redirected there
    return redirect("/")


#Increment by whatever value the user wants
@app.route("/customizedIncrement",methods=["POST"])
def customizedIncrement():
    session["counter"]+=int(request.form["number"])-1  #Because the "/" will already add 1 when we are redirected there
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)
