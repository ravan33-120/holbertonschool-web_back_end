#!/usr/bin/env python3
"""
Function that lists all documents in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Returns a list of all documents in the collection
    Returns an empty list if the collection is empty
    """
    return list(mongo_collection.find())
