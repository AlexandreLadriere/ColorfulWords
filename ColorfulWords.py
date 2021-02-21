#!/usr/bin/env python3*
from Text import Text
from TextImage import TextImage

def main():
    textObj = Text(text="Le : petit Prince est le deuxième livre le plus traduit au monde Alexnadre.")
    print(textObj.colors)
    textImg = TextImage(textObj)
    print(textImg.text.colors)
    textImg.draw(1000)

if __name__ == '__main__':
    main()
    