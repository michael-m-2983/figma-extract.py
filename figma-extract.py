#!/bin/python3

"""
figma-extract.py

A tool for extracting metadata and thumbnail images from Figma .fig files.

Usage
    pip install pygame # Ensure that pygame is installed

    python figma-extract.py --help # Print the help message

    python figma-extract.py <PATH TO .FIG FILE> # Display a popup with information about a .fig file
"""

import sys
import zipfile
import io
import json
from argparse import ArgumentParser

def load_figma_file(file_path: str):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        thumbnail = None
        with zip_ref.open("thumbnail.png") as image_file:
            thumbnail = image_file.read()
        
        metadata = None
        with zip_ref.open("meta.json") as meta_file:
            metadata = json.load(meta_file)

        return (thumbnail, metadata)


argparser = ArgumentParser()
argparser.add_argument("file", help="Path to the .fig file")
argparser.add_argument("-m", "--metadata", help="Extract JSON metadata to the specified path")
argparser.add_argument("-t", "--thumbnail", help="Extract PNG thumbnail to the specified path")
args = argparser.parse_args()

thumbnail, metadata = load_figma_file(args.file)

if args.metadata:
    with open(args.metadata, "w") as fp:
        json.dump(metadata, fp)
    sys.exit(0)

if args.thumbnail:
    with open(args.thumbnail, "wb") as fp:
        fp.write(thumbnail)
    sys.exit(0)

###################################################
# The rest of this script is for the GUI display. #
###################################################

# disable the default pygame message to simplify UX
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

pygame.init()

width, height = 600, 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Figma Display: " + args.file)


font = pygame.font.Font(None, 25)

create_text_surface = lambda text : font.render(text, True, (236, 239, 244))

fileName = create_text_surface(f"File Name: {metadata['file_name']}")

size_obj = metadata['client_meta']['thumbnail_size']
size = create_text_surface(f"Thumbnail Size: {size_obj['width']}x{size_obj['height']}")

thumbnail_size = (200 * width // size_obj['width'], 200 * height // size_obj['height'])
thumbnail_image = pygame.image.load(io.BytesIO(thumbnail))
thumbnail_image = pygame.transform.scale(thumbnail_image, thumbnail_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((46, 52, 64))

    screen.blit(thumbnail_image, (20, (height - thumbnail_size[1]) // 2))

    screen.blit(fileName, (thumbnail_size[0] + 40, (height - thumbnail_size[1]) // 2))
    screen.blit(size, (thumbnail_size[0] + 40, 2 * fileName.get_height() + (height - thumbnail_size[1]) // 2))

    pygame.display.flip()

pygame.quit()
sys.exit()
