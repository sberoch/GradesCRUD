from pymongo import MongoClient

#TODO: Get these variables from environment
URI = 'mongodb+srv://admin:admin@campus.japbq.mongodb.net/test'
NAME = 'campus'

class DataSource:
	def __init__(self):
		self.db = MongoClient(URI)[NAME]


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

	#TODO: terminar
	def update_grade(self, student_id, course_id, grade_id, updated_grade):
		query = {
			'courseid': course_id,
			'userid': student_id,
			'gradeitems.id': grade_id
		}
		action = {
			'$set': {
				'gradeitems.$.content': updated_grade
			}
		}
		self.db.grades.update_one(query, action)


	def update_course(self, course_id, fields):
		pass


	def delete_course(self, course_id):
		self.db.courses.delete_one({'_id': course_id})


	def delete_grade(self, course_id, student_id, grade_id):
		query = {
			'courseid': course_id,
			'userid': student_id,
		}
		action = {
			'$pull': {
				'gradeitems': {
					'id': grade_id
				}
			}
		}
		self.db.grades.update_one(query, action)


	def get_course(self, course_id):
		return self.db.courses.find({'_id': course_id})


	def get_courses(self, query={}):
		return self.db.courses.find(query)


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
		return self.db.grades.find(query, projection)


	def insert_course(self, new_course):
		self.db.courses.insert_one(new_course)


	def insert_grade(self, course_id, student_id, grade):
		query = {
			'courseid': course_id,
			'userid': student_id
		}
		action = {
			'$push': {
				'gradeitems': grade
			}
		}
		self.db.grades.update_one(query, action)










