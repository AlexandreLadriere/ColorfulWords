#!/usr/bin/env python3*
from Text import Text
from TextImage import TextImage

def main():
    textObj = Text(textPath="./droits_homme.txt")
    textObj.colors
    textImg = TextImage(textObj)
    textImg.save("./test", dimX=4000)

if __name__ == '__main__':
    main()
    