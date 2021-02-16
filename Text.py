#!/usr/bin/env python3*
from Word import Word

class Text:
    def __init__(self, text="", textPath=""):
        self.text = text
        self.textPath = textPath
        if textPath != "":
            self.__loadText()
            
    def __loadText(self):
        pass
    
    @property
    def colors(self):
        # split text
        # create Word object for each word
        # add word color to list
        colors = []
        splittedText = self.text.split(" ")
        for word in splittedText:
            # check if ponctuation
            print("word = " + word)
            currentWord = Word(word)
            colors.append(currentWord.color)
        return colors