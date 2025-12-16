Steps to run:

cd docker-microservice-hydra
docker build -t hydra-service ./hydra-service
docker build -t prometheus-exporter ./prometheus-exporter
docker network create hydra-net
docker run -d --name hydra-service --network hydra-net -p 8000:8000 hydra-service
docker run -d --name prometheus-exporter --network hydra-net -p 9000:9000 prometheus-exporter
curl http://localhost:8000/health
curl http://localhost:9000/metrics
