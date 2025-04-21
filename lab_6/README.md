# Kubernetes NFS HTTP Server Demo

This project sets up a basic web server in a Kubernetes cluster with a shared volume provided by a dynamically provisioned NFS server.

## 🔧 Requirements

- Docker
- [Kind](https://kind.sigs.k8s.io/) (Kubernetes in Docker)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/)
- (Optional for Windows) [Chocolatey](https://chocolatey.org/) to simplify installations

## 🛠️ Setup instructions

### 1. Install dependencies (Windows + Chocolatey)

```powershell
choco install kind
choco install kubernetes-helm
```

### 2. Create kind cluster

```powetshell
kind create cluster --name nfs-demo
```

### 3. Install NFS Server Provisioner using Helm

```powetshell
helm repo add kvaps https://kvaps.github.io/charts
helm repo update
helm install nfs-server kvaps/nfs-server-provisioner -f nfs-values.yaml
```


### 4. Apply kubernates resources

```powetshell
kubectl apply -f pvc.yaml
kubectl apply -f nginx-deployment.yaml
kubectl apply -f nginx-service.yaml
kubectl apply -f copy-content-job.yaml
```

### 5. Postforward and test
```powershell
kubectl port-forward svc/nginx-service 8080:80
```

Visit http://localhost:8080 to see the served content.