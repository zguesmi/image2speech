FROM ziedguesmi/mimic-tts:latest

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

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

RUN pip3 install -r /image2speech/requirements.txt

WORKDIR /mimic

ENTRYPOINT [ "/image2speech/docker-start" ]