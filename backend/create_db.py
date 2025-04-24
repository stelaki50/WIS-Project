from pymongo            import MongoClient
from insert_product     import InsertProduct
from delete_product     import DeleteProduct
from pymongo.server_api import ServerApi
from app                import mongo_uri

# connect to MongoDB
client = MongoClient(mongo_uri, server_api=ServerApi('1'))

# create or switch to a database
db = client["PCStore"]

# create or switch to a collection
collection = db["PCParts"]

try:
    if __name__ == "__main__":
        # Main DB Handler Menu
        def main_menu():
            while True:
                print("\n===| PC Parts E-shop Store Database Handler |===\n")
                print("Enter 'insert' to insert a product")
                print("Enter 'delete' to delete a product")
                print("Enter 'view' to view the products of the database")
                print("Enter 'help' if you get stuck")
                print("Enter 'exit' to quit")
                option = input("Enter your option: ")
                if option == 'exit':
                    print("Exiting...")
                    break
                elif option not in ['insert', 'delete', 'help', 'view']:
                    print("Wrong option entered. Please enter a correct option.")
                else:
                    handle_option(option)

        # handle each option
        def handle_option(option):
            if option == 'insert':
                product_input = InsertProduct(collection)
                print(f"Product {product_input.get_product_name()} inserted successfully into the database.")
            elif option == 'view':
                products = list(collection.find())
                print(f"\nThere are {len(products)} products in the database:\n")

                if products:
                    for product in products:
                        print(f"{product}\n")
                else:
                    print("No products found in the database.")
            elif option == 'delete':
                deleted_product = DeleteProduct(collection=collection)
                print(f"Product {deleted_product.get_deleted_product_name()} deleted successfully from the database.")
            elif option == 'help':
                print("In this CLI tool you can freely insert and delete products in the database.")
                print("You can also view the products of the database, everytime you make any changes.")
                print("NOTE: when you insert a product, just make sure to include only the name of the image file and not the path.")
                print("The image must be into the folder /static/products_images/product-photo.jpg otherwise it will not appear in the website.")
                
        main_menu()

except Exception as e:
    raise ValueError(f"An error occurred: {e}")
