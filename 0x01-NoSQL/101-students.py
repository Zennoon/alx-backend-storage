#!/usr/bin/env python3
"""
Contains:
    Functions
    =========
    top_students - Returns all students ranked by average score
"""


def top_students(mongo_collection):
    """Returns all students ranked by average score"""
    pipeline = [
        {"$unwind": "$topics"},
        {"$group": {
            "_id": "$_id",
            "name": {"$first": "$name"},
            "topics": {"$push": "$topics"},
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))
