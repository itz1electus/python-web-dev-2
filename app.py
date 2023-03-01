from flask import Flask, render_template, jsonify
from database import load_from_db, load_job_info_from_db

app = Flask(__name__)


@app.route("/")
def hello_jovian():
    global jobs_list
    jobs_list = load_from_db()
    return render_template('home.html', jobs=jobs_list)


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs_list)


@app.route("/jobs/<id>")
def job_info_page(id):
    job_info = load_job_info_from_db(id)
    if not job_info:
        return "Error Not Found", 404
    return render_template('jobinfo.html', job=job_info)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
