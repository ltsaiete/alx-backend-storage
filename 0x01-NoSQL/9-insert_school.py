#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs

    Args:
        mongo_collection (_type_): pymongo collection
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
