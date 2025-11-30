#!/usr/bin/env python3
"""It inserts a new document in a collection based on kwargs"""

def insert_school(mongo_collection, **kwargs):
    result = mongo_collection_insert._one(kwargs)
    return result.inserted_id
