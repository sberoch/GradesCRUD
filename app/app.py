from flask import Flask, jsonify
import campus_dao as cdao

app = Flask(__name__)

campus = cdao.CampusDAO()

@app.route('/')
@app.route('/courses')
def hello_world():
    return jsonify(campus.get_courses())