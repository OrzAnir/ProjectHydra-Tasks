from flask import Flask, Response
import random
import time
import psutil
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('api_requests_total', 'Total API Requests')
REQUEST_LATENCY = Histogram('api_response_time_seconds', 'API response time')

price = 100.0

@app.route("/")
def home():
    return """
STOCK MONITORING SERVICE

Available endpoints:
- /stock   → current stock price
- /metrics → Prometheus metrics
"""

@app.route("/stock")
def stock():
    global price
    REQUEST_COUNT.inc()

    with REQUEST_LATENCY.time():
        change = random.uniform(-1, 1)
        price += change
        return f"""
Stock: DEMO
Price: {price:.2f}
Change: {change:+.2f}
"""

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

