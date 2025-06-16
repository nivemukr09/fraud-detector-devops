# 🛡️ Insurance Claim Fraud Detector (DevOps Project)

This is a full-stack DevOps project that simulates a real-world **Insurance Claim Fraud Detection** system, powered by a machine learning model. It is fully containerized, CI/CD-enabled, and deployable on Kubernetes using ArgoCD and Helm.

---

## 🧠 Project Overview

Insurance fraud costs billions each year. This project uses an ML model to classify insurance claims as either **fraudulent** or **legitimate** based on factors like:

- Claim amount
- Number of past accidents
- Age of the policyholder
- Claim type (vehicle, health, home)
- Region (north, south, east, west)

---

## 📦 Tech Stack

### Backend
- Python 3.10
- Flask
- Scikit-learn
- NumPy, Pandas
- REST API with CORS enabled

### Machine Learning
- Logistic Regression
- OneHotEncoding + ColumnTransformer
- Pickle for model persistence

### DevOps
- Docker (containerization)
- Jenkins (CI pipeline)
- Helm (packaging for Kubernetes)
- ArgoCD (CD to Kubernetes)
- Prometheus & Grafana (monitoring)
- GitHub (source control)

---

## 🚀 Project Structure

fraud-detector-devops/
├── backend/
│ ├── app/
│ │ ├── main.py # Flask API
│ │ ├── utils.py # Model loading & prediction logic
│ │ ├── model.pkl # Trained ML model
│ │ ├── requirements.txt # Python dependencies
│ │ └── Dockerfile # Flask app container
├── jenkins/
│ └── Jenkinsfile # CI pipeline
├── helm/
│ └── fraud-detector-chart/ # Helm chart for deployment
├── k8s/
│ └── manifests.yaml # K8s manifests (optional if not using Helm)
└── README.md


---

## 🔧 Local Setup
```bash
1. Clone the Repo


git clone https://github.com/nivemukr09/fraud-detector-devops.git
cd fraud-detector-devops/backend/app

2. Setup Virtual Environment
py -3.10 -m venv venv
source venv/Scripts/activate    # Use venv\Scripts\activate.bat if on CMD
pip install -r requirements.txt

3. Run the App
python main.py
App will be available at: http://localhost:5000

🧪 CI/CD Pipeline (Jenkins)
Clone repo
Build Docker image
Push to DockerHub
Deploy to Kubernetes via Helm/ArgoCD
