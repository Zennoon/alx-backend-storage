#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    list_all - lists all documents in a mongo collection
"""


def list_all(mongo_collection):
    """Returns a list of all the documents in a collection"""
    return [*mongo_collection.find()]
