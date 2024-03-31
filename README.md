# Flask Demo App

A simple Flask application designed to demonstrate the deployment of containerized applications on Kubernetes using Helm.

For a detailed walkthrough on how this project was developed, refer to my [blog post](https://medium.com/@kishorchukka/deploying-flask-apps-with-kubernetes-docker-helm-a-comprehensive-guide-1719d4a055be) on Medium.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Deployment](#deployment)

## Overview

`flask-demo-app` is a basic web application built with Flask. It serves as a practical example for those looking to understand how to containerize applications with Docker and subsequently deploy them on a Kubernetes cluster using Helm.

## Prerequisites

- Python 3.8+
- Docker
- Kubernetes (optional for local testing)
- Helm (for Kubernetes deployment)

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/flask-demo-app.git
   cd flask-demo-app
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application Locally**:
   ```bash
   python app.py
   ```

5. **Testing**:
   ```bash
   pytest test_app.py
   coverage run -m pytest test_app.py
   coverage report -m
   coverage html
   ```
## Deployment

1. **Build the Docker Image**:
   ```bash
   docker build --build-arg PUBLIC_VARIABLE=<value> -t flask-demo-app:1.0.0 .
   docker run -d -p 5000:5000 -e SECRET_VARIABLE=<value> --name flask-demo-container flask-demo-app:1.0.0
   ```

2. **Deploying on Kubernetes with Helm**:
   Refer to the Helm chart in the `flask-demo-app-chart` directory and the associated documentation for deployment instructions.


## Reference 

1. [Python Flask Docker Hello World](https://github.com/shekhargulati/python-flask-docker-hello-world/tree/master)
2. [Deploying a Flask App to Kubernetes](https://medium.com/featurepreneur/deploying-a-flask-app-to-kubernetes-f05c93866aff)
3. [Sample Flask with Kubernetes](https://github.com/ginomempin/sample-flask-with-kubernetes)
4. [Deploy Flask App on Kubernetes](https://dev.to/yogendra_tamang/deploy-flask-app-on-kubernetes-2-17pb)
5. [Deploy a Python To-Do App with Flask, Kubernetes, and CockroachCloud](https://www.cockroachlabs.com/docs/cockroachcloud/deploy-a-python-to-do-app-with-flask-kubernetes-and-cockroachcloud)
6. [Write Helm Charts for Python Flask App](https://augustasberneckas.medium.com/write-helm-charts-for-python-flask-app-ee2777fb458c)
7. [Flask Kubernetes Helm](https://github.com/mrasap/flask-kubernetes-helm)
8. [Deploying Flask Apps with Kubernetes, Docker, Helm: A Comprehensive Guide](https://medium.com/@kishorchukka/deploying-flask-apps-with-kubernetes-docker-helm-a-comprehensive-guide-1719d4a055be)
9. [Flask Demo App GitHub Repository](https://github.com/kishorechk/flask-demo-app/blob/main/app.py)

Originally picked up from [Flask Demo App README](https://github.com/kishorechk/flask-demo-app/blob/main/README.md)

