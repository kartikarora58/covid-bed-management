import pymongo
from bson.objectid import ObjectId


class DB:
    def __init__(self):
        encoded_url = "mongodb+srv://root:root@cluster0.kheuu.mongodb.net/mydb?retryWrites=true&w=majority"
        client = pymongo.MongoClient(encoded_url)
        # connecting to database
        db = client['mydb']
        self.collection = db['bed']

    def register_user(self, record):
        x = self.collection.insert_one(record)
        return x.inserted_id

    def retrieve_user(self, credentials):
        query = {'email': credentials[0], 'password': credentials[1]}
        docs = list(self.collection.find(query))
        return docs

    def save_hospital(self, id, data):
        query = {'_id': ObjectId(id)}
        values = {"$set": {"hospital_details": data}}
        self.collection.update_one(query, values)
        print("Successful")

    def edit_hospital(self, id):
        query = {'_id': ObjectId(id)}
        docs = list(self.collection.find(query, {'_id': 0, 'email': 0, 'password': 0}))
        print(docs[0]['hospital_details'])
        return docs[0]['hospital_details']

    def retrieve_data(self):
        data = list(self.collection.find({}, {'hospital_details': 1, '_id': 0}))
        return data
