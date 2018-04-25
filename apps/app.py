import argparse
import cv2
import os
import sys
from PIL import Image
import pytesseract
import pyttsx3


def parseArgs():

    description = ''' my desc '''
    epilog = ''' the end '''
    argParser = argparse.ArgumentParser()
    argParser.add_argument('-i', '--image', required=True, help='Path to input image')
    argParser.add_argument('-o', '--output', required=True, help='Output format',
        choices=['text', 'speech'], type=str)
    argParser.add_argument('-l', '--language', required=False, help='Language (defaut is english)',
        choices=['eng', 'fra', 'ara'], default='eng', type=str)
    argParser.add_argument('-p', '--preprocess', required=False, help='type of preprocessing to be done',
        choices=['thresh', 'blur'], default='thresh', type=str)
    
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


def textToSpeech(text, language):
    ''' convert text to speech '''
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    # voices = engine.getProperty('voices')

    # TODO test on the language

    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel') # voices[7].id
    engine.say("this is daniel's voice")
    engine.say("your text is")    
    engine.say(text)
    engine.runAndWait()

    # TODO save the file and return it

    return 'tts'


def main():

    args = parseArgs()

    try:
        open(args['image']).close()
    except IOError as e:
        sys.exit(e)
    
    image = preprocess(args['image'], args['preprocess'])
    filename = saveTempFile(image)
    text = imageToString(filename, args['language'])
    print(text)

    try:
        os.remove(filename)
    except Exception as e:
        print('Warning: couldn\'t remove temporary file {}'.format(filename))

    if args['output'] == 'text': return text
    if args['output'] == 'speech': return textToSpeech(text, args['language'])


if __name__ == '__main__':
    main()