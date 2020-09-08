from pymongo import MongoClient

#TODO: Get these variables from environment
URI = "mongodb+srv://admin:admin@campus.japbq.mongodb.net/test"
NAME = "campus"

class DataSource:

	def __init__(self):
		self.db = MongoClient(URI)[NAME]

	def test(self):
		return self.db.courses.find({"test": "test"})