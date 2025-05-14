class InsertProduct:

    def __init__(self, collection):
        self.collection = collection
        print("NOTE: The image of the product must be in /static/products_images/product-image.jgp")
        self.category = input("Category (Graphics Card, Processor, Motherboard, RAM, M2-SSD-HDD, Case, CPU Cooler, Power Supply): ")
        self.image = input("Enter image file name (eg: product-image.jpg): ")
        self.name = input("Enter the name of the product: ")
        self.description = input("Enter a quick description of the product: ")
        self.price = float(input("Enter the price of the product: "))
        self.likes = 0

        self.new_product = {
            "category": self.category,
            "image": self.image,
            "name": self.name,
            "description": self.description,
            "likes": self.likes,
            "price": self.price
        }

        # save to database
        self.save_to_db()

    def get_product_name(self):
        return self.name
    
    def get_product(self):
        return self.new_product

    def save_to_db(self):
        self.collection.insert_one(self.new_product)
