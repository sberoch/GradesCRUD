from pymongo import MongoClient

#TODO: Get these variables from environment
URI = 'mongodb+srv://admin:admin@campus.japbq.mongodb.net/test'
NAME = 'campus'

class DataSource:
	def __init__(self):
		self.db = MongoClient(URI)[NAME]

	def test(self):
		return self.db.courses.find({'test': 'test'})

	def clear(self):
		self.db.courses.delete_many({})
		self.db.grades.delete_many({})

	def insert_courses(self, courses):
		for course in courses:
			course['_id'] = course.pop('id')
		self.db.courses.insert_many(courses)

	def insert_grades(self, course_grades):
		if course_grades['usergrades']:
			self.db.grades.insert_many(course_grades['usergrades'])

	def update_grade(self, student_id, course_id, grade_id, fields):
		pass

	def update_course(self, course_id, fields):
		pass

	def delete_course(self, course_id):
		self.db.courses.delete_one({'_id': course_id})

	def delete_grade(self, course_id, student_id, grade_id):
		pass

	def get_course(self, course_id):
		pass

	def get_courses(self, query={}):
		return self.db.courses.find(query)

	def get_grades(self, course_id):
		pass

	def insert_course(self):
		pass

	def insert_grade(self):
		pass










