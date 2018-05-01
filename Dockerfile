FROM ubuntu:16.04

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

RUN apt-get update && apt-get install -y \
        # libsm6 \
        libtesseract-dev \
        # libxext6 \
        tesseract-ocr \
        tesseract-ocr-ara \
        tesseract-ocr-eng \
        tesseract-ocr-fra \
        tesseract-ocr-spa \
        tesseract-ocr-deu \
        tesseract-ocr-chi-sim \
        tesseract-ocr-ita \
        tesseract-ocr-jpn \
        tesseract-ocr-por \
        tesseract-ocr-rus \
        tesseract-ocr-tur \
        tesseract-ocr-kor \
        python3 \
        python3-pip \
        # python3-dev \     
        # libgtk2.0-bin \
        # libsm6 \
        # libxext6 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./app/ /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ['python3', 'app.py']