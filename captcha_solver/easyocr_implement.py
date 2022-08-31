from easyocr import Reader
import warnings
from pathlib import Path
from uuid import uuid4


class MyEasyOCR:
    def __init__(self, image, gpu_mode, language):
        self.image = image
        self.language = language
        self.gpu_mode = gpu_mode
        self.allow_list = "ABbCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    @property
    def easy_result(self):
        warnings.filterwarnings("ignore", category=UserWarning)
        reader = Reader([self.language], gpu=self.gpu_mode, verbose=False)
        result = reader.readtext(self.image, allowlist=self.allow_list, detail=False).pop()
        Path("captcha.jpg").rename(f"captcha_images_solved/{uuid4()}.jpg")
        return result
