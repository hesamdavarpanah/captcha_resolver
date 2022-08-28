from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
import pyautogui
from os import path, rename, remove
from shutil import rmtree
from time import sleep


class CaptchaDownloader:
    def __init__(self, url):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=self.options)
        self.browser.set_page_load_timeout(120)
        self.browser.get(url=self.url)
        self.status_code = None

    def captcha_downloader(self, captcha_img_xpath):
        dir_path = path.dirname(path.realpath(__file__))
        WebDriverWait(self.browser, 60).until(visibility_of_element_located((By.XPATH, captcha_img_xpath)))
        pyautogui.hotkey("ctrl", "s")
        sleep(1)
        pyautogui.typewrite(f"{dir_path}")
        pyautogui.hotkey("enter")
        sleep(2)
        rename("captcha_solver_files/Index", "captcha.jpg")
        rmtree("captcha_solver_files")
        remove("captcha_solver.html")

    def captcha_sender(self, captcha_input_xpath, captcha_data):
        try:
            self.browser.find_element(By.XPATH, captcha_input_xpath).send_keys(captcha_data)
            self.status_code = 200
        except Exception:
            self.status_code = 400
        return self.status_code

    def user_sender(self, user_xpath, user):
        try:
            self.browser.find_element(By.XPATH, user_xpath).send_keys(user)
            self.status_code = 202
        except Exception:
            self.status_code = 400
        return self.status_code

    def password_sender(self, password_input_xpath, password_data):
        try:
            self.browser.find_element(By.XPATH, password_input_xpath).send_keys(password_data)
            self.status_code = 202
        except Exception:
            self.status_code = 400
        return self.status_code

    def submit(self, submit_xpath):
        try:
            self.browser.find_element(By.XPATH, submit_xpath).click()
            self.status_code = 202
        except Exception:
            self.status_code = 400
        return self.status_code