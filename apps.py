from flask import Flask, redirect, url_for, render_template
from datetime import datetime
app = Flask(__name__)
@app.route("/")
def home():
    
    return render_template("tindex.html",content=["sana","jiya"],user="jay",date=datetime.now().strftime("%Y-%m-%d"))


if __name__== "__main__":
    app.run(debug=True)