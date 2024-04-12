# lcbo-ingester-bridge
Python application that ingests extracted data from LCBO and produce related events for further usage.

## Run

set environment variables in `.env` file: `cp .env.example .env`

You can run either directly on Docker or deploy to Kubernetes using Kind.

### Docker

```
docker-compose up
```

### KinD
Use Kind to run a multi-node Kubernetes Cluster. Create a yaml file with the following content:
```
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
- role: worker
- role: worker
- role: worker
```
Run this command to create the cluster:
```
kind create cluster --config kind-example-config.yaml
```
To deploy and run lcbo-ingester-bridge on Kubernetes on your local system:
```
cd nfs
docker build -t nfs-storage .
cd ..
kind load docker-image nfs-storage:latest
kubectl apply -f charts/storage

docker build -t lcbo-ingester-bridge .
kind load docker-image lcbo-ingester-bridge:latest
kubectl apply -f charts/templates
```
Clean Up
```
kubectl delete -f charts/templates
kubectl delete -f charts/storage
```

