import pymongo


class Collection():
    
    def __init__(self, mongo_connection, db_name, collection_name):
        self.connection = mongo_connection
        self.collection = mongo_connection[db_name][collection_name]


class PedestrianCounts(Collection):

    def counts(self, limit=10):
        return [i for i in self.collection.find(limit=limit)]

    def reshape_counts(r):
        r.pop('id')
        

