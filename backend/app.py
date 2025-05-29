from flask                  import Flask, jsonify, request, send_from_directory
from pymongo                import MongoClient
from flask_cors             import CORS
from bson.objectid          import ObjectId
from dotenv                 import load_dotenv
from pymongo.server_api     import ServerApi
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

static_dir = os.path.join(basedir, '../frontend', 'static')

app = Flask(__name__, static_url_path='/static', static_folder=static_dir)

CORS(app)

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client["PCStore"]
collection = db["PCParts"]

# send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"An error occured: {e}")

# serialize MongoDB documents
def serialize_product(product):
    product['_id'] = str(product['_id'])
    return product

# list all products
@app.route('/api/products')
def get_products():
    products = list(collection.find())
    return jsonify([serialize_product(p) for p in products])

# like a product
@app.route('/api/likes', methods=['POST'])
def like_product():
    # post request with json payload
    data = request.get_json()
    product_id = data.get('id')

    if not product_id:
        return jsonify({'error': 'Product ID is required'}), 400

    try:
        # finds the product matching the _id and increments likes +1
        result = collection.update_one(
            {'_id': ObjectId(product_id)},
            {'$inc': {'likes': 1}})

        # if no product was matched/found
        if result.matched_count == 0:
            return jsonify({'error': 'Product not found'}), 404

        # fetch updated product to return new/updated likes count
        updated_product = collection.find_one({'_id': ObjectId(product_id)})
        updated_product = serialize_product(updated_product)
        
        return jsonify({
            'message': 'Like added successfully',
            'likes': updated_product.get('likes', 0)}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

 
# search for a product by name
@app.route('/api/search', methods=['GET'])
def search_products():
    name_query = request.args.get('name', '').strip()

    try:
        if name_query == "":
            #return all products 
            products = list(collection.find())
        else:
            # search for products where the name contains the query (case-insensitive)
            # and  sort them in increasing order
            products = list(collection.find(
                {'name': {'$regex': name_query, '$options': 'i'}}
            ).sort('price', 1))

        serialized_products = [serialize_product(p) for p in products]
        return jsonify(serialized_products), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    
#return most popular products   
@app.route('/api/popular_products', methods=['GET'])
def popular_products():
    try:
        
        popular_products = list(collection.find().sort("likes", reverse=True).limit(5))
        return jsonify(popular_products), 200
    
    except Exception as e:
        return jsonify({'An error occured': str(e)}), 500
    


# Get a single product by ID
@app.route('/api/products/<product_id>')
def get_product(product_id):
    try:
        product = collection.find_one({'_id': ObjectId(product_id)})
        if product:
            return jsonify(serialize_product(product))
        else:
            return jsonify({'error': 'Product not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
