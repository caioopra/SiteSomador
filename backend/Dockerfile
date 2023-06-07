FROM python:3.11

WORKDIR /app/backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY server.py .

EXPOSE 8080

CMD ["python3", "server.py"]
