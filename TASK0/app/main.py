from flask import Flask

app = Flask(__name__)

@app.get("/health")
def health_check():
    return "OK"

@app.get("/")
def home():
    return "The app is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
