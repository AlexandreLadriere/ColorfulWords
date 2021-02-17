#!/usr/bin/env python3*
from Word import Word

class Text:
    
    # text: text String (optional)
    # textPath: Path of the .txt file (optional)
    # colors: List of pixel color value, where each value represent the color of a word
    
    def __init__(self, text="", textPath=""):
        self.text = text
        self.textPath = textPath
        if textPath != "":
            self.__loadText()
            
    def __loadText(self):
        pass
    
    @property
    def colors(self):
        colors = []
        splittedText = self.text.split(" ")
        for word in splittedText:
            currentWord = Word(word)
            if currentWord.formatedText != "": # Check if word is not a separate punctuation symbol for example
                colors.append(currentWord.color)
        return colors