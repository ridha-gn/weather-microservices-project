Weather Microservices Project
A full DevOps pipeline implementation featuring microservices architecture with Kubernetes orchestration, containerization, and automated deployments.

Project Overview
This project demonstrates a complete production-ready weather application built with microservices architecture. The system consists of two main services:

weather-api: FastAPI backend service for weather data

weather-frontend: Flask frontend application for user interface

The project showcases end-to-end DevOps practices from code to production deployment with full HTTPS/SSL security.

Architecture
Microservices: FastAPI backend + Flask frontend

Containerization: Docker-based container deployment

Orchestration: Kubernetes (K3s) on Azure VM

Networking: Proper service discovery and load balancing

Security: HTTPS with SSL certificates and secure configurations

CI/CD: Jenkins pipeline for automated deployments

Technical Stack
Container Orchestration: Kubernetes (K3s)

Containerization: Docker

Web Servers: NGINX/Traefik for ingress and load balancing

SSL Management: cert-manager with Let's Encrypt

DNS: Custom domain (ridha-weather.duckdns.org)

Cloud Platform: Azure Cloud VM

CI/CD: Jenkins pipeline automation

Architecture: Microservices distributed system

Project Structure

weather-project/
├── docker-compose.yml
├── weather-api/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── weather-frontend/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── k8s/
    ├── cluster-issuer.yaml
    ├── ingress-https.yaml
    ├── ingress-traefik-fixed.yaml
    ├── loadbalancer-services.yaml
    ├── weather-api.yaml
    ├── weather-frontend.yaml
    ├── ingress-final.yaml
    ├── ingress-self-signed.yaml
    ├── ingress.yaml
    └── self-signed-issuer.yaml
Features Implemented
Auto-scaling microservices architecture

HTTPS with automatic SSL certificate renewal

Blue-green deployment capability

Health checks and monitoring readiness

Zero-downtime deployment strategies

Secure container registry integration

Production-grade ingress configuration

DNS management and custom domain routing

Project Status
Note: This project was discontinued due to Azure platform restrictions. The Azure for Students subscription identified this as an advanced project requiring standard subscription tiers, resulting in VM access being blocked. The implementation was fully functional with all components successfully deployed and accessible via the custom domain before the restriction was applied.

Skills Demonstrated
Cloud infrastructure provisioning and management

Container orchestration at scale

CI/CD pipeline design and implementation

SSL/TLS security configuration

Microservices architecture design

Production deployment strategies

DNS configuration and management

Automated certificate management

Getting Started
To run this project locally or in your own environment:

Clone the repository

Set up Docker and Kubernetes environment

Configure your DNS settings

Update configuration files with your domain

Deploy using the provided Kubernetes manifests

License
This project is for educational and demonstration purposes.
