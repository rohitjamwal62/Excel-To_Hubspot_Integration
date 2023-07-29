import requests,json
def GetAllDeals():
    AllDealsHere = list()
    url = "https://api.hubapi.com/crm/v4/objects/deals/?limit=100"
    payload={}
    headers = {
    'authorization': 'Bearer pat-na1-c5b4ca80-ef0e-41c3-a4f1-c584d0081dc8'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    count=0
    while True:
        try: 
            AfterValue = json.loads(response.text).get('paging').get('next').get('after')
            url =f"https://api.hubapi.com/crm/v4/objects/deals/?hasmore=true&limit=100&after={AfterValue}"
            payload={}
            headers = {
            'authorization': 'Bearer pat-na1-c5b4ca80-ef0e-41c3-a4f1-c584d0081dc8'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            StoreResponse = json.loads(response.text)
            res = StoreResponse.get('results')
            for i in res:
                data = i.get('properties').get('dealname')
                GetId = i.get('id')
                AllDealsHere.append({"Deal":data,"Id":GetId})
            count +=1
        except Exception as e:
            break
    return AllDealsHere
