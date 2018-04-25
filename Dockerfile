FROM ubuntu:16.04

LABEL maintainer="Zied Guesmi <guesmy.zied@gmail.com>"

RUN apt-get update && apt-get install -y \
        tesseract-ocr \
        libtesseract-dev \
        tesseract-ocr-eng \
        tesseract-ocr-ara \
        tesseract-ocr-fra \
        python3-pip \
        python3-dev \
        # libgtk2.0-bin \
        # libsm6 \
        # libxext6 \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


ENTRYPOINT ["bash"]
