# My GCP App

GCP deployment workflow with Docker and CI/CD.

## Features
- Flask REST API
- Dockerized application
- Automated CI/CD pipeline
- Container registry integration

## Local Development
```bash
# Build
docker build -t my-web-app .

# Run
docker run -p 8080:8080 my-web-app

# Test
curl http://localhost:8080
```

## Endpoints
- `/` - Home
- `/health` - Health check
- `/info` - System info
- `/version` - Version info
