FROM python:3.9-slim
RUN apt-get update \
    && apt-get install tesseract-ocr -y \
    && apt-get install tesseract-ocr-spa -y



COPY main.py ./web.py
COPY requirements.txt ./requirements.txt
COPY ./images ./images

RUN pip3 install -r requirements.txt

ENTRYPOINT FLASK_APP=./web.py flask run --host=0.0.0.0 --port=8080