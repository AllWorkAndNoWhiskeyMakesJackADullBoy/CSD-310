#Assignment 6.2
#July 5th, 2023
#Jeff Haberman
#CYBR 410
#Python script to find all documents in student collection, then update one record, and return updated document

#installing python tool for MongoDB
import pymongo
from pymongo import MongoClient

#connection to MongoAtlas and setting variables for database and collection
url="mongodb+srv://admin:admin@cluster0.uotjn6t.mongodb.net/"
client= MongoClient(url)
db = client.pytech
students = db.students.find()

#printing all documents in the students collection
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
 
    print(f"Student ID: {student[ 'student_id']}")
    print(f"First Name: {student['first_name']}")
    print(f"Last Name: {student['last_name']}\n")

#updating last name of student_id 1007
updated_student = db.students.update_one({"student_id": 1007}, {"$set": {"last_name": "Smith"}})

#using find_one method to find student
find_student = db.students.find_one({'student_id':1007})

#printing the document for student_id 1007
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")

print(f"Student ID: {find_student['student_id']}")
print(f"First Name: {find_student['first_name']}")
print(f"Last Name: {find_student['last_name']}")
