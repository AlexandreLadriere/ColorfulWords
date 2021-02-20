#!/usr/bin/env python3*
from math import sqrt
from Text import Text

class TextImage:
    
    # text: Text used for the image
    
    def __init__(self, text):
        self.text = text
        
        
    def save(self, imagePath, extension=".png", dimX="2000", dimY="2000"):
        pass
    
    def draw(self, dimX, dimY):
        pass            
    
    def __getSquareSideLength(self, gridDimX, gridDimY):
        totalArea = gridDimX * gridDimY
        squareArea = totalArea / len(self.text.color) # Single square area (px) = totalArea (px) / number of colors
        return sqrt(squareArea)
    
    def __getNumberOfSquaresPerRow(self, gridDimX, gridDimY):
        return gridDimX / self.__getSquareSideLength(gridDimX, gridDimY)