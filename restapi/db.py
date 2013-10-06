from geo import geolocation_by_site_id


class PedestrianCounts(object):

    def __init__(self, mongo_collection):
        self.collection = mongo_collection

    def counts(self, start=None, stop=None, offset=0, limit=10):
        print 'offset', offset
        spec = {}
        if start:
            spec['timestamp'] = {'$gte': start}
        if start and stop:
            spec['timestamp']['$lt'] = stop
        if start:
            return [self.reshape(i) for i in self.collection.find(spec, skip=offset, limit=limit)]

        return [self.reshape(i) for i in self.collection.find(limit=limit)]

    def reshape(self, r):
        d = dict(r)
        d.pop('_id')
        d['statistics'] = dict(total=d.pop('total_pedestrains'), mean=0.0, std=0.0)
        transformations = dict(
            site_id='siteId',
            site_name='siteName')
        for src, dst in transformations.iteritems():
            d[dst] = d.pop(src)
        d.pop('owner')
        d['geolocation'] = geolocation_by_site_id[d['siteId']]
        return d
