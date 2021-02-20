#!/usr/bin/env python
import requests
import pandas as pd

class Records:

    def __init__(self, genusKey=None, year=None): 
        # store input params
        self.genusKey = genusKey
        self.year = year
        # will be used to store output results
        self.df = None
        self.json = None
    def get_single_batch(self, offset=0, limit=20):
        "returns JSON result for a small batch query"
        res = requests.get(
            url="https://api.gbif.org/v1/occurrence/search/",
            params={
            "offset": offset,
            "limit": limit,
            "genusKey": self.genusKey,
            "year": self.year,
            }
        )
        return res.json()
    def get_all_records(self):
        "stores result for all records to self.json and self.df"
        alldata = []
        offset = 0
        while 1:
            jdata = self.get_single_batch(offset, 300)
            offset += 300
            alldata.extend(jdata["results"])
            if jdata["endOfRecords"]:
                print(f'Done. Found {len(alldata)} records')
                break
            print('.', end='')
        self.df = pd.json_normalize(alldata)
        self.json = alldata
        return alldata
