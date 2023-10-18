#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called schools_by_topic
"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic:

    Args:
        mongo_collection (pymongo): pymongo collection
        topic (str): will be topic searched
    """

    mongo_collection.find({'topics': {'$all': [topic]}})
