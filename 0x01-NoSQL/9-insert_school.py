#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    insert_document - Inserts a new document to a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document to the given collection using values
    from kwargs
    Returns the newly inserted object's id (_id)
    """
    return mongo_collection.insert_one(kwargs).inserted_id
