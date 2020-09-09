import data_source as ds
import requests
import json


base_url = 'http://www.ing-racero.com.ar/webservice/rest/server.php'
token = '44d471767bb81f48258fd27698d233d1'

grades = ds.DataSource()


def get_courses():
	params = {
		'wstoken': token, 
		'wsfunction': 'core_course_get_courses',
		'moodlewsrestformat': 'json'
	}
	return requests.get(base_url, params=params)


grades.insert_courses(get_courses().json())