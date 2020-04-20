import urllib.request, json 
from urllib.request import Request

def getData(url):

    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    openrUrl = urllib.request.urlopen(req)
    if(openrUrl.getcode()==200):
        data = openrUrl.read()
        jsonData = json.loads(data)
        print("Successfully loaded Json.")
    else:
        print("Error receiving data", openrUrl.getcode())
    return jsonData