#!/usr/bin/env python3
"""
Displays some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def main():
    """It provides some stats about Nginx logs stored in MongoDB"""

    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    col = db.nginx

    # Total number of logs
    total_logs = col.count_documents({})
    print(f"{total_logs} logs")

    # HTTP Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = col.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Number of GET /status requests
    status_count = col.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

if __name__ == "__main__":
    main()

