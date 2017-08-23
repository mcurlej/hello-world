from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome!"

@app.route("/clanky")
def zoznam():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/search")
def search():
    return render_template("search.html")

if __name__== "__main__":
    app.run()
