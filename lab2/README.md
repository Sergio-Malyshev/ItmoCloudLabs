# лабораторная работа №2
---  
Плохие и хорошие Dockerfile  
## Плохой Dockerfile
```
FROM python:latest

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD python docker_lab.py
```
Что в нем плохого?
- Использован тег ```latest``` что может привести к ошибкам в будущем.
- Дважды использован ```RUN```, хотя эти действия можно выполнить с помощью одной командой.
- Используется CMD.
## Хороший Dockerfile
```
FROM python:3.9

WORKDIR /app

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "docker_lab.py"]
```
Что исправлено?
- Указана конктреная версия ```python```.
- Написан один ```RUN```.
- Используется ```ENTRYPOINT```, так как наш контейнер должен выполнять одну и ту же основную команду.
