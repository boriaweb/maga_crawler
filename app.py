from flask import Flask
from db.query import get_products
from db.query import clean_database
from flask import Response, request
from bson import json_util

app = Flask(__name__)

@app.route('/')
def list_products():
    sku = request.args.get('sku')
    ean = request.args.get('ean') 
    products = get_products(ean=ean, sku=sku)

    return Response(
        json_util.dumps({'total': len(products), 'products':products}), 
        mimetype='application/json'
    )

@app.route('/clean')
def clean_db():
    clean_database()
    return Response(
        json_util.dumps({'success': True}), 
        mimetype='application/json'
    )

app.run(debug=False, host='0.0.0.0')