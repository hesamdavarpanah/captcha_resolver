class ExceptionHandler:
    def __init__(self, status_code):
        self.status_code = status_code
        self.status = {200: f"\033[91m The service is not secure",
                       202: f"\033[94m data sent",
                       400: f"\033[93m data not sent",
                       401: f"\033[93m invalid user",
                       403: f"\033[93m invalid password",
                       429: f"\033[93m invalid captcha data",
                       500: f"\033[92m The service is secure", }

    @property
    def exception_sender(self):
        return self.status[self.status_code]
