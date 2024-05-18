import random
import sys
from PIL import Image
from pathlib import Path

VALID_IMAGES = [".jpg", ".jpeg", ".png"]


def get_images(location: str) -> list:
    images = []
    directory = Path(location)
    try:
        for file in directory.iterdir():
            ext = Path(file).suffix
            if file.is_file() and ext in VALID_IMAGES:
                images.append(file)
    except FileNotFoundError:
        print("No such file exists")
        raise
    finally:
        return images


def show_image(images: list) -> None:
    if len(images) == 0:
        print("No images at this location!")
    else:
        choice = random.choice(images)
        image = Image.open(choice)
        image.show()


def get_path() -> str:
    try:
        location = sys.argv[1]
    except IndexError:
        print("No location provided")
        raise
    else:
        return location


def main() -> None:
    location = get_path()
    images = get_images(location)
    show_image(images)


if __name__ == "__main__":
    main()
