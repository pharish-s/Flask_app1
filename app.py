from flask import Flask,render_template, request,flash
# from sympy import refine

app = Flask(__name__)
app.secret_key="123456789"

@app.route("/")
def index():
    flash("Enter your input")
    return render_template("index.html")
    # return "Congratulations, it's a web app!"

@app.route("/input", methods=["POST","GET"])
def input_data():
    flash("Hi "+ str(request.form['name_input']))
    # print(str(request.form['input']))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)