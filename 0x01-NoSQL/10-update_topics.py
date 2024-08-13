#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    update_topics - Updates document with given name value
    by adding a new attribute whose value is a given list
"""


def update_topics(mongo_collection, name, topics):
    """
    Updates document with given name value by adding a new
    attribute whose value is a given list
    """
    mongo_collection.update_one(
        {"name": name},
        {"$set": {"topics": topics}}
    )
