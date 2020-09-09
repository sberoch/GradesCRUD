from pymongo import MongoClient

#TODO: Get these variables from environment
URI = 'mongodb+srv://admin:admin@campus.japbq.mongodb.net/test'
NAME = 'campus'

class DataSource:

	def __init__(self):
		self.db = MongoClient(URI)[NAME]

	def test(self):
		return self.db.courses.find({'test': 'test'})

	def insert_courses(self, courses):
		for course in courses:
			course['_id'] = course.pop('id')
		self.db.courses.insert_many(courses)

	def insert_grades(self, course_grades):
		if course_grades['usergrades']:
			self.db.grades.insert_many(course_grades['usergrades'])