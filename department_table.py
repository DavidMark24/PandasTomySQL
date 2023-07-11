from utils.csv_reader import read_csv
from database_connect import database_con
import logging


def dept_table():
    mydb = database_con()
    cursor = mydb.cursor()
    table_name = 'Departments'
    try:
        table_query = f'DROP TABLE IF EXISTS {table_name}'
        cursor.execute(table_query)
    except Exception as e:
        logging.error(f"An error occurred while executing SQL command: {str(e)}")
    else:
        table_name = 'Departments'
        table_query = f'CREATE TABLE IF NOT EXISTS {table_name} (dept_id INT PRIMARY KEY, department_name VARCHAR(255))'
        cursor.execute(table_query)

        # Read CSV and Insert Data
        dept_file = 'data/departments.csv'
        dept_data = read_csv(dept_file)
        for row in dept_data:
            id_val = row[0]
            dept_name = row[1]
            insert_value = f"INSERT INTO {table_name} (dept_id, department_name) VALUES ({id_val},'{dept_name}')"
            cursor.execute(insert_value)
            mydb.commit()
