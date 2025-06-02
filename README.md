# 4th Section of the WIS (World Wide Web Information Systems) assignment.

(Optional Section D): Create docker images for deployment. <br>
Created 3 Dockerfiles in the project root directory:<br>
1: Dockerfile.frontend -> web server (sveltekit) with all the files <br>
2: Dockerfile.backend -> python application Flask REST API <br>
3: Dockerfile.mongo -> mongoDB database (atlas)

## Run locally

Follow the steps below to clone and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/wis-project.git
cd wis-project
```

### **2. Run with docker (docker-compose)**
NOTE: Make sure you have Node.js latest version installed (LTS version). 
See instructions in section 3 or 4 below based on your OS.<br>

In the project root directory, in bash (For Linux systems):

```bash
sudo snap install docker
sudo docker-compose up --build
```

In the project root directory, in cmd (For Windows systems): <br>
Ensure you have docker desktop installed and running: https://www.docker.com/products/docker-desktop/ <br>

```bash
docker-compose up --build
```

This should deploy the project and you can access it after typing "localhost" in your browser.

### **3. Run manually using linux terminal (Ubuntu)**
NOTE: Node.js https://nodejs.org/en latest version must be installed in your system (LTS version).
```bash
sudo apt update
sudo apt install -y curl
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

Verify installation:
```bash
node -v
npm -v
```

Navigate to the project root directory and install dependencies:
```bash
pip install -r requirements.txt
```

In the project frontend directory, in bash:

```bash
cd frontend
npm install
npm run build
npm run dev
```

In the project backend directory, in bash:
```bash
cd ../backend
python3.10 app.py
```

This should deploy the project and you can access it after typing "localhost:5173" in your browser.

### **4. Run using cmd (Windows 10/11)**
NOTE: Node.js latest version must be installed in your system (LTS version).
Follow installation instructions shown in the website: https://nodejs.org/en <br>
NOTE: Make sure Python 3.10 version is installed. <br>
Also ensure pip is available in your system Path <br>

Verify installation:
```bash
node -v
```

In the project root directory, in bash:

```bash
pip install -r requirements.txt
```

In the project frontend directory install Node.js dependencies, in bash:<br>

```bash
cd frontend
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
npm install
npm run build
npm run dev
```

In the project backend directory, in bash:

```bash
cd ../backend
python3.10 app.py
```

This should deploy the project and you can access it after typing "localhost:5173" in your browser.

### **5. Important notices**
The SectionD branch is the final section of the project. The project sucessfully finished. A temporary user with read and write
access to the database is created (if it was read-only some functionalities of the site would not work). Note that every item/product
that appears on the website was used for the project only. THIS IS A UNIVERSITY PROJECT, which pushes students who would like to take a 
step into web development by creating a simple site of their choosing. Feel free to contribute.