import requests
import json
from AllMatchResults import MatchingResults

def UpdateDeals():
  HubspotMatchingRecords = MatchingResults()
  for i in HubspotMatchingRecords:
    Deals = i.get('Deal')
    cageCode = i.get('Cage_Code')
    ExpirationDate = i.get('ExpirationDate')
    Id = i.get('Id')
    
    firstLoc = ExpirationDate[0:4]
    # firstresult = ExpirationDate.replace(firstLoc,firstLoc +"-")
    f1 = ExpirationDate.replace(firstLoc,firstLoc +"-").split('-')[0]
    f2 = ExpirationDate.replace(firstLoc,firstLoc +"-").split('-')[1]
    secondresult = f2[0:2]
    f3 = f2[-2:]
    getDate = f1+"-"+secondresult+"-"+f3


    url = f"https://api.hubapi.com/crm/v3/objects/deals/{Id}/?hasmore=true&limit=100&properties=Cage_Code,Expiration_Date"
    payload = json.dumps({
      "properties": {
        "dealname": Deals,
        "cage_code": cageCode,
        "expiration_date": getDate
      }
    })

    headers = {
      'authorization': 'Bearer pat-na1-c5b4ca80-ef0e-41c3-a4f1-c584d0081dc8',
      'content-type': 'application/json'
    }

    response = requests.request("PATCH", url, headers=headers, data=payload)
    storeResponse = json.loads(response.text)
    print(storeResponse)
UpdateDeals()