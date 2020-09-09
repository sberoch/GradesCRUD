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
		courses = [c for c in courses if c['format'] != 'site']
		for course in courses:
			course['_id'] = course.pop('id')
		self.db.courses.insert_many(courses)