from pymongo import MongoClient

def connect(user, password):
    # connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
    client = MongoClient('mongodb+srv://'+user+':'+password+'@mongodb-af1em.gcp.mongodb.net/test?retryWrites=true&w=majority')
    db=client
    print('Successfully connected to MongoDB.')
    return db
    