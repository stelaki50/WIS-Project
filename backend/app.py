from flask                  import Flask, jsonify, request
from pymongo                import MongoClient
from flask_cors             import CORS
from bson.objectid          import ObjectId
from dotenv                 import load_dotenv
from pymongo.mongo_client   import MongoClient
from pymongo.server_api     import ServerApi
import os

load_dotenv()

app = Flask(__name__, static_url_path='/static',
            static_folder='/home/pismi/Desktop/WIS-Project/static')
CORS(app, origins=["http://localhost:5173"])

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri, server_api=ServerApi('1'))
db = client["PCStore"]
collection = db["PCParts"]

# send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# serialize MongoDB documents
def serialize_product(product):
    product['_id'] = str(product['_id'])
    return product

@app.route('/api/products')
def get_products():
    products = list(collection.find())
    return jsonify([serialize_product(p) for p in products])

@app.route('/like', methods=['POST'])
def like_product():
    try:
        # get product id from request
        product_id = request.form.get('id') or request.json.get('id')
        
        if not product_id:
            return jsonify({"error": "Missing product id"}), 400
        
        # convert to ObjectId
        try:
            product_oid = ObjectId(product_id)
        except Exception:
            return jsonify({"error": "Invalid product id format"}), 400
        
        # find and update the product's likes
        result = collection.update_one(
            {"_id": product_oid},
            {"$inc": {"likes": 1}})
        
        if result.matched_count == 0:
            return jsonify({"error": "Product not found"}), 404
        
        return jsonify({"message": "Like added successfully!"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
