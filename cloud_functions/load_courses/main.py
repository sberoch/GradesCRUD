import moodle
import data_source as ds

def load_courses(request):

	client = ds.DataSource()

	client.clear()
	courses = moodle.get_courses()
	client.insert_courses(courses)

	for course in courses:
		client.insert_grades(moodle.get_grades_for_course(course['_id']))
