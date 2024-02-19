import os
from datetime import datetime, timedelta
from faker import Faker
import csv
import random

fake = Faker()

def generate_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(1, (end_date - start_date).days))

def create_file(file_path, header, data_generator, num_rows):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for i in range(num_rows):
            csv_writer.writerow(data_generator(i))

def create_vendors_data(row_id):
    return [row_id, fake.company()]

def create_animals_data(row_id):
    entry_date = generate_date(entry_date_start, entry_date_end)
    maturity = random.choice(["да", "нет"])
    age = random.randint(1, 10)
    gender = random.choice(["Самец", "Самка"])
    return [row_id, fake.name().split()[0], entry_date, maturity, age, gender]

def create_employees_data(row_id):
    employment_date = generate_date(entry_date_start, entry_date_end)
    age = random.randint(18, 80)
    gender = random.choice(["М", "Ж"])
    salary = random.randint(30000, 200000)
    return [row_id, fake.name().split()[0], fake.name().split()[1], fake.name().split()[0], age, gender, employment_date, salary]

def create_zoo_data(row_id):
    return [row_id, fake.company(), fake.country(), fake.city()]

entry_date_start = datetime(2005, 1, 9)
entry_date_end = datetime.now()

your_path = input("Enter your path: ")
num_rows = int(input("Enter number of rows: "))

vendors_file_path = your_path + 'Vendors.csv'
animals_file_path = your_path + 'Animval.csv'
employees_file_path = your_path + 'Employee.csv'
zoo_file_path = your_path + 'Zoo.csv'

create_file(vendors_file_path, ["Id", "Наименование"], create_vendors_data, num_rows)
create_file(animals_file_path, ["Id", "Кличка", "Дата появления", "Зрелость", "Возраст", "Пол"], create_animals_data, num_rows)
create_file(employees_file_path, ["Id", "Имя", "Фамилия", "Отчество", "Возраст", "Пол", "Дата приема на работу", "Размер зарплаты"], create_employees_data, num_rows)
create_file(zoo_file_path, ["Id", "Наименование", "Страна", "Город"], create_zoo_data, num_rows)
