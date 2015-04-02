import pymongo as m
from bson.objectid import ObjectId

client = m.MongoClient()
db = client.lspl_queries
queries = db.queries

def insert_query(title, sql, tags, desc, who):
    _tags = [ tag.strip() for tag in tags.strip().split(",") \
            if len(tag.strip()) > 0]
    queries.insert({
            "title": title,
            "sql": sql,
            "tags": _tags,
            "desc": desc,
            "who": who
        })

def update_query(id, title, sql, tags, desc, who):
    _tags = [ tag.strip() for tag in tags.strip().split(",") \
            if len(tag.strip()) > 0]

    queries.update({
        "_id": ObjectId(id)
        },
        { "$set" : {
            "title": title,
            "sql": sql,
            "tags": _tags, 
            "desc": desc,
            "who": who
            }}, upsert=False)

def delete_query(id):
    queries.remove({"_id": ObjectId(id)})

def get_queries():
    _queries = []
    for query in queries.find():
        _queries.append(query)
    return _queries

def get_query_details(id):
    return queries.find_one(ObjectId(id))
