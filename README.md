# Random Forest Regression Project

This project demonstrates the use of a **Random Forest Algorithm** for regression tasks. It also includes deployment using **Docker** and **Kubernetes** while providing real-time monitoring with **Prometheus** and **Grafana**.

---

## Features

- Implementation of a **Random Forest Algorithm** for regression.
- Deployment containerized with **Docker** and orchestrated with **Kubernetes**.
- Monitoring and observability integrated with **Prometheus** and **Grafana**.

---

## Prerequisites

- Docker installed on your system.
- Kubernetes cluster set up (e.g., Minikube, k3s, or any cloud provider).
- Prometheus and Grafana setup for monitoring.

---

## Setup and Usage

### Step 1: Clone the Repository

Clone this project to your local machine using the following command:

```bash
git clone https://github.com/firass99/ML-Pipeline.git
cd ML-Pipeline
```
### Step 2: Build and Run with Docker

#### Build the Docker image

Use the following command to build the Docker image:

```bash
docker build -t random-forest-app .
```

#### Run the container

Run the application in a Docker container:

```bash
docker run -p 5000:5000 random-forest-app
```

Access the application locally at `http://localhost:5000`.

---

### Step 3: Deploy with Kubernetes

#### Apply Kubernetes Deployment

Deploy the application to your Kubernetes cluster:

```bash
kubectl apply -f k8s/deployment.yaml
```

#### Verify Pods

Ensure the pods are running:

```bash
kubectl get pods
```

#### Expose the Service

Expose the application as a service to access it through the cluster’s IP.

---

### Step 4: Set Up Monitoring with Prometheus and Grafana

#### Install Prometheus and Grafana

Install Prometheus and Grafana in your Kubernetes cluster using Helm:

```bash
helm install prometheus prometheus-community/prometheus
helm install grafana grafana/grafana
```

#### Configure Prometheus

Set up Prometheus to scrape metrics from the application. Update the `prometheus.yaml` file in your configuration with the appropriate endpoints.

#### Visualize Metrics in Grafana

- Log in to Grafana and add Prometheus as a data source.
- Import or create a dashboard to monitor the application metrics.

---

## Monitoring Dashboard Example

- **Prometheus**: Provides real-time metrics collection.
- **Grafana**: Displays insightful dashboards for monitoring system health.

---

## Contributing

Feel free to submit issues or create pull requests for improvements. Contributions are welcome!

---

## Contact

For questions or feedback, contact [firassebai.fs.com](mailto:your-email@example.com).

