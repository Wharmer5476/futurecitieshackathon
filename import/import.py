import csv
from os import environ
import sys
from datetime import datetime

from pymongo import MongoClient


db_user = environ['futurecities_db_user']
db_pass = environ['futurecities_db_pass']
db_uri = 'mongodb://%s:%s@ds049548.mongolab.com:49548' % (db_user, db_pass)
conn = MongoClient('mongodb://%s:%s@ds049548.mongolab.com:49548/futurecitieshackathon' % (db_user, db_pass))
coll = conn['futurecitieshackathon']['pedestrianCounts']
print conn
print coll

def import_lines():
    for l in sys.stdin:
        (total_pedestrains, site_id, borough, hour, year, owner, month, site_name, day) = l.split(',')
        d = datetime(int(year), int(month), int(day), int(hour.split(':')[0]))
        print coll.insert(dict(
            total_pedestrains=int(total_pedestrains),
            site_id=site_id,
            borough=borough,
            timestamp=d,
            owner=owner,
            site_name=site_name))

def main():
    import_lines()

if __name__ == '__main__':
    main()