#!/usr/bin/env python3*
from Word import Word

class Text:
    
    # text: text String (optional)
    # textPath: Path of the .txt file (optional)
    # colors: List of pixel color value in rgb, eg: [[123, 0, 23], [34, 78, 234]]
    
    def __init__(self, text="", textPath=""):
        self.text = text
        self.textPath = textPath
        if textPath != "":
            self.__loadText()
            
    def __loadText(self):
        pass
    
    def saveTextToImage(self, imagePath, extension=".png", dimX="2000", dimY="2000"):
        pass
    
    @property
    def colors(self):
        colors = []
        splittedText = self.text.split(" ")
        for word in splittedText:
            currentWord = Word(word)
            if currentWord.formatedText != "": # Check if word is not a separate punctuation symbol for example
                colors.append([currentWord.color, currentWord.color, currentWord.color])
        return colors