# лабораторная работа №2
---  
Плохие и хорошие Dockerfile  
## Плохой Dockerfile
\'''
FROM python:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD python docker_lab.py
\'''
