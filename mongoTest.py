import pymongo
client = pymongo.MongoClient("mongodb+srv://jaydeep_jo:Jay7745@cluster0.jlgmc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

d={
    "Name":"Jaydeep",
    "From" : "From_Pycharm",
    "To" : "To_Mongo"
}

dd = client['mongotest2']
coll = dd["test"]
re = coll.insert_one(d)
print(re)

