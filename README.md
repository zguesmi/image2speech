# Image-to-speech-Dapp

![dapp logo](./logo.svg)


## Description
This dapp applies ![tesseract-OCR](https://github.com/tesseract-ocr/tesseract) on images to extract text and convert it to speech  
Image ---(tesseract)---> Text ---(pyttsx)---> sound

## Usage
    # Help
    $ python3 app.py -h

    # Extract text without converting it to speech
    $ python3 app.py -i path/to/image -o text

    # Extract text and convert it to speech
    $ python3 app.py -i path/to/image -o speech

    # Extract frensh text and convert it to speech
    $ python3 app.py -i path/to/image -o speech -l fra

## Supported languages
English - eng (default)  
Frensh - fra  
Arabic - ara  

To change the language use the -l (--language) option

## Dependencies
    python3
    ![tesseract-ocr](https://github.com/tesseract-ocr/tesseract)
    ![pyttsx3](https://pypi.org/project/pyttsx3/2.5/)
    ![opencv](https://opencv.org/)

## Docker installation
For easier installation check ![this](./docker)

## Native installation
Install system dependencies:

    $ apt-get update && apt-get install -y \
        tesseract-ocr \
        libtesseract-dev \
        tesseract-ocr-eng \
        tesseract-ocr-ara \
        tesseract-ocr-fra \
        python3 \
        python3-pip \
        python3-dev

Install python depedencies

    $ pip3 install -r requirements.txt