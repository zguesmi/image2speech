# WIP compile mimic for raspberry pi - ziedguesmi/mimic-tts-raspbian

FROM ziedguesmi/mimic-tts-raspbian

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"
LABEL version="1.0"

RUN [ "cross-build-start" ]

RUN apt-get update && apt-get install -y \
        libtesseract-dev \
        libsm6 \
        python3 \
        python3-pip \
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
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /iexec

COPY ./app /image2speech

RUN pip3 install pytesseract pillow PyYAML yamlordereddictloader

RUN [ "cross-build-end" ]

WORKDIR /mimic

ENTRYPOINT [ "/image2speech/docker-start" ]