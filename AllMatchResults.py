from main import matchResult
from alldeal import GetAllDeals
from copy import copy

def MatchingResults():
    DealRecordsHere = GetAllDeals()
    ExcelMatchingResults = matchResult()
    AllRecordsHere = list()
    for item in DealRecordsHere:
        for item2 in ExcelMatchingResults:
            if item.get('Deal') == item2.get('Deal'):
                new_item = copy(item)
                new_item['Cage_Code'] = item2.get('CadgeCode')
                new_item['ExpirationDate'] =item2.get('ExpirationDate')
                AllRecordsHere.append(new_item)
    return AllRecordsHere
