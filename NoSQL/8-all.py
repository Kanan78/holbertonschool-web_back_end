#!/usr/bin/env python3
"""This module defines the function list_all"""

def list_all(mongo_collection):
    """Lists all documents in a MongoDB collection."""
    docs = list(mongo_collection.find())
    return docs
