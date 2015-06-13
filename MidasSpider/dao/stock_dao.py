#coding=utf-8
from pymongo import MongoClient
import sys


def get_mongo_client():
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.prod
    coll = db.StockMisc
    return client, db, coll

def main():
    client, db, coll = get_mongo_client()
    fileHandle = open('D://MktData//RawData//stock_concept.txt', 'w')
    for document in coll.find({"_id": "AllStockNames"}):
        allStockNames = document["stockNames"]
        for stockName in allStockNames:
            if stockName[0:3] == "IDX":
                pass
            else:
                name = stockName[2:len(stockName)]
                print name
                fileHandle.write('%s\ts%s\t\n' % (name, name))
    fileHandle.close()


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    main()