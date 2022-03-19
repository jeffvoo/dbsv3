from flask import Flask
app=Flask(__name__)

from flask import request, render_template
import joblib

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates=request.form.get("rates")
        print(rates)
        model = joblib.load('DBS_regression')
        pred = model.predict([[float(rates)]])
        print(pred)
        s = "Predicted DBS Share Price: " + str(pred)
        print(s)
        return(render_template("index.html", results=s))

    else:
        return(render_template("index.html", results="DBS Share Price Prediction"))


if __name__=="__main__":
    app.run()
    

