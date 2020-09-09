import data_source as ds
import moodle

client = ds.DataSource()

def refresh():
	print('Deleting all previous data')
	client.clear()

	courses = moodle.get_courses()
	print('Inserting courses')
	client.insert_courses(courses)

	for course in courses:
		print('Inserting grades for course', course['_id'])
		client.insert_grades(moodle.get_grades_for_course(course['_id']))

refresh()