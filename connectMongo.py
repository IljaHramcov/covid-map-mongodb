from pymongo import MongoClient

def connect(connectionString):
    # Get first your connection String.
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient(connectionString)
    db=client
    print('Successfully connected to MongoDB.')
    return db
    