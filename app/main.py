from flask import Flask, jsonify, request
from flask_cors import CORS
from http import HTTPStatus
import campus_dao as cdao

app = Flask(__name__)
CORS(app)

campus = cdao.CampusDAO()

@app.route('/')
@app.route('/courses')
def get_courses():
    return jsonify(campus.get_courses()), HTTPStatus.OK


@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
	course = campus.get_course(course_id)
	if course:
		return jsonify(course), HTTPStatus.OK
	else:
		return f"Course not found", HTTPStatus.NOT_FOUND


@app.route('/courses/<int:course_id>/grades', methods=['GET'])
def get_grades(course_id):
	return jsonify(campus.get_grades(course_id)), HTTPStatus.OK


@app.route('/courses', methods=['POST'])
def insert_course():
	course = request.get_json()
	inserted = campus.insert_course(course)
	if inserted:
		return f"Course created.", HTTPStatus.OK
	else:
		return f"Course already exists", HTTPStatus.BAD_REQUEST 


@app.route('/courses/<int:course_id>/grades', methods=['POST'])
def insert_grades(course_id, student_id):
	grades = request.get_json()
	inserted = campus.insert_grades_for_student(grades)
	if inserted:
		return f"grades created.", HTTPStatus.OK
	else:
		return f"Could not found that course/student combination", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_courses(course_id):
	course = request.get_json()
	updated = campus.update_course(course_id, course)
	if updated:
		return f"Course updated.", HTTPStatus.OK
	else:
		return f"Course not found", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>/grades/<int:student_id>', methods=['PUT'])
def update_grades(course_id, student_id):
	grades = request.get_json()
	updated = campus.update_grades(course_id, student_id, grades)
	if updated:
		return f"Grades updated.", HTTPStatus.OK
	else:
		return f"Grade not found", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
	deleted = campus.delete_course(course_id)
	if deleted:
		return f"Deleted course {course_id}", HTTPStatus.OK
	else:
		return f"Course {course_id} not found", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>/grades/<int:student_id>', methods=['DELETE'])
def delete_grades(course_id, student_id):
	deleted = campus.delete_grades(course_id, student_id)
	if deleted:
		return f"Deleted grades from student {student_id}, course {course_id}",\
				HTTPStatus.OK
	else:
		return f"Grade not found", HTTPStatus.NOT_FOUND 

