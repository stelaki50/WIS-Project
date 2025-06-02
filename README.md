# 4th Section of the WIS (World Wide Web Information Systems) assignment.

(Optional Section D): Create docker images for deployment. <br>
Created 3 Dockerfiles in the project root directory:<br>
1: Dockerfile.frontend -> web server (sveltekit) with all the files <br>
2: Dockerfile.backend -> python application Flask REST API <br>
3: Dockerfile.mongo -> mongoDB database (atlas)

## Run locally

Follow the steps below to clone and run the project locally.

### 1. Clone the Repository (and choose the branch SectionD)

```bash
git clone https://github.com/your-username/wis-project.git
cd wis-project
git checkout SectionD
```

### **2. Run docker-compose**
In the project root directory, in bash:

```bash
sudo snap install docker
sudo docker-compose up --build
```

This should deploy the project and you can access it after typing "localhost" in your browser.

### **3. Run using terminal**
First, install dependencies:
```bash
pip install -r requirements.txt
```

In the project frontend directory, in bash:

```bash
npm install
npm run build
npm run dev
```

In the project backend directory, in bash:
```bash
python3.10 app.py
```

This should deploy the project and you can access it after typing "localhost:5173" in your browser.

### **4. Important notices**
The SectionD branch is the final section of the project. The project sucessfully finished. A temporary user with read and write
access to the database is created (if it was read-only some functionalities of the site would not work). Note that every item/product
that appears on the website was used for the project only. THIS IS A UNIVERSITY PROJECT, which pushes students who would like to take a 
step into web development by creating a simple site of their choosing. Feel free to contribute.