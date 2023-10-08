FROM python:3.10.13-alpine3.18

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "src/__init__.py"]