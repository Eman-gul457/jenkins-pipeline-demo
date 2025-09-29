# 🚀 Jenkins CI/CD Pipeline Demo

This repository demonstrates a simple **CI/CD pipeline** using Jenkins.

---

## 📝 Project Overview

| File | Description |
|------|-------------|
| 🐍 **app.py** | ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) Web application (Flask or similar) |
| 📦 **Dockerfile** | ![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white) Build instructions |
| 📜 **requirements.txt** | Python dependencies |
| 🔧 **Jenkinsfile** | ![Jenkins](https://img.shields.io/badge/Jenkins-D24939?logo=jenkins&logoColor=white) Pipeline configuration |

---

## 📂 Step-by-Step Setup

1. 🐍 **Create `app.py`** → simple Flask app  
2. 📜 **Add `requirements.txt`** → list dependencies (`Flask`)  
3. 📦 **Create `Dockerfile`** → define build process  
4. 🛠 **Build Docker Image**  
   ```bash
   docker build -t myapp .

---
### ✅ App Running
![App Running](screenshots/app_running.png)

### 🌐 Browser Output (5000 port)
![Browser Output 5000](screenshots/browser_output(5000 port).png)

### 🌐 Browser Output (9090 port)
![Browser Output 9090](screenshots/browser_output(9090 port).png)

### 🚀 Pipeline Success
![Pipeline Success](screenshots/pipeline_success.png)

