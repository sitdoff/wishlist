from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """
    Main page of the application
    """
    return render_template("index.html")
