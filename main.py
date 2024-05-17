import sys
from PIL import Image
from pathlib import Path
from random import randint
valid_images = [".jpg", ".jpeg", ".png"]


def get_images(location):
    images = []
    directory = Path(location)
    try:
        for file in directory.iterdir():
            ext = Path(file).suffix
            if file.is_file() and ext in valid_images:
                images.append(file)
    except FileNotFoundError as e:
        print(e)
        print("No such file exists")
        raise
    else:
        if len(images) != 0:
            return images


def show_image(images: list):
    try:
        length = len(images)
    except TypeError as e:
        print("no images in this location")
        raise
    else:
        index = randint(0, length - 1)
        image = Image.open(images[index])
        image.show()


def main():
    try:
        location = sys.argv[1]
    except IndexError as e:
        print(e)
        print("No location provided")
        raise
    else:
        images = get_images(location)
        show_image(images)


if __name__ == "__main__":
    main()

