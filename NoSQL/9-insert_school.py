#!/usr/bin/env python3
"""
Function that inserts a new document in a MongoDB collection
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document using kwargs
    Returns the _id of the new document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
