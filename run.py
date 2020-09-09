import data_source as ds
import requests
import json


base_url = 'http://www.ing-racero.com.ar/webservice/rest/server.php'
token = '44d471767bb81f48258fd27698d233d1'

grades = ds.DataSource()

def get_grades_for_course(course_id):
	params = {
		'wstoken': token, 
		'wsfunction': 'gradereport_user_get_grade_items',
		'moodlewsrestformat': 'json',
		'courseid': course_id
	}
	return requests.get(base_url, params=params).json()

def get_courses():
	params = {
		'wstoken': token, 
		'wsfunction': 'core_course_get_courses',
		'moodlewsrestformat': 'json'
	}
	courses = requests.get(base_url, params=params).json()
	return [c for c in courses if c['format'] != 'site']

courses = get_courses()
grades.insert_courses(courses)
for course in courses:
	print('Inserting course', course['_id'])
	grades.insert_grades(get_grades_for_course(course['_id']))
