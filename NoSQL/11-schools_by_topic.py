#!/usr/bin/env python3
"""
Returns list of schools having a specific topic
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools that have a specific topic

    Args:
        mongo_collection: pymongo collection object
        topic (string): topic to search for

    Returns:
        List of documents that match
    """
    return list(mongo_collection.find({ "topics": topic }))
