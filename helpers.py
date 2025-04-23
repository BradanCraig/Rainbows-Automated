import base64
from io import BytesIO
from PIL import Image

def decode_image(encoded_img):
    
    img_str = base64.b64decode(encoded_img)
    img_file = BytesIO(img_str)
    img = Image.open(img_file)

    return img