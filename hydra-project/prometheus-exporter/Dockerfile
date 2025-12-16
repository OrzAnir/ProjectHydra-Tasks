FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY exporter.py .

CMD ["uvicorn", "exporter:app", "--host", "0.0.0.0", "--port", "9000"]
