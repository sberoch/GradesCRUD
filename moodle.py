import requests
import json

#TODO: Get this variable from environment
base_url = 'http://www.ing-racero.com.ar/webservice/rest/server.php'

#TODO: Get the token from a proper auth 
token = '44d471767bb81f48258fd27698d233d1'

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