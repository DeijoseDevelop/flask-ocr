import pytesseract
import re
from spellchecker import SpellChecker
from langdetect import detect


class ProccessText(object):

    def __init__(self, text: str):
        self.text = text
        self.spell_checker = SpellChecker(language=detect(text))

    def clean_text(self):
        self.text = re.sub(r'[^a-zA-Z\s]', '', self.text)
        return self

    def normalize_text(self):
        self.text = ' '.join(self.text.lower().split())
        return self

    def spelling_correction(self):
        words = self.text.split()
        corrected_words = []
        for word in words:
            corrected_word = self.spell_checker.correction(word)
            if corrected_word is not None:
                corrected_words.append(corrected_word)
            else:
                corrected_words.append(word)
        self.text = ' '.join(corrected_words)
        return self



