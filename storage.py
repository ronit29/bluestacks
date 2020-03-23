
import pymongo


'''MongoDb used as Storage for Saving and reading search queries on the bot
Implements two method
write()
    Creates a new record for every search in the mongo collection
read()
    Queries the collection which contains the matching data
'''
class Storage():

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        self.mycol = mydb["customers"]

    def write(self, data):
        """
        Inserts the Query result into the collection
        """
        self.mycol.insert_one({"query":data})

    def read(self, data):
        """
        Fetch the history records for all matching with query using mongo regex operator
        """
        query = { "query": {'$regex': '.*'+str(data)+'.*'} }
        mydoc = self.mycol.find(query)
        return mydoc
