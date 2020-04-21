import connectMongo
import loadJson
import time



#Connect to DB.
#First you have to create an user and whitelist your IP. Then get your connection String.
user = 'serviceAcc'
password = '12345'

connectionString = 'mongodb+srv://'+user+':'+password+'@mongodb-af1em.gcp.mongodb.net/test?retryWrites=true&w=majority'


client = connectMongo.connect(connectionString)

while True:

    #Dataset URL
    url = "http://corona.lmao.ninja/v2/countries"

    #Get JSON from URL
    jsonData = loadJson.getData(url)

    #Create reference to database. If there is no Database called covidDB it will be created.
    db = client.covidDB

    #Create reference to collection (table). If there is no Collection called dailyData it will be created.
    collection = db.dailyData

    #Drop old collection.
    collection.drop()
    print('Old collection was dropped.')

    #Insert array of Objects to MongoDB Atlas
    collection.insert_many(jsonData)
    print('New collection was inserted.')

    print(collection.count_documents({}))

    time.sleep(30)