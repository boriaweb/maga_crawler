from pymongo import MongoClient
import os, pprint
from .query import get_products

client = MongoClient(os.environ["DB_PORT_27017_TCP_ADDR"], 27017)
db = client.products_database

def get_stock_total(marca=None):

    query_params = [{
            '$group': {
                '_id': None,
                'total': {
                    '$sum':  '$estoque' 
                    }
                }
            }]
        
    if marca is not None:
        query_params = [
            {
                '$match': {
                    'marca': marca
                }
            },
            {
                '$group': {
                    '_id': None,
                    'total': {
                        '$sum':  '$estoque' 
                        }
                    }
                }
        ]
    
    query_result = db.products.aggregate(query_params)
    
    query_result = list(query_result)
    total = query_result[0]['total'] if len(query_result) > 0 else 0
    
    return total

def get_report(marca):
    marca = marca.upper()
    
    total_estoque = get_stock_total()
    total_estoque_marca = get_stock_total(marca=marca)
    market_share = 0
    
    if total_estoque > 0:
        market_share = "{:.2f}".format( (total_estoque_marca / total_estoque) * 100 )
    
    market_share = str(market_share) + '%'


    products_list = []
    if total_estoque_marca > 0:
        products = get_products(marca=marca)
        
        for product in products:
            estoque_produto = product['estoque']
            ruptura = "{:.2f}".format((estoque_produto / total_estoque_marca) * 100)
            
            products_list.append({
                        'nome': product['produto'], 
                        'ruptura': str(ruptura) + '%',
                        'quantidade': estoque_produto
                    })
    
    return {
        'marca': marca, 
        'total_estoque_marca' :  total_estoque_marca,
        'market_share': market_share,
        'ruptura': products_list
    }
