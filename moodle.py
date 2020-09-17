import requests
import json
import datetime

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
	for course in courses:
		course['formatted_startdate'] = _get_formatted_startdate(course['startdate'])
	return [c for c in courses if c['format'] != 'site']


def _get_formatted_startdate(startdate_timestamp):
	date = datetime.datetime.fromtimestamp(startdate_timestamp)
	year = date.year

	if (date.month >= 1 and date.month <= 5) or (date.month == 12):
		quarter = '1C'
	elif date.month >= 6 and date.month <= 11:
		quarter = '2C'
	else:
		raise ValueError('Can not get quarter from date ' + str(date))

	return quarter + '-' + str(year)
