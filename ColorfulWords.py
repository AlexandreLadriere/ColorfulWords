#!/usr/bin/env python3*
from Text import Text
from TextImage import TextImage

def main():
    textObj = Text(text="Le petit prince est le deuxième livre le plus traduit au monde, après la Bible.")
    textImg = TextImage(textObj)
    textImg.save("./test")

if __name__ == '__main__':
    main()
    