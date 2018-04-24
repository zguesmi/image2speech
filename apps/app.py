from PIL import Image
import pytesseract
import argparse
import cv2
import os
import pyttsx3


def parseArgs():

    description = ''' my desc '''
    epilog = ''' the end '''
    argParser = argparse.ArgumentParser(description, epilog)
    argParser.add_argument('-i', '--image', required=True, help='path to input image')
    argParser.add_argument('-o', '--output', required=True, help='output format [text, speech]',
        choices=['text', 'speech'], default='', type=str)
    argParser.add_argument('-o', '--language', required=False, help='language of text [EN, FR, AR]',
        choices=['EN', 'FR', 'AR'], default='EN', type=str)
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


def imageToString(filename):
    ''' load image as PIL and return extracted text '''
    return pytesseract.image_to_string(Image.open(filename))


def textToSpeech(text):
    ''' convert text to speech '''
    engine = pyttsx3.init()
    engine.setProperty('rate', 200)
    # voices = engine.getProperty('voices')

    # TODO test on the language

    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex') # voices[0].id
    engine.say("this is alex's voice")
    engine.say("your text is")    
    engine.say(text)

    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.daniel') # voices[7].id
    engine.say("this is daniel's voice")
    engine.say("your text is")    
    engine.say(text)
    
    engine.runAndWait()


def main():

    args = parseArgs()
    image = preprocess(args['image'], args['preprocess'])

    # write the grayscale image to disk as a temporary file
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, image)

    text = imageToString(filename)
    print(text)

    os.remove(filename)

    if args['output'] == 'text': return text

    if args['output'] == 'speech': return textToSpeech(text, args['language'])


if __name__ == '__main__':
    main()