from typing import Union
from pydantic import BaseModel, HttpUrl, FilePath, Field


class User(BaseModel):
    url: HttpUrl = Field(title="Put URL here", example="https://www.example.com")
    user_input_file: FilePath = Field(title="Input the user file", example="./user.txt")
    captcha_xpath: str = Field(title="Captcha image input box XPath", example="""//*[@id="example01"]""")
    captcha_image_name: str = Field(title="Captcha image file name", example="image.jpg")
    captcha_error_xpath: str = Field(title="Invalid Captcha error XPath", example="""//*[@id="example01"]""")
    user_xpath: str = Field(title="User input box XPath", example="""//*[@id="example01"]""")
    user_error_xpath: str = Field(title="Invalid user error XPath", example="""//*[@id="example01"]""")
    submit_xpath: str = Field(title="Submit button XPath", example="""//*[@id="example01"]""")
    gpu_mode: bool = Field(title="Use GPU render", example=False)
    captcha_language: Union[str, None] = Field(title="Language of captcha image", example="en")
    thread_number: Union[int, None] = Field(title="Number of threads", example=1)


class UserPass(BaseModel):
    url: HttpUrl = Field(title="Put URL here", example="https://www.example.com")
    user_input_file: FilePath = Field(title="Input the user file", example="./user.txt")
    password_input_file: FilePath = Field(title="Input the password file", example="./password.txt")
    captcha_image_xpath: str = Field(title="Captcha image XPath", example="""//*[@id="example01"]""")
    captcha_input_xpath: str = Field(title="Captcha image input box XPath", example="""//*[@id="example01"]""")
    captcha_image_name: str = Field(title="Captcha image file name", example="image.jpg")
    captcha_error_xpath: str = Field(title="Invalid Captcha error XPath", example="""//*[@id="example01"]""")
    user_xpath: str = Field(title="User input box XPath", example="""//*[@id="example01"]""")
    user_error_xpath: str = Field(title="Invalid user error XPath", example="""//*[@id="example01"]""")
    password_xpath: str = Field(title="Password input box XPath", example="""//*[@id="example01"]""")
    password_error_xpath: str = Field(title="Invalid user error XPath", example="""//*[@id="example01"]""")
    submit_xpath: str = Field(title="Submit button XPath", example="""//*[@id="example01"]""")
    gpu_mode: bool = Field(title="Use GPU render", example=False)
    captcha_language: Union[str, None] = Field(title="Language of captcha image", example="en")
    thread_number: Union[int, None] = Field(title="Number of threads", example=1)
