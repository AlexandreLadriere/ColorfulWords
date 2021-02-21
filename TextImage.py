#!/usr/bin/env python3*
from PIL import Image, ImageDraw
from math import sqrt
from Text import Text

class TextImage:
    
    # text: Text used for the image
    
    def __init__(self, text):
        self.text = text
        
    def save(self, imagePath, imageName="", extension=".png", dimX=2000):
        imgToSave = self.__draw(dimX)
        imgToSave.save(imagePath + imageName + extension)
    
    def __draw(self, dimX):
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
        squareRoot = sqrt(len(self.text.colors))
        if squareRoot % 1 == 0:
            return squareRoot
        else:
            return int(squareRoot) + 1
        
    def __getSquareSideLength(self, dimX):
        return dimX / self.__getGridSize()
        