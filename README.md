# 3rd Section of the WIS (World Wide Web Information Systems) assignment.

In the 3rd section you are asked to connect the implementations of Section 1 and Section 2 using JavaScript, 
in order to deploy a dynamic website. JS allows you to create interactions between a static HTML page and a REST API.<br />
Interaction 1: When a user searches for a product (in search bar in products page), the website must do a GET request in the 
endpoint \search (which was implemented in the 2nd Section - SectionB) using the text in the search box. When the request
is completed, the results of the search will be appear on the products page. <br />
Interaction 2: When a user clicks on the photo of the product (or in the like button), a POST request should happen in the endpoint
\like to update the likes count of the product. <br />
Interaction 3: In the slideshow of the home page, the photos of the top 5 most popular products should appear, which are returned
from the GET request of the endpoint \popular-products. <br />
NOTE: For the POST request you must define the "Content-Type" header to "application/json".


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