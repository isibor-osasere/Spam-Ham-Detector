from flask import Flask, render_template, request
import sklearn, joblib

app = Flask(__name__)

messages = []

#loading our model
model_0 = joblib.load('spam_ham_naive_bayes.pkl')

@app.route ("/")
def home ():
    return render_template ("index.html")

@app.route("/submit", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        message = request.form.get("message")
        prediction = model_0.predict ([message])[0]
            
            
    return render_template("index.html", prediction = prediction)

if __name__ == "__main__":
    app.run(debug=True)

        
        

