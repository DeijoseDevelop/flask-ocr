import base64
from io import BytesIO

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r''


class ReadImage(object):

    def __init__(self, bytes_or_image: str or bytes):
        self.bytes_or_image = bytes_or_image
        self.image = None

    def convert_image_to_base64(self):
        buffered = BytesIO()
        self.image.save(buffered, format="JPEG")
        self.image = base64.b64encode(buffered.getvalue())
        return self

    def convert_base64_to_image(self):
        self.image = Image.open(BytesIO(base64.b64decode(self.bytes_or_image)))
        return self

    def create_image_from_path(self):
        self.image = Image.open(self.bytes_or_image)
        return self

    def convert_image_to_text(self):
        return pytesseract.image_to_string(self.image)

