from flask                  import Flask, jsonify, request
from pymongo                import MongoClient
from flask_cors             import CORS
from bson.objectid          import ObjectId
from dotenv                 import load_dotenv
from pymongo.mongo_client   import MongoClient
from pymongo.server_api     import ServerApi
import os

load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))

static_dir = os.path.join(basedir, '..', 'static')

app = Flask(__name__, static_url_path='/static', static_folder=static_dir)

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

if __name__ == '__main__':
    app.run(debug=True)
