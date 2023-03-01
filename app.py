from flask import Flask, render_template, jsonify
from database import load_from_db

app = Flask(__name__)

@app.route("/")
def hello_jovian():
    global jobs_list
    jobs_list = load_from_db()
    return render_template('home.html', jobs=jobs_list, company_name='Jovian')


@app.route("/api/jobs")
def list_jobs():
    return jsonify(jobs_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
