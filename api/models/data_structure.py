from typing import Union
from pydantic import BaseModel, HttpUrl, FilePath, Field


class Data(BaseModel):
    url: HttpUrl = Field(title="Put URL here", example="https://www.example.com/")
    user_input_file: FilePath = Field(title="Input the user file", example="./user.txt")
    password_input_file: Union[str, None] = Field(title="Input the password file", example="password.txt (optional)")
    captcha_image_xpath: str = Field(title="Captcha image XPath", example="""//*[@id="example01"]""")
    captcha_input_xpath: str = Field(title="Captcha image input box XPath", example="""//*[@id="example01"]""")
    user_xpath: str = Field(title="User input box XPath", example="""//*[@id="example01"]""")
    submit_xpath: str = Field(title="Submit button XPath", example="""//*[@id="example01"]""")
    password_xpath: Union[str, None] = Field(title="The password XPath", example="""//*[@id="example01"] (optional)""")
    gpu_mode: bool = Field(title="Use GPU render", example=False)
    captcha_language: Union[str, None] = Field(title="Language of captcha image", example="en")
    thread_number: Union[int, None] = Field(title="Number of threads", example=1)
