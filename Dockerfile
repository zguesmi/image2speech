FROM ziedguesmi/mimic-tts:latest

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"
LABEL version="1.0"

COPY requirements.txt /image2speech/requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends \
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
    pip3 install -r /image2speech/requirements.txt  --no-cache-dir && \
    rm /image2speech/requirements.txt && \
    apt-get remove -y python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir /iexec

COPY ./app /image2speech

WORKDIR /mimic

ENTRYPOINT [ "/image2speech/entrypoint" ]