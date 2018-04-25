import argparse
import cv2
import os
import sys
from PIL import Image
import pytesseract
import pyttsx3


ENG_VOICES = {
    'default': 'com.apple.speech.synthesis.voice.daniel.premium',
    'daniel': 'com.apple.speech.synthesis.voice.daniel.premium',
    'alex': 'com.apple.speech.synthesis.voice.Alex',
    'karen': 'com.apple.speech.synthesis.voice.karen',
    'moira': 'com.apple.speech.synthesis.voice.moira'
}

ESP_VOICES = {
    'default': 'com.apple.speech.synthesis.voice.jorge',
    'jorge': 'com.apple.speech.synthesis.voice.jorge',
    'paulina': 'com.apple.speech.synthesis.voice.paulina'
}

ARA_VOICES = {
    'default': 'com.apple.speech.synthesis.voice.maged',
    'maged': 'com.apple.speech.synthesis.voice.maged'
}

FRA_VOICES = {
    'default': 'com.apple.speech.synthesis.voice.thomas',
    'thomas': 'com.apple.speech.synthesis.voice.thomas',
    'amelie': 'com.apple.speech.synthesis.voice.amelie'
}

LANGUAGES = {
    'eng': ENG_VOICES,
    'esp': ESP_VOICES,
    'ara': ARA_VOICES,
    'fra': FRA_VOICES
}

def parseArgs():

    argParser = argparse.ArgumentParser()
    argParser.add_argument('-i', '--image', required=True, help='Path to input image', type=str)
    argParser.add_argument('-o', '--output', required=True, help='Output format', type=str,
        choices=['text', 'speech'])
    argParser.add_argument('-l', '--language', required=True, help='Text\'s language', type=str,
        choices=['eng', 'esp', 'ara', 'fra'])
    argParser.add_argument('-v', '--voice', required=False, help='Voice id', type=str,
        choices=['daniel', 'alex', 'karen', 'moira', 'jorge', 'paulina', 'maged', 'thomas', 'amelie'], default='default')
    argParser.add_argument('-p', '--preprocess', required=False, help='Type of preprocessing', type=str,
        choices=['thresh', 'blur'], default='thresh')
    
    return vars(argParser.parse_args())


def preprocess(image, preprocessMethod):
    ''' load image with opencv, convert it to grayscale and apply preprocessing '''
    
    img = cv2.cvtColor(cv2.imread(image), cv2.COLOR_BGR2GRAY)

    if preprocessMethod == 'thresh':
        return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    if preprocessMethod == 'blur':
        return cv2.medianBlur(img, 3)


def saveTempFile(image):
    '''' write the grayscale image to disk as a temporary file '''
    filename = "{}.png".format(os.getpid())
    try:
        cv2.imwrite(filename, image)
        return filename
    except Exception as e:
        sys.exit(e)


def imageToString(filename, lang):
    ''' load image as PIL and return extracted text '''
    try:
        return pytesseract.image_to_string(Image.open(filename), lang=lang)
    except Exception as e:
        sys.exit(e)


def matchLanguageVoice(lang, voice):
    if not voice in LANGUAGES[lang]: voice = 'default'
    return LANGUAGES[lang][voice]


def textToSpeech(text, voiceId):
    ''' convert text to speech '''
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    engine.setProperty('voice', voiceId)
    engine.say(text)
    engine.runAndWait()

    # TODO save the file and return it

    return 'tts'


def main():

    args = parseArgs()

    if not os.path.isfile(args['image']): sys.exit('No such file or directory: {}'.format(args['image']))
    
    image = preprocess(args['image'], args['preprocess'])
    filename = saveTempFile(image)
    text = imageToString(filename, args['language'])
    print(text)

    try:
        os.remove(filename)
    except Exception as e:
        print('Warning: couldn\'t remove temporary file {}'.format(filename))

    if args['output'] == 'text': return text
    if args['output'] == 'speech': return textToSpeech(text, matchLanguageVoice(args['language'], args['voice']))


if __name__ == '__main__':
    main()