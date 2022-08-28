class ExceptionHandler:
    def __init__(self, func_name, status_code):
        self.status_code = status_code
        self.func_name = func_name
        self.status = {202: f"\033[92m {self.func_name} sent",
                       200: f"\033[92m {self.func_name} solved",
                       400: f"\033[91m {self.func_name} not sent"}

    @property
    def exception_sender(self):
        return self.status[self.status_code]
