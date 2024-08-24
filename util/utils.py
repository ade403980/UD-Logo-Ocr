
from PIL import Image
import os

def is_valid_image(path):
    try:
        with Image.open(path) as img:
            img.verify()
        return True
    except Exception as er:
        print(f"invalid image path:{path} , error:{er}")
        return False
    

def check_file_exist(filepaths):
    for path in filepaths:
        if not os.path.exists(path):
            print(f"File was not found:{path}")
            