#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called update_topics
"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document based on the name

    Args:
        mongo_collection (pymongo): pymongo collection
        name (str): school name to update
        topics (list): list of topics approached in the school
    """
    mongo_collection.update_one(
        {'name': name}, {'$set': {'topics': topics}}, upsert=True)
