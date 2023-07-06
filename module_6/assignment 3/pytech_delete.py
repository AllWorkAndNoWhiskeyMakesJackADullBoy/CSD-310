#Assignment 6.3
#July 5th, 2023
#Jeff Haberman
#CYBR 410
#Python script to use find() method to display all documents in a collection, use insert_one method to add a new document, delete_one method to delete a document

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
    print(f"Student ID: {student['student_id']}")
    print(f"First Name: {student['first_name']}")
    print(f"Last Name: {student['last_name']}\n")

#create document to insert
new_student_document = {"student_id": 1010, "first_name": "John", "last_name": "Doe"}

#inserting new student into collection
insert_new_student = db.students.insert_one(new_student_document).inserted_id

#display inserted document
print(f"Inserted student record {new_student_document['first_name']} {new_student_document['last_name']} into the students collection with document id {insert_new_student}")

#using find_one method to find new student
new_student = db.students.find_one({'student_id':1010})

#printing the document for new student
print("-- DISPLAYING STUDENT TEST DOC --")

print(f"Student ID: {new_student['student_id']}")
print(f"First Name: {new_student['first_name']}")
print(f"Last Name: {new_student['last_name']}\n")

#deleting document for student id 1010

db.students.delete_one({'student_id':1010})

students = db.students.find()
#displaying all students 
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for student in students:
    print(f"Student ID: {student['student_id']}")
    print(f"First Name: {student['first_name']}")
    print(f"Last Name: {student['last_name']}\n")