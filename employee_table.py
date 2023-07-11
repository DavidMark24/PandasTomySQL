from utils.csv_reader import read_csv
from database_connect import database_con
import logging


def emp_table():
    mydb = database_con()
    cursor = mydb.cursor()
    table_name2 = 'Employees'
    try:
        emp_query = f'DROP TABLE IF EXISTS {table_name2}'
        cursor.execute(emp_query)
    except Exception as e:
        logging.error(f"An error occurred while executing SQL command: {str(e)}")
    else:
        emp_query = f'CREATE TABLE IF NOT EXISTS {table_name2} (first_name VARCHAR (255), last_name VARCHAR(255), id int ' \
                    f'PRIMARY KEY, man_name VARCHAR(255), man_id int, dept_id int, join_date DATE, age int, birth_date DATE, salary int)'
        cursor.execute(emp_query)

    emp_file = 'data/employee.csv'
    emp_data = read_csv(emp_file)
    for row in emp_data:
        emp_id = int(row[2])
        emp_first = row[0]
        emp_last = row[1]
        emp_man = row[3]
        man_id = int(row[4])
        dept = int(row[5])
        join = row[6]
        emp_age = int(row[7])
        birth = row[8]
        emp_sal = int(row[9])
        insert_emp = f"INSERT INTO {table_name2} (id, first_name, last_name, man_name, man_id, dept_id, join_date, age, " \
                     f"birth_date, salary) VALUES ({emp_id}, '{emp_first}', '{emp_last}', '{emp_man}', {man_id}, {dept}, '{join}', {emp_age}, '{birth}', {emp_sal})"
        cursor.execute(insert_emp)
        mydb.commit()
