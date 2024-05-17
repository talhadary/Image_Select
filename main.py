import sys
from PIL import Image
from pathlib import Path
from random import randint


def getimages(location):
    image = []
    validimages = [".jpg", ".jpeg", ".png"]
    p = Path(location)
    try:
        for x in p.iterdir():
            ext = Path(x).suffix
            if x.is_file() and ext in validimages:
                image.append(x)
    except FileNotFoundError as e:
        print(e)
        print("No such file exists")
        sys.exit()
    except Exception as e:
        print(e)
        print("There was a problem")
        sys.exit()
    else:
        if len(image) != 0:
            return image


def showimage(img: list):
    try:
        length = len(img)
    except TypeError as e:
        print(e)
        print("no images in this location")
        sys.exit()
    else:
        index = randint(0, length - 1)
        image = Image.open(img[index])
        image.show()


if __name__ == "__main__":
    try:
        location = sys.argv[1]
    except IndexError as e:
        print(e)
        print("No location provided")
        sys.exit()
    else:
        img = getimages(location)
        showimage(img)

