from captcha_solver.easyocr_implement import MyEasyOCR
from captcha_solver.logger import Logger
from captcha_solver.mongodb_config import MongoDBConfiguration
from time import sleep
from os import path, rename, remove
import cv2
import matplotlib.pyplot as plt
import numpy as np
import extcolors
from shutil import rmtree
from PIL import Image
from easyocr import Reader
import warnings
from pathlib import Path
from uuid import uuid4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from captcha_solver.data_sender import DataSender
from captcha_solver.file_reader import FileReader
from captcha_solver.image_processing import DSP

# # import unittest
# #
# #
# # class MyTestCase(unittest.TestCase):
# #     def test_something(self):
# #         self.assertEqual(True, False)  # add assertion here
# #
# #
# # if __name__ == '__main__':
# #     unittest.main()
#
# data_dict = data.dict()
# file = FileReader(file_path=data_dict["user_input_file"])
# captcha = CaptchaDownloader(url=data_dict["url"])
#
# for user in file.text_reader():
#     if data_dict["password_input_file"]:
#         password_file = FileReader(file_path=data_dict["password_input_file"])
#
#         for password in password_file.text_reader():
#             captcha.captcha_downloader(data_dict["captcha_image_xpath"])
#             dsp = DSP()
#             image = dsp.image_editor(dsp.get_color()[0]["start"], dsp.get_color()[0]["end"])
#             captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
#
#             captcha.user_sender(user_xpath=data_dict["user_xpath"], user=user)
#             captcha.password_sender(password_input_xpath=data_dict["password_xpath"], password_data=password)
#             captcha.captcha_sender(captcha_input_xpath=data_dict["captcha_input_xpath"],
#                                    captcha_data=captcha_data.easy_result())
#             captcha.submit(data_dict["submit_xpath"])
#     else:
#         captcha.captcha_downloader(data_dict["captcha_image_xpath"])
#         dsp = DSP()
#         image = dsp.image_editor(dsp.get_color()[0]["start"], dsp.get_color()[0]["end"])
#         captcha_data = MyEasyOCR(image=image, gpu_mode=data_dict["gpu_mode"],
#                                  language=data_dict["captcha_language"])
#
#         captcha.user_sender(user_xpath=data_dict["user_xpath"], user=user)
#         captcha.captcha_sender(captcha_input_xpath=data_dict["captcha_input_xpath"],
#                                captcha_data=captcha_data.easy_result())
#         captcha.submit(data_dict["submit_xpath"])


# options = webdriver.ChromeOptions()
# options.add_argument("--incognito")
# options.add_experimental_option("detach", True)
# capabilities = DesiredCapabilities.CHROME.copy()
# capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
# browser = webdriver.Chrome(options=options, desired_capabilities=capabilities)
# action = ActionChains(browser)
# browser.set_page_load_timeout(120)
# browser.get(url="https://sayancard.ir/Customer/POSRequest")
# logs = browser.get_log('performance')
# user = ["0123456789", "1234567890"]
#
# user_xpath = browser.find_element(By.XPATH, "//*[@id=\"ValidCode\"]")
# for u in user:
#     user_xpath.send_keys(u)
#     sleep(3)
#     user_xpath.clear()


# for user in user_file.text_reader():
#     try:
#         captcha_error = data_sender.captcha_error(data_dict["captcha_error_xpath"])
#         user_error = data_sender.user_error(data_dict["user_error_xpath"])
#         if captcha_error == 429:
#             data_sender.clear_xpath(data_dict["captcha_image_xpath"])
#             data_sender.captcha_downloader(data_dict["captcha_image_xpath"], data_dict["captcha_image_name"])
#             dsp = DSP()
#             image = dsp.image_editor(dsp.get_color[0]["start"], dsp.get_color[0]["end"])
#             captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
#             data_sender.captcha_sender(data_dict["captcha_input_xpath"], captcha_data.easy_result)
#             data_sender.submit(data_dict["submit_xpath"])
#             out = data_sender.check_vul_exist()
#             status = ExceptionHandler(out)
#             logger.mongodb_insert_one({out: status})
#             return status
#         elif user_error == 401:
#             status = ExceptionHandler(401)
#             logger.mongodb_insert_one({401: status})
#         else:
#             data_sender.captcha_downloader(data_dict["captcha_image_xpath"], data_dict["captcha_image_name"])
#             data_sender.clear_xpath(data_dict["user_xpath"])
#             dsp = DSP()
#             image = dsp.image_editor(dsp.get_color()[0]["start"], dsp.get_color()[0]["end"])
#             captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
#             data_sender.user_sender(data_dict["user_xpath"], user)
#             data_sender.captcha_sender(data_dict["captcha_input_xpath"], captcha_data.easy_result())
#             data_sender.submit(data_dict["submit_xpath"])
#             out = data_sender.check_vul_exist()
#             status = ExceptionHandler(out)
#             logger.mongodb_insert_one({out: status})
#             return status
#     except FileNotFoundError:
#         captcha_error = data_sender.captcha_error(data_dict["captcha_error_xpath"])
#         user_error = data_sender.user_error(data_dict["user_error_xpath"])
#         if captcha_error == 429:
#             data_sender.clear_xpath(data_dict["captcha_image_xpath"])
#             data_sender.captcha_downloader(data_dict["captcha_image_xpath"], data_dict["captcha_image_name"])
#             dsp = DSP()
#             image = dsp.image_editor(dsp.get_color[0]["start"], dsp.get_color[0]["end"])
#             captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
#             data_sender.captcha_sender(data_dict["captcha_input_xpath"], captcha_data.easy_result)
#             data_sender.submit(data_dict["submit_xpath"])
#             out = data_sender.check_vul_exist()
#             status = ExceptionHandler(out)
#             logger.mongodb_insert_one({out: status})
#             return status
#         elif user_error == 401:
#             status = ExceptionHandler(401)
#             logger.mongodb_insert_one({401: status})
#         else:
#             data_sender.captcha_downloader(data_dict["captcha_image_xpath"], data_dict["captcha_image_name"])
#             data_sender.clear_xpath(data_dict["user_xpath"])
#             dsp = DSP()
#             image = dsp.image_editor(dsp.get_color()[0]["start"], dsp.get_color()[0]["end"])
#             captcha_data = MyEasyOCR(image, data_dict["gpu_mode"], data_dict["captcha_language"])
#             data_sender.user_sender(data_dict["user_xpath"], user)
#             data_sender.captcha_sender(data_dict["captcha_input_xpath"], captcha_data.easy_result())
#             data_sender.submit(data_dict["submit_xpath"])
#             out = data_sender.check_vul_exist()
#             status = ExceptionHandler(out)
#             logger.mongodb_insert_one({out: status})
#             return status
data_sender = DataSender("https://sayancard.ir/Customer/POSRequest")
data_sender.captcha_downloader("Index")
dsp = DSP()
image = dsp.image_editor(dsp.get_color[0]["start"], dsp.get_color[0]["end"])
captcha_data = MyEasyOCR(image, False, "en")
print(captcha_data.easy_result)
# m = MongoDBConfiguration()
# l = Logger(m.mongodb_config)
# coll = l.mongodb_collection(l.mongodb_database("test"), "test")
# l.mongodb_insert_one(coll, {"test": 1})
