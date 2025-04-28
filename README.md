# 2nd Section of the WIS (World Wide Web Information Systems) assignment.

The endpoints you will deploy/implement are: /search: Deploy a GET request that will accept a parameter by name and will search for a product in the database based on the name and will return the product (or products). In case it finds more than one product, then the products that will be returned will be in descending order classified by price. The request will return a list of all products found in JSON format. If no product is found, then the endpoint will return an empty list[]. For example, if you search for a product with the name Paper, then the search should return all products that have the word Paper in the name, e.g. Paper A4, Paper A3. However, if you search for a product with the name Paper A3, then the search should return only that product. If the search parameter is an empty string, then it should return all the products in the eshop. <br />
/like: Deploy a POST request that will accept a parameter with the id of a product and will update the Likes field of the product by adding the number 1 to the existing value. <br />
/popular-products: Develop a GET request that will return a list of the top 5 most popular products based on the number of Likes.<br />


## Run locally

Follow the steps below to clone and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wis-project.git
cd wis-project
```

### **2. Install dependencies**
Make sure you have Node.js (preferably v18 or higher) installed.

```bash
npm install
pip install -r requirements.txt
```

### **3. Start the development server**
This will start the app at http://localhost:5173/ (or the next available port).

```bash
npm run dev
python app.py
```

### **4. Important notices**
This is just a demonstration of what we're trying to accomplish as a team,
the database itself is not published here, for security reasons.
For this safe result a .env file is created and this: MONGO_URI=mongodb+srv://username:password@your-project-db.ueop5j7.mongodb.net/?retryWrites=true&w=majority&appName=Your-Project-DB is inside of the file, so we can access safely the database.
Also, a simple CLI script in Python (create_db.py) for adding, deleting and viewing products in our database is created.
This script is very useful and you can test it yourself on your projects or on our project as well (after connecting to your MongoDB atlas database server).