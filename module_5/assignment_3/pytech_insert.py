import pymongo
from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.uotjn6t.mongodb.net/"
client= MongoClient(url)
db = client.pytech

new_student_object = ({"student_id":1007, "first_name":"Thorin", "last_name":"Oakenshield"})
new_student_Id = db.students.insert_one(new_student_object).inserted_id
first_name = new_student_object["first_name"]
last_name = new_student_object["last_name"]
print(f"Inserted student record {first_name} {last_name} into the students collection with document id {new_student_Id}")

new_student_object = ({"student_id":1008, "first_name":"Bilbo", "last_name":"Baggins"})
new_student_Id = db.students.insert_one(new_student_object).inserted_id
first_name = new_student_object["first_name"]
last_name = new_student_object["last_name"]
print(f"Inserted student record {first_name} {last_name} into the students collection with document id {new_student_Id}")

new_student_object = ({"student_id":1009, "first_name":"Frodo", "last_name":"Baggins"})
new_student_Id = db.students.insert_one(new_student_object).inserted_id
first_name = new_student_object["first_name"]
last_name = new_student_object["last_name"]
print(f"Inserted student record {first_name} {last_name} into the students collection with document id {new_student_Id}")