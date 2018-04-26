FROM ubuntu:16.04

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

RUN apt-get update && apt-get install -y \
        espeak \
        libsm6 \
        libtesseract-dev \
        libxext6 \
        tesseract-ocr \
        tesseract-ocr-ara \
        tesseract-ocr-eng \
        tesseract-ocr-fra \
        tesseract-ocr-spa \
        python3 \
        # python3-dev \     
        python3-pip \
        # libgtk2.0-bin \
        # libsm6 \
        # libxext6 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./app/ /app/

WORKDIR /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["bash"]
