from flask import Flask, render_template, request
import os

from resume_analyze import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")



@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:

        return "No Resume Uploaded"

    resume = request.files["resume"]

    if resume.filename == "":

        return "Please Select a Resume"

    filepath = os.path.join(

        app.config["UPLOAD_FOLDER"],

        resume.filename

    )

    resume.save(filepath)

    result = analyze_resume(filepath)

    return render_template(

        "result.html",

        result=result,

        resume_text=result["resume_text"]

    )



@app.route("/dashboard")
def dashboard():

    return render_template("dashboard.html")




@app.route("/about")
def about():

    return render_template("about.html")




@app.route("/contact")
def contact():

    return render_template("contact.html")




if __name__ == "__main__":

    app.run(debug=True)