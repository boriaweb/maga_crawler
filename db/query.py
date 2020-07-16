from pymongo import MongoClient
import os

client = MongoClient(os.environ["DB_PORT_27017_TCP_ADDR"], 27017)
db = client.products_database

def get_products(ean=None, sku=None):
    params = {}
    if ean is not None:
        params['ean'] = ean
    if sku is not None:
        params['sku'] = sku
    
    products = db.products.find(params)
    return [product for product in products]

def clean_database():
    return db.products.remove()