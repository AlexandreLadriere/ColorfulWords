#!/usr/bin/env python3*
import unicodedata

class Word:
    def __init__(self, text):
        self.text = text
        
    @property
    def color(self):
        alpha = "abcdefghijklmnopqrstuvwxyz" # alpha[1] = "b"
        alphaPos = dict([ (x[1],x[0]) for x in enumerate(alpha) ]) # alphaPos["b"] = 1
        colorValue = 0
        alphaText = ''.join(e for e in self.text if e.isalnum())
        alphaText = ''.join(c for c in unicodedata.normalize('NFD', alphaText)
                  if unicodedata.category(c) != 'Mn')
        for letter in alphaText:
            if letter.isdigit():
                colorValue += int(letter)
            else:
                colorValue += alphaPos[letter.lower()]
        return colorValue % 256