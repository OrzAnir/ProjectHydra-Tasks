from fastapi import FastAPI
import requests
import time

app = FastAPI()

HYDRA_URL = "http://hydra-service:8000"

@app.get("/metrics")
def metrics():
    try:
        start = time.time()
        r = requests.get(f"{HYDRA_URL}/metrics", timeout=1)
        latency = (time.time() - start) * 1000
        data = r.json()

        return (
            f"hydra_cpu {data['cpu']}\n"
            f"hydra_latency_ms {latency}\n"
            f"hydra_up 1\n"
        )
    except:
        return "hydra_up 0\n"
