from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/version/download")
def download():
    return send_from_directory("static","a.py", as_attachment = True)

@app.route("/api/version")
def versionControl():
    return version

@app.errorhandler(404)
def pageNotFound(error):
    return error, 404

if __name__ == "__main__":

    version = "5.0.0"

    app.run(debug="on")