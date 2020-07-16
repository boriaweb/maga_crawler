from pymongo import MongoClient
import os

class MongoDBPipeline(object):
    def __init__(self): 
        client = MongoClient(os.environ["DB_PORT_27017_TCP_ADDR"], 27017)
        db = client.products_database
        self.products = db.products
    def process_item(self, item, spider):
        self.products.insert(dict(item))