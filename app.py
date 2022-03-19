from flask import Flask, request, render_template
import joblib

app = Flask(__name__) #__xx__

#which directory is file in
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST": #when user press 'Enter' in front end
        rates = request.form.get("rates")
        print(rates)
        model = joblib.load('DBS_regression')
        pred = model.predict([[float(rates)]])
        print(pred)
        s = "Predicted DBS Share Price : " + str(pred[0][0])
        print(s)
        return(render_template("index.html", results=s))

    else: #before user press 'Enter' in front end
        return(render_template("index.html", results="DBS Share Price Prediction"))


if __name__ == "__main__": #need this to run in cloud environment, to verify that code is mine
    app.run()
    

