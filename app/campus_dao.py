from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from bson.json_util import dumps

#TODO: Get these variables from environment
URI = 'mongodb+srv://admin:admin@campus.japbq.mongodb.net/test'
NAME = 'campus'

class CampusDAO:
	def __init__(self):
		self.db = MongoClient(URI)[NAME]


	def clear(self):
		self.db.coursesTest.delete_many({})
		self.db.gradesTest.delete_many({})


	def insert_courses(self, courses):
		for course in courses:
			course['_id'] = course.pop('id')
		self.db.coursesTest.insert_many(courses)


	def insert_grades(self, course_grades):
		if course_grades['usergrades']:
			self.db.gradesTest.insert_many(course_grades['usergrades'])


	def update_course(self, course_id, updated_course):
		query = { 
			'_id': course_id
		}
		action = {
			'$set': updated_course
		}
		res = self.db.coursesTest.update_one(query, action)
		return res.modified_count == 1


	def update_grades(self, course_id, student_id, updated_grade):
		query = {
			'courseid': course_id,
			'userid': student_id,
		}
		action = {
			'$set': updated_grade
		}
		res = self.db.gradesTest.update_one(query, action)
		return res.modified_count == 1


	def delete_course(self, course_id):
		res = self.db.coursesTest.delete_one({'_id': course_id})
		return res.deleted_count == 1


	def delete_grades(self, course_id, student_id):
		query = {
			'courseid': course_id,
			'userid': student_id,
		}
		res = self.db.gradesTest.delete_one(query)
		return res.deleted_count == 1


	def get_course(self, course_id):
		return self.db.coursesTest.find_one({'_id': course_id})


	def get_courses(self, query={}):
		return list(self.db.coursesTest.find(query))


	def get_grades(self, course_id):
		query={
		    'courseid': course_id
		}
		projection={
		    '_id': 0, 
		    'courseid': 1, 
		    'userid': 1, 
		    'userfullname': 1, 
		    'gradeitems.id': 1, 
		    'gradeitems.itemname': 1, 
		    'gradeitems.gradeformatted': 1
		}
		return list(self.db.gradesTest.find(query, projection))


	def insert_course(self, new_course):
		try:
			self.db.coursesTest.insert_one(new_course)
			return True
		except DuplicateKeyError:
			return False
		

	def insert_grades_for_student(self, grades):
		try:
			self.db.gradesTest.insert_one(grades)
			return True
		except DuplicateKeyError:
			return False










