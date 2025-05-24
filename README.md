# 4th Section of the WIS (World Wide Web Information Systems) assignment.

(Optional Section D): Create docker images for deployment. <br>
Created 3 Dockerfiles in the project root directory:<br>
1: Dockerfile.frontend -> web server (sveltekit) with all the files <br>
2: Dockerfile.backend -> python application Flask REST API
3: Dockerfile.mongo -> mongoDB database (atlas)
## Run locally

Follow the steps below to clone and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wis-project.git
cd wis-project
```

### **2. Run docker-compose**
In the project root directory, in bash:

```bash
sudo docker-compose up --build
```

This should deploy the project and you can access it after typing "localhost" in your browser.

### **3. Important notices**
This is just a demonstration of what we're trying to accomplish as a team,
the database itself is not published here, for security reasons.
For this safe result a .env file is created and this: MONGO_URI=mongodb+srv://username:password@your-project-db.ueop5j7.mongodb.net/?retryWrites=true&w=majority&appName=Your-Project-DB is inside of the file, so we can access safely the database.
Also, a simple CLI script in Python (create_db.py) for adding, deleting and viewing products in our database is created.
This script is very useful and you can test it yourself on your projects or on our project as well (after connecting to your MongoDB atlas database server).