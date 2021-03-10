#!/usr/bin/env python3.9
import argparse
from Text import Text
from TextImage import TextImage

def main(text_path, text_string, image_path, image_name, image_format, image_size):
    if text_path != '':
        textObj = Text(textPath=text_path)
    else:
        textObj = Text(text=text_string)
    textObj.colors
    textImg = TextImage(textObj)
    textImg.save(image_path, imageName=image_name, extension=image_format, dimX=image_size)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog = 'Colorful Words',
                                     description = 'Create an image reppresentation of a text. Each color represents a word')
    parser.add_argument('-tp',
                        '--text_path',
                        type=str,
                        required=False,
                        default='',
                        help='Path (str) of the txt file')
    parser.add_argument('-ts',
                        '--text_string',
                        type=str,
                        required=False,
                        default='',
                        help='Text (str) that you want to use')
    parser.add_argument('-ip',
                        '--image_path',
                        type=str,
                        required=True,
                        help='Path (str) of the folder where you want to save the image')
    parser.add_argument('-in',
                        '--image_name',
                        type=str,
                        required=False,
                        default='image',
                        help='Name (str) of the image you want to create')
    parser.add_argument('-if',
                        '--image_format',
                        type=str,
                        required=False,
                        default='png',
                        help='Format (str) of the image you want to save')
    parser.add_argument('-is',
                        '--image_size',
                        type=int,
                        required=False,
                        default=2000,
                        help='Size (int) in pixels of the image you want to save')
    args = parser.parse_args()
    main(args.text_path, args.text_string, args.image_path, args.image_name, args.image_format, args.image_size)
    