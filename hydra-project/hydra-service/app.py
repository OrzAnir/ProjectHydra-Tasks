from fastapi import FastAPI, Response
import random

app = FastAPI()

@app.get("/health")
def health():
    return "OK"

@app.get("/metrics")
def metrics():
    return {
        "cpu": random.uniform(10, 90),
        "latency_ms": random.uniform(50, 300)
    }

@app.get("/simulate_failure")
def failure(response: Response):
    response.status_code = 500
    return {"status": "failure"}

