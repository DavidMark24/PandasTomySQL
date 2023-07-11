import logging


class Logger:

    def __init__(self, file, level, message):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        file_handler = logging.FileHandler("data/main.log")
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def logs(self):
        self.logger.error("An error occurred with SQL execution")





print(logs.file, logs.level, logs.message)

