FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ ./app/
COPY sample_docs/ ./sample_docs/
COPY persona_task.json ./persona_task.json
CMD ["python", "app/main.py"]
