Go web application, along with container deployment and a `k6` script to test the application when scaled to 3 replicas.

### Running the App Locally and Pushing to Docker

1. **Build the Docker Image**:

   If using **Docker Desktop**'s built-in Kubernetes or Minikube, you can build the image locally and make it available to Kubernetes.

   ```bash
   docker build -t go-web-app:latest .
   ```

   If you're using Minikube, ensure Docker is pointing to Minikube's environment by running:

   ```bash
   eval $(minikube docker-env)
   ```

2. **Apply the Kubernetes Deployment and HPA**:

   Deploy the Go web app and the HPA in the local Kubernetes cluster:

   ```bash
   kubectl apply -f deployment.yaml
   ```

3. **Expose the Service**:

   Depending on your setup (Docker Desktop or Minikube), you can expose the service differently:

   - **Docker Desktop Kubernetes**: It will automatically expose the LoadBalancer service.
   - **Minikube**: Run this command to get the service's IP:

     ```bash
     minikube service go-web-app-service --url
     ```

### Steps to Run k6 Load Test

1. Install `k6`:
   ```bash
   # for macOS
   brew install k6
   ```
   
   ```
   # For Ubuntu
   sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
   echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
   sudo apt-get update
   sudo apt-get install k6
   ```

2. Replace `<your-service-ip>` with the actual URL (Docker Desktop LoadBalancer or Minikube service URL).

3. Run the test:

   ```bash
   k6 run test.js
   ```

### Monitoring Autoscaling

You can monitor the Horizontal Pod Autoscaler and the number of replicas by running:

```bash
kubectl get hpa
```

To check the number of replicas currently running:

```bash
kubectl get pods
```
