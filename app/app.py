from flask import Flask, jsonify, request
from http import HTTPStatus
import campus_dao as cdao

app = Flask(__name__)

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


@app.route('/courses/<int:course_id>/students/<int:student_id>/grades', methods=['POST'])
def insert_grade(course_id, student_id):
	grade = request.get_json()
	inserted = campus.insert_grade(course_id, student_id, grade)
	if inserted:
		return f"Grade created.", HTTPStatus.OK
	else:
		return f"Could not found that course/student combination", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>', methods=['PUT'])
def update_course(course_id):
	course = request.get_json()
	updated = campus.update_course(course_id, course)
	if updated:
		return f"Course updated.", HTTPStatus.OK
	else:
		return f"Course not found", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>/students/<int:student_id>/grades/<int:grade_id>', methods=['PUT'])
def update_grade(course_id, student_id, grade_id):
	grade = request.get_json()
	updated = campus.update_grade(course_id, student_id, grade_id, grade)
	if updated:
		return f"Grade updated.", HTTPStatus.OK
	else:
		return f"Grade not found", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
	deleted = campus.delete_course(course_id)
	if deleted:
		return f"Deleted course {course_id}", HTTPStatus.OK
	else:
		return f"Course {course_id} not found", HTTPStatus.NOT_FOUND 


@app.route('/courses/<int:course_id>/students/<int:student_id>/grades/<int:grade_id>', methods=['DELETE'])
def delete_grade(course_id, student_id, grade_id):
	deleted = campus.delete_grade(course_id, student_id, grade_id)
	if deleted:
		return f"Deleted grade {grade_id} from student {student_id}, course {course_id}",\
				HTTPStatus.OK
	else:
		return f"Grade {grade_id} not found", HTTPStatus.NOT_FOUND 

