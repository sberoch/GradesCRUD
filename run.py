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

print(client.get_courses().next())

#client.delete_course(4)

#for grade in client.get_grades(2):
	#print(grade)


new_grade = {
	'id': 19,
	'itemname': 'Primer Parcial',
	'gradeformatted': 10
}
client.insert_grade(2, 6, new_grade)

updated_grade = {
	'id': 19,
	'itemname': 'Primer Parcial',
	'gradeformatted': 9
}
client.delete_grade(2, 6, 19)

print(client.get_course(2).next())
