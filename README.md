# Image-to-speech-Dapp

![dapp logo](./logo.svg)


## Description
This dapp applies [tesseract-OCR](https://github.com/tesseract-ocr/tesseract) on images to extract text and convert it to speech.  

## Usage
    # Help
    $ python3 app.py -h

    # Extract text without converting it to speech
    $ python3 app.py -i path/to/image -o text -l eng

    # Extract text and convert it to speech
    $ python3 app.py -i path/to/image -o speech -l eng

    # Change speech voice
    $ python3 app.py -i path/to/image -o speech -l fra -v moira

## Supported languages
#### English
Symbol: eng  
Voices: daniel (default), alex, karen, moira.
#### Spanish
Symbol: esp  
Voices: jorge (default), paulina.
#### Arabic
Symbol: ara  
Voices: maged (default).
#### Frensh
Symbol: fra  
Voices: thomas (default), amelie.

## Dependencies
python3  
[tesseract-ocr](https://github.com/tesseract-ocr/tesseract)  
[pyttsx3](https://pypi.org/project/pyttsx3/2.5/)  
[opencv](https://opencv.org/)

## Docker installation
For easier installation check [this](./docker)

## Native installation
Install system dependencies:

    $ apt-get update && apt-get install -y \
        tesseract-ocr \
        libtesseract-dev \
        tesseract-ocr-ara \
        tesseract-ocr-eng \
        tesseract-ocr-fra \
        tesseract-ocr-spa \
        python3 \
        python3-pip
        
Install python depedencies:

    $ cd app
    $ pip3 install -r requirements.txt