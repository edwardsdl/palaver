import re

import pytesseract
from PIL import Image


def get_access_code(image_path):
    image = Image.open(image_path)
    image = image.convert('L')
    text = pytesseract.image_to_string(image)
    match = re.search('(\d{4}).(\d{4}).(\d{4}).(\d{5}).(\d{8})', text)

    if match is not None:
        return '-'.join(match.groups())
