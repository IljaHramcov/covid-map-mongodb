import connectMongo
import loadJson

#Connect to DB
user = 'serviceAcc'
password = '12345'

client = connectMongo.connect(user,password)

#Load Json
#url = "https://opendata.ecdc.europa.eu/covid19/casedistribution/json/"
url = "http://corona.lmao.ninja/v2/countries"

#Write Json to MongoDB
jsonData = loadJson.getData(url)

db = client.covidDB

collection = db.dailyData

collection.drop()
print('Old collection was dropped.')

collection.insert_many(jsonData)
print('New collection was inserted.')

print(collection.count_documents({}))