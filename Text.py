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
            self.__loadText(textPath)
            
    def __loadText(self, textPath):
        if textPath.endswith(".txt"):
            with open(textPath, 'r') as f:
                fileText = f.read()
                fileText = fileText.replace("\n", " ")
                fileText = fileText.replace("\r", " ")
                self.text = fileText
        return        
    
    @property
    def colors(self):
        colors = []
        splittedText = self.text.split(" ")
        for word in splittedText:
            currentWord = Word(word)
            if currentWord.formatedText != "": # Check if word is not a separate punctuation symbol for example
                colors.append(currentWord.color)
        return colors