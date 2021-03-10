#!/usr/bin/env python3*
from Word import Word

class Text:
    """
    Object representation for a text
    
    Parameters
    ----------
    text : str
        text String (optional)
    textPath : str
        Path of the .txt file (optional)
    colors : List of integers lists
        List of pixel color value in rgb, eg: [[123, 0, 23], [34, 78, 234]]
    """
   
    def __init__(self, text="", textPath=""):
        """
        Initialize the Text object with a given text string or a given path to txt file
        
        Parameters
        ----------
        text : str 
            Text String (optional)
        textPath : str
            Path of the .txt file (optional)
        """
        self.text = text
        self.textPath = textPath
        if textPath != "":
            self.__loadText(textPath)
            
    def __loadText(self, textPath):
        """
        Load the content of the txt file in the class parameter "text".
        Nothing happen if the given path is not a txt file
        
        Parameters
        textPath : str
            Path of the .txt file (optional)
        ----------
        """
        if textPath.endswith(".txt"):
            with open(textPath, 'r') as f:
                fileText = f.read()
                fileText = fileText.replace("\n", " ")
                fileText = fileText.replace("\r", " ")
                self.text = fileText
        return        
    
    @property
    def colors(self):
        """
        Return a list a color (RGB values) where each color (ie each RGB triplet) represent a word
        """
        colors = []
        splittedText = self.text.split(" ")
        for word in splittedText:
            currentWord = Word(word)
            if currentWord.formatedText != "": # Check if word is not a separate punctuation symbol for example
                colors.append(currentWord.color)
        return colors