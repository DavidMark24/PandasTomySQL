import pandas as pd
from database_connect import Database
from utils.config_parse import config_parse
from sqlalchemy import text
import logging

# Creating Logging config format
logging.basicConfig(filename='data/main.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')


class Main:
    def __init__(self):
        self.mydb = Database("data/config.ini")
        self.engine = self.mydb.create_engine()
        self.connect = self.mydb.create_engine().connect()
        self.config_file = "data/config.ini"
        self.query_key = "qy"
        self.departments_csv = "data/departments.csv"

    def read_config(self):
        try:
            config = config_parse(self.config_file)
            return config.get('query', self.query_key)
        except Exception as err:
            logging.error(f'An error occurred while reading the config file: {str(err)}')
            return None

    def read_departments_csv(self):
        try:
            return pd.read_csv(self.departments_csv)
        except Exception as err:
            logging.error(f'An error occurred while reading the departments CSV file: {str(err)}')
            return None

    def execute_query(self, query):
        try:
            with self.connect as conn:
                dept_df = self.read_departments_csv()
                if dept_df is not None:
                    query = text(query)
                    output_df = pd.read_sql_query(query, conn, params=dict(dept_df))
                    print(output_df)
        except Exception as err:
            logging.error(f'An error occurred with SQL query execution: {str(err)}')


if __name__ == '__main__':
    start_data = Main()
    sql_query = start_data.read_config()
    if sql_query is not None:
        start_data.execute_query(sql_query)
