import argparse
import cv2
import os
import sys
import subprocess
from PIL import Image
import pytesseract



class OCR:

    def preprocess(self, image, method):
        ''' load image with opencv, convert it to grayscale and apply preprocessing '''
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if method == 'thresh':
            return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

        if method == 'blur':
            return cv2.medianBlur(image, 3)

    def imageToString(self, image, lang):
        ''' load image as PIL and return extracted text '''
        try:
            return pytesseract.image_to_string(image, lang=lang)
        except Exception as e:
            sys.exit(e)


class Speech:
    
    ENG_VOICES = {
        'default': 'daniel.premium',
        'daniel': 'daniel.premium',
        'alex': 'Alex',
        'karen': 'karen',
        'moira': 'moira'
    }

    ESP_VOICES = {
        'default': 'jorge',
        'jorge': 'jorge',
        'paulina': 'paulina'
    }

    ARA_VOICES = {
        'default': 'maged',
        'maged': 'maged'
    }

    FRA_VOICES = {
        'default': 'thomas',
        'thomas': 'thomas',
        'amelie': 'amelie'
    }
    
    LANGUAGES = {
        'eng': ENG_VOICES,
        'esp': ESP_VOICES,
        'ara': ARA_VOICES,
        'fra': FRA_VOICES
    }


    def matchLanguageVoice(self, lang, voice):
        BASE_VOICE_URI = 'com.apple.speech.synthesis.voice.'
        if not voice in self.LANGUAGES[lang]: voice = 'default'
        return BASE_VOICE_URI + self.LANGUAGES[lang][voice]
    
    def textToSpeech(self, text):
        subprocess.call(["espeak", "-w", "speech", text])


class App:

    # args
    # text

    def __init__(self):
        self.parseArgs()
        if not os.path.isfile(self.args['image']): sys.exit('No such file or directory: {}'.format(self.args['image']))
        self.image = cv2.imread(self.args['image'])

    def parseArgs(self):

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
        
        self.args = vars(argParser.parse_args())

    def extractText(self):
        ocr = OCR()
        self.image = ocr.preprocess(image=self.image, method=self.args['preprocess'])
        self.text = ocr.imageToString(self.image, self.args['language'])

    def main(self):
        
        self.extractText()

        print(self.text.encode('utf-8').strip())
        print('*******************')

        if self.args['output'] == 'text': return self.text

        if self.args['output'] == 'speech':
            speech = Speech()
            # voiceId = speech.matchLanguageVoice(self.args['language'], self.args['voice'])
            speech.textToSpeech(self.text)
    

if __name__ == '__main__':
    App().main()