FROM python:3.9

WORKDIR /app

COPY . /app

CMD ["python3.9", "main.py"]
