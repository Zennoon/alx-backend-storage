#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    schools_by_topic - Returns all documents in a collection
    whose topic attribute contains a given value
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns all documents in a collection whose topic
    attribute contains a given value
    """
    return [*mongo_collection.find({"topics": {"$all": [topic]}})]
