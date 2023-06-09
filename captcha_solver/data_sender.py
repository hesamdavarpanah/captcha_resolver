from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pyautogui
from json import loads
from os import path, rename, remove
from shutil import rmtree
from time import sleep
from PIL import Image
from selenium.common.exceptions import NoSuchElementException
import getpass
from webdriver_manager.chrome import ChromeDriverManager


class DataSender:
    def __init__(self, url):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.options.add_experimental_option("detach", True)
        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=self.options,
                                        desired_capabilities=capabilities)
        self.browser.set_page_load_timeout(120)
        self.browser.get(url=self.url)
        self.logs = self.browser.get_log('performance')
        self.status_code = None

    def captcha_downloader(self, captcha_image_name):
        user = getpass.getuser()
        sleep(3)
        pyautogui.hotkey("ctrl", "s")
        sleep(1)
        pyautogui.typewrite("captcha_solver")
        pyautogui.hotkey("enter")
        sleep(2)
        filename, file_extension = path.splitext(captcha_image_name)
        if file_extension == ".png":
            img = Image.open(f"/home/{user}/Downloads/captcha_solver_files/{captcha_image_name}")
            img.save('captcha.jpg', "JPEG")
            rmtree(f"/home/{user}/Downloads/captcha_solver_files")
            remove(f"/home/{user}/Downloads/captcha_solver.html")
        else:
            rename(f"/home/{user}/Downloads/captcha_solver_files/{captcha_image_name}", "captcha.jpg")
            rmtree(f"/home/{user}/Downloads/captcha_solver_files")
            remove(f"/home/{user}/Downloads/captcha_solver.html")

    def window_closer(self):
        pyautogui.hotkey("alt", "f4")

    def captcha_sender(self, captcha_input_xpath, captcha_data):
        try:
            self.browser.find_element(By.XPATH, captcha_input_xpath).send_keys(captcha_data)
            self.status_code = 202
        except Exception:
            self.status_code = 400
        return self.status_code

    def clear_xpath(self, x_path):
        try:
            sleep(3)
            self.browser.find_element(By.XPATH, x_path).clear()
            self.status_code = 202
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
        sleep(2)
        try:
            self.browser.find_element(By.XPATH, submit_xpath).click()
            self.status_code = 202
        except Exception:
            self.status_code = 400
        return self.status_code

    def captcha_error(self, captcha_error_xpath):
        try:
            self.browser.find_element(By.XPATH, captcha_error_xpath)
            self.status_code = 429
        except NoSuchElementException:
            self.status_code = 200
            return self.status_code
        except Exception:
            self.status_code = 400
            return self.status_code

    def user_error(self, user_error_xpath):
        try:
            self.browser.find_element(By.XPATH, user_error_xpath)
            self.status_code = 401
        except NoSuchElementException:
            self.status_code = 200
        except Exception:
            self.status_code = 400
        return self.status_code

    def password_error(self, password_error_xpath):
        try:
            self.browser.find_element(By.XPATH, password_error_xpath)
            self.status_code = 403
        except NoSuchElementException:
            self.status_code = 200
        except Exception:
            self.status_code = 400
        return self.status_code

    def check_vul_exist(self):
        statuses = []
        for log in self.logs:
            if log['message']:
                d = loads(log['message'])
                if d['message'].get('method') == "Network.responseReceived":
                    statuses.append(d['message']['params']['response']['status'])
        for i in statuses:
            if not i == 200:
                self.status_code = 500
                return self.status_code
            else:
                self.status_code = 200
        return self.status_code
