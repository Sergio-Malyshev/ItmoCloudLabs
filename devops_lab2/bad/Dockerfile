FROM python:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT python docker_lab.py
