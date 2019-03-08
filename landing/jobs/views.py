from flask import jsonify
from landing import app

# json
@app.route("/jobs/")
def jobs_api():
    data = {'job_id': 123, 'tasks': [12, 13,21312, 3121]}
    return jsonify(data)


@app.route("/jobs/<job_id>/")
def jobs(job_id):
    data = {'job_id': job_id, 'tasks': [12, 13,21312, 3121]}
    return jsonify(data)