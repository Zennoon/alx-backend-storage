#!/usr/bin/env python3
"""
Contains:
    Global
    ======
    Displays stats about Nginx logs stored in MongoDB
"""
import pymongo


if __name__ == "__main__":
    client = pymongo.MongoClient()
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))

    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        print("\tmethod {}: {}".format(
            method,
            collection.count_documents({"method": method})
            ))

    print("{} status check".format(
        collection.count_documents({"method": "GET", "path": "/status"})
    ))
