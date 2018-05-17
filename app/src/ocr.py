import pytesseract
import cv2

import custom_exceptions as customExceptions


class OCR:

    '''
    this class preprocesses and image and uses tesseract ocr to extract text it
    '''

    LANGUAGES = {
        None: None,
        'en': 'eng',        # english
        'fr': 'fra',        # frensh
        'es': 'spa',        # Spanish
        'ar': 'ara',        # arabic
        'de': 'deu',        # German
        'zh': 'chi_sim',    # chinese
        'it': 'ita',        # Italian
        'ja': 'jpn',        # Japanese 
        'pt': 'por',        # Portuguese
        'ru': 'rus',        # russian
        'tr': 'tur',        # turkish
        'ko': 'kor',         # Korean
    }

    def _preprocess(self, image):
        ''' convert image to grayscale and apply threshold preprocessing '''
        try:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            return cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        except Exception:
            return image

    def _matchLanguage(self, lang):
        return self.LANGUAGES[lang]


    def imageToString(self, path, lang):
        image = self._preprocess(image=cv2.imread(path))
        try:
            return pytesseract.image_to_string(image, lang=self._matchLanguage(lang)).encode()
        except KeyError:
            raise customExceptions.UnsupportedLanguageError(lang)
        except Exception as e:
            raise customExceptions.CanNotExtractTextError(e, path)

