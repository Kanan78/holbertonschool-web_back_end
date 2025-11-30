#!/usr/bin/env python3
"""This module defines the function insert_school"""

def insert_school(mongo_collection, **kwargs):
    """This function inserts a new document in a collection based on kwargs"""
    result = mongo_collection_insert._one(kwargs)
    return result.inserted_id
