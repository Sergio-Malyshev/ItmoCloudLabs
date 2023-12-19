FROM python:3.9

WORKDIR /app
COPY devops_lab3/main.py .

ENTRYPOINT ["python", "main.py"]
