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

```
docker build -t lcbo-ingester-bridge .
kind load docker-image lcbo-ingester-bridge:latest
kubectl apply -f charts/templates


kubectl delete -f charts/templates
```

