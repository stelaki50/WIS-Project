class DeleteProduct:

    def __init__(self, collection):
        self.collection = collection
        self.product_name = input("Enter the full name of the product to delete: ").strip()

        result = self.collection.find_one({"name": self.product_name})

        if result:
            confirm = input(f"Are you sure you want to delete '{self.product_name}'? (y/n): ").strip().lower()
            if confirm == 'y':
                self.delete_from_db()
            else:
                print("Deletion cancelled.")
        else:
            print("Product not found in database.")

    def delete_from_db(self):
        self.collection.delete_one({"name": self.product_name})

    def get_deleted_product_name(self):
        return self.product_name
