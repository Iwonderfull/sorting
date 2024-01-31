import os
from datetime import datetime, timedelta
from faker import Faker
import csv
import random


fake = Faker()

yourPath = "/home/barry/Документы/Data/"

def create_vendros(num_rows):
    csv_file_path = yourPath + 'Vendors.csv'

    with open(csv_file_path, 'w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["Id", "Наименование"])

        for i in range(num_rows):

            data_row = [i, fake.company()]
            csv_writer.writerow(data_row)


def create_animals(num_rows):
    csv_file_path = yourPath +' Animval.csv'

    with open(csv_file_path, 'w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["Id", "Кличка", "Дата появления", "Зрелость", "Возраст", "Пол"])

        for i in range(num_rows):
            entry_date = datetime(2020, 1, 1) + timedelta(days=random.randint(1, 365))
            maturity = random.choice(["да", "нет"])
            age = random.randint(1, 10)
            gender = random.choice(["Самец", "Самка"])

            csv_writer.writerow([i, fake.name().split()[0], entry_date, maturity, age, gender])



def create_employees(num_rows):
    csv_file_path = yourPath + 'Employee.csv'

    with open(csv_file_path, 'w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["Id", "Имя", "Фамилия", "Отчество", "Возраст", "Пол", "Дата приема на работу", "Размер зарплаты" ])

        for i in range(num_rows):
            employment_date = datetime(1995, 1, 1) + timedelta(days=random.randint(-3365, 3365))
            age = random.randint(18, 80)
            gender = random.choice(["М", "Ж"])
            salary = random.randint(30000, 200000)

            csv_writer.writerow([i, fake.name().split()[0], fake.name().split()[1], fake.name().split()[0], age,gender,employment_date, salary])

def create_zoo(num_rows):
    csv_file_path = yourPath + 'Zoo.csv'


    with open(csv_file_path, 'w', newline='') as csv_file:

        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(["Id", "Наименование", "Страна", "Город"])

        for i in range(num_rows):


            csv_writer.writerow([i, fake.company(),fake.country(),fake.city()])


yourPath = input("Enter your path ")

num = int(input("Enter number of rows "))

create_zoo(num)
create_employees(num)
create_animals(num)
create_vendros(num)