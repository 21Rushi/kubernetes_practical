# kubernetes_practical
Deployed a Flask frontend and Express backend application locally on a Kubernetes cluster using Minikube. Created Docker images for both applications, configured Kubernetes Deployments and Services using YAML files, and verified successful pod and service communication within the cluster.


## Project Overview
This project demonstrates deployment of a Flask frontend and Express backend application on a local Kubernetes cluster using Minikube. Both applications are containerized using Docker and deployed using Kubernetes Deployments and Services.

---

## Technologies Used

- Python Flask
- Node.js Express
- Docker
- Kubernetes
- Minikube
- kubectl

---

## Project Structure

```bash
kubernetes_labs/
│
├── frontend/
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
│
├── backend/
│   ├── Dockerfile
│   ├── server.js
│   └── package.json
│
├── k8s/
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── backend-deployment.yaml
│   └── backend-service.yaml
│
└── README.md
```

---

## Prerequisites

Install the following tools:

- Docker Desktop
- Minikube
- kubectl

---

## Step 1 — Start Minikube

```bash
minikube start
```

Verify cluster:

```bash
kubectl get nodes
```

---

## Step 2 — Configure Docker Environment

Use Minikube Docker daemon:

```bash
eval $(minikube docker-env)
```

---

## Step 3 — Build Docker Images

Build frontend image:

```bash
docker build -t flask-frontend ./frontend
```

Build backend image:

```bash
docker build -t express-backend ./backend
```

Verify images:

```bash
docker images
```

---

## Step 4 — Deploy Kubernetes Resources

Apply all YAML files:

```bash
kubectl apply -f k8s/
```

---

## Step 5 — Verify Deployment

Check all resources:

```bash
kubectl get all
```

Check pods:

```bash
kubectl get pods
```

---

## Step 6 — Access Application

Open frontend service:

```bash
minikube service frontend-service
```

---

## Useful Commands

### Check Pods

```bash
kubectl get pods
```

### Check Services

```bash
kubectl get svc
```

### View Logs

```bash
kubectl logs <pod-name>
```

### Delete Resources

```bash
kubectl delete -f k8s/
```

### Stop Minikube

```bash
minikube stop
```

### Delete Minikube Cluster

```bash
minikube delete
```

---

## Output

- Flask frontend deployed successfully
- Express backend deployed successfully
- Kubernetes pods running
- Services exposed using Minikube

---

## Author

Rushikesh Dhule
