from utils.config_parse import config_parse
from sqlalchemy import create_engine
import logging


class Database:

    def __init__(self, file):
        self.file = file

    def create_engine(self):
        try:
            config = config_parse(self.file)
            db_host = config['host']['name']
            db_user = config['user']['name']
            db_pass = config['password']['pw']
            db_db = config['database']['db']
            db_pt = config['port']['pt']
            return create_engine(
                f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_pt}/{db_db}')
        except Exception as err:
            logging.error(f'An error occurred with engine creation: {str(err)}')
            return None

