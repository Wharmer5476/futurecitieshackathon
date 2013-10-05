import pymongo


class PedestrianCounts(object):

    def __init__(self, mongo_collection):
        self.collection = mongo_collection

    def counts(self, start=None, stop=None, limit=10):
        spec = {}
        if start:
            spec['timestamp'] = {'$gt': start}
        if start and stop:
            spec['timestamp']['$lt'] = stop
        if start:
            return [self.reshape(i) for i in self.collection.find(spec, limit=limit)]

        return [self.reshape(i) for i in self.collection.find(limit=limit)]

    def reshape(self, r):
        d = dict(r)
        d.pop('_id')
        d['pedestrianCount'] = dict(total=d.pop('total_pedestrains'), mean=0.0, std=0.0)
        transformations = dict(
            site_id='siteId',
            site_name='siteName')
        for src, dst in transformations.iteritems():
            d[dst] = d.pop(src)
        return d
