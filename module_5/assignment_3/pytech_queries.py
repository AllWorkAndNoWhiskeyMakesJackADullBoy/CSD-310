import pymongo
from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.uotjn6t.mongodb.net/"
client= MongoClient(url)
db = client.pytech


students = db.students.find()
single_student = db.students.find_one({'student_id': 1008})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
	print(f"Student ID: {student['student_id']}")
	print(f"First Name: {student['first_name']}")
	print(f"Last Name: {student['last_name']}\n")


print("-- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print(f"Student ID: {single_student['student_id']}")
print(f"First Name: {single_student['first_name']}")
print(f"Last Name: {single_student['last_name']}\n")