# WiseCow Deployment

## Overview

This project demonstrates the deployment of a Dockerized application using Kubernetes (K8s) on an AWS EC2 instance. The application, known as WiseCow, displays a cow graphic and is containerized using Docker. The process includes setting up Docker, Kubernetes, and Git on an EC2 instance, creating and pushing a Docker image to DockerHub, and deploying the application with Kubernetes manifests.

## Prerequisites

1. **EC2 Instance**: Set up an EC2 instance on AWS.
2. **Software Requirements**: Ensure the following software is installed on the EC2 instance:
   - Docker
   - Git
   - Kubernetes CLI (`kubectl`)

## Installation and Configuration

### 1. Install Docker, Git, and Kubernetes

Follow the official installation guides for Docker, Git, and Kubernetes for your EC2 instance:

- [Install Docker](https://docs.docker.com/engine/install/)
- [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Install Kubernetes CLI (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

### 2. Clone the Repository

Clone the repository containing the WiseCow application and navigate into the directory:

```bash
git clone https://github.com/your-repo/wisecow.git
cd wisecow

```

### Run the WiseCow Script
Execute the wisecow.sh script to verify that the application runs correctly:
```bash
./wisecow.sh
```
### Kubernetes Deployment
#### 1. Apply Kubernetes Manifests
Deploy the application and expose it using Kubernetes by applying the manifests:

bash
Copy code
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
#### 2. GitHub Actions Deployment
The deployment process is automated using GitHub Actions. Ensure that your GitHub repository is configured with the necessary workflows for continuous integration and deployment (CI/CD).

#### Files
Dockerfile: Contains instructions for building the Docker image.
deployment.yaml: Kubernetes Deployment manifest for the WiseCow application.
service.yaml: Kubernetes Service manifest to expose the WiseCow application.
wisecow.sh: Script to verify local execution of the application.
