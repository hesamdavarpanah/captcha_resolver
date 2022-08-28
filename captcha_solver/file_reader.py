import re


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def text_reader(self):
        file = open(self.file_path)
        lines = file.readlines()
        return [re.sub('\n', '', _) for _ in lines]
