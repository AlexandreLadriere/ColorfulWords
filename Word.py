#!/usr/bin/env python3*
import unicodedata

class Word:
    
    # text: word text
    # formatedText: word text without accent, punctuation, etc
    # color: pixel color values in rgb for the word - eg: [0, 255, 56]
    
    def __init__(self, text):
        self.text = text
        self.formatedText = self.__formatText()
        
    @property
    def color(self):
        alpha = "abcdefghijklmnopqrstuvwxyz" # alpha[1] = "b"
        alphaPos = dict([ (x[1],x[0]) for x in enumerate(alpha) ]) # alphaPos["b"] = 1
        colorValue = 0
        for letter in self.formatedText:
            if letter.isdigit():
                colorValue += int(letter)
            else:
                colorValue += alphaPos[letter.lower()]
        return [(colorValue * len(self.formatedText)) % 256, (colorValue * 2) % 256, (colorValue * 3 % 256)]
    
    def __formatText(self):
        uniText = ''.join(e for e in self.text if e.isalnum()) # remove punctuation
        uniText = ''.join(c for c in unicodedata.normalize('NFD', uniText)
                  if unicodedata.category(c) != 'Mn') # Remove accents and other special letter chars
        uniText = uniText.replace("œ", "oe")
        uniText = uniText.replace("ª", "a")
        return uniText