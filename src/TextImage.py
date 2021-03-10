#!/usr/bin/env python3*
from PIL import Image, ImageDraw
from math import sqrt
from Text import Text

class TextImage:
    """
    Object representation of the image representation of a Text
    
    Parameters
    ----------
    text : str
        Text used for the image
    """
    
    def __init__(self, text):
        """
        Initialize a Textimage object with the given text
        
        Parameters
        ----------
        text : str
            text string
        """
        self.text = text
        
    def save(self, imagePath, imageName="", extension="png", dimX=2000):
        """
        Save the image object according to the given parameters
        
        Parameters
        ----------
        imagePath : str
            Path of the image, without image name
        imageName : str
            Name of the image, without extension
        extension : str
            Image format
        dimX : int
            Dimension, in pixels, of the side of the image
        """
        imgToSave = self.__draw(dimX)
        imgToSave.save(imagePath + imageName + "." + extension)
    
    def __draw(self, dimX):
        """
        Return an Image object  which is a representation of the object text
        
        Parameters
        ----------
        dimX : int
            Dimension, in pixels, of the side of the image
        """
        img = Image.new('RGB', (dimX, dimX), color='white')
        draw = ImageDraw.Draw(img)
        squareNumX = 0
        squareNumY = 0
        squareSize = self.__getSquareSideLength(dimX)
        borderRatio = squareSize / 10
        colorList = self.text.colors
        for color in colorList:
            upperLeftX = squareNumX * squareSize + borderRatio
            upperLeftY = squareNumY * squareSize + borderRatio
            lowerRightX = (squareNumX + 1) * squareSize - borderRatio
            lowerRightY = (squareNumY + 1) * squareSize - borderRatio
            draw.rectangle((upperLeftX, upperLeftY, lowerRightX, lowerRightY), fill=(color[0], color[1], color[2]))
            squareNumX += 1
            if squareNumX == self.__getGridSize():
                squareNumX = 0
                squareNumY += 1
        return img
            
    
    def __getGridSize(self):
        """
        Return the number of squares needed on each line/column
        """
        squareRoot = sqrt(len(self.text.colors))
        if squareRoot % 1 == 0:
            return squareRoot
        else:
            return int(squareRoot) + 1
        
    def __getSquareSideLength(self, dimX):
        """
        Return the size, in pixels, of each color square
        
        Parameters
        ----------
        dimX : int
            Dimension, in pixels, of the side of the image
        """
        return dimX / self.__getGridSize()
        