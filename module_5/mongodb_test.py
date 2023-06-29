import pymongo,sys
from pymongo import MongoClient

url="mongodb+srv://admin:admin@cluster0.uotjn6t.mongodb.net/";
client= MongoClient(url)
db = client.pytech
col= db.list_collection_names()

print("-- Pytech Collections List --")
print(col)
print()
print()
answer = input("End of application. Press Enter to exit..") 
sys.exit()
