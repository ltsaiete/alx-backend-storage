#!/usr/bin/env python3
"""
This is a simple module and it only has
one function called list_all
"""


def list_all(mongo_collection):
    """ lists all documents in a collection

    Args:
        mongo_collection (_type_): mongodb collection
    """
    return mongo_collection.find()
