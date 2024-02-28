from datetime import datetime, timedelta
from faker import Faker
import csv
import random

fake = Faker()

specie_dict = {'Chinese Alligator': [220, 44, 45, 4.5, 50],
               'Venezuelan Amazon': [41, 8.2, 0.34, 0.034, 60],
               'Yellow-faced Amazon': [37, 7.4, 0.34, 0.034, 50],
               'Blue-faced Amazon': [54.5, 10.9, 0.52, 0.052, 70],
               'White-tailed wildebeest': [120, 24, 170, 17, 20],
               'Black Antelope': [90, 18, 170, 17, 20],
               'Red Macaw': [90, 18, 1.25, 0.125, 80],
               'Yellow macaw': [147, 29.4, 1.3, 0.13, 50],
               'Big cormorant': [100, 20, 3, 0.3, 20],
               'Snow leopard (Snow Leopard)': [120, 24, 30, 3, 20],
               'Panamanian Psalmopeus': [23, 4.6, 0.15, 0.015, 15],
               'Golden Eagle': [93, 18.6, 5, 0.5, 50],
               'Ordinary beaver': [80, 16, 30, 3, 20],
               'Bristly Armadillo': [38, 7.6, 0.9, 0.09, 16],
               'Vicuna': [150, 30, 50, 5, 20],
               'Mexican Venomous tooth': [90, 18, 45, 4.5, 30],
               'Raven': [70, 14, 0.14, 0.014, 40],
               'Horned Raven': [115, 23, 6, 0.6, 60],
               'Senegalese galago': [38, 7.6, 200, 20, 20],
               'Thick-tailed galago': [70, 14, 1.2, 0.12, 22],
               'Black-armed Gibbon': [64, 12.8, 6, 0.6, 30],
               'Striped Hyena': [120, 24, 40, 4, 15],
               'Lowland Gorilla': [165, 33, 130, 13, 50],
               'Arizona yadozub': [60, 12, 2, 0.2, 30],
               'Jaguarundi': [137, 27.4, 8, 0.8, 40],
               'Diamond Turtledove': [137, 27.4, 8, 0.8, 15],
               'Emu': [190, 38, 45, 4.5, 30],
               'Australian broad-nosed': [56, 11.2, 0.7, 0.07, 3],
               'Laughing Turtledove': [30, 6, 0.25, 0.025, 12],
               'Black Vulture': [280, 56, 11, 1.1, 50],
               'Chinchilla': [55, 11, 0.75, 0.075, 20],
               'Shiloklyovka': [48, 9.6, 0.32, 0.032, 15],
               'Asian Jackal': [121, 24.2, 9, 0.9, 14],
               'Lapwing': [45, 9, 0.3, 0.03, 12],
               'Silver Gull': [60, 12, 0.8, 0.08, 10],
               'Grey Heron': [98, 19.6, 1.5, 0.15, 8],
               'Great White Heron': [104, 20.8, 1.1, 0.11, 7],
               'white-browed goose': [77, 15.4, 2.6, 0.26, 17],
               'Ussuri Harza': [94, 18.8, 4, 0.4, 17],
               'Mountain Goose': [70, 14, 3, 0.3, 30],
               'Pink Flamingo': [145, 29, 3.5, 0.35, 50],
               'Goose gumennik': [89, 17.8, 3.5, 0.35, 30],
               'Red Flamingo': [145, 29, 3.5, 0.35, 50],
               'Western goose gumennik': [90, 18, 4, 0.4, 30],
               'West Siberian Owl': [75, 15, 2, 0.2, 70],
               'red-headed goose': [50, 10, 2, 0.2, 25],
               'Fennec': [40, 8, 1.5, 0.15, 20],
               'Pheasant Tragopan Temminka': [210, 42, 1.5, 0.15, 13],
               "Magellan's goose": [65, 13, 3, 0.3, 25],
               'Silver pheasant': [120, 24, 4, 0.4, 15],
               'Fire-backed Pheasant': [70, 14, 1.2, 0.12, 12],
               'Golden Pheasant': [80, 16, 0.72, 0.072, 15],
               'Brown Peacock Pheasant': [89, 17.8, 1.5, 0.15, 12],
               "Ross's Goose": [66, 13.2, 1.3, 0.13, 25],
               'Grey Goose': [90, 18, 3.7, 0.37, 30],
               'Dry-nosed goose': [95, 19, 3.8, 0.38, 25],
               'Diamond Pheasant': [110, 22, 0.6, 0.06, 25],
               'Cuban Whistling Duck': [56, 11.2, 0.65, 0.065, 20],
               'double-humped camel': [360, 72, 40, 4, 50],
               'Toucan toko': [50, 10, 0.5, 0.05, 20],
               'Blackbird': [26, 5.2, 0.125, 0.0125, 7],
               'White-breasted hedgehog': [29, 5.8, 0.9, 0.09, 4],
               'Amur tiger': [200, 40, 250, 25, 15],
               'Raccoon polosun': [85, 17, 6, 0.6, 4],
               'Red-tailed Jacko': [35, 7, 0.6, 0.06, 49],
               'Panthera leo': [250, 90, 190, 30, 20],
               'Elephas maximus': [300, 120, 4500, 200, 60],
               'Ailuropoda melanoleuca': [150, 10, 150, 15, 30],
               'Panthera tigris': [270, 100, 300, 50, 25],
               'Crocodylidae': [300, 50, 50, 10, 50],
               'Gorilla': [170, 100, 200, 13, 35],
               'Aquila': [70, 30, 5, 2, 15],
               'Macropodidae': [200, 40, 50, 3, 50],
               'Equus zebra': [200, 80, 400, 20, 30],
               'Giraffa camelopardalis': [500, 200, 1200, 100, 40]}
specie_arr = ['Chinese Alligator', 'Venezuelan Amazon', 'Yellow-faced Amazon', 'Blue-faced Amazon',
              'White-tailed wildebeest', 'Black Antelope', 'Red Macaw', 'Yellow macaw', 'Big cormorant',
              'Snow leopard (Snow Leopard)', 'Panamanian Psalmopeus', 'Golden Eagle', 'Ordinary beaver',
              'Bristly Armadillo', 'Vicuna', 'Mexican Venomous tooth', 'Raven', 'Horned Raven', 'Senegalese galago',
              'Thick-tailed galago', 'Black-armed Gibbon', 'Striped Hyena', 'Lowland Gorilla', 'Arizona yadozub',
              'Jaguarundi', 'Jaguarundi', 'Diamond Turtledove', 'Emu', 'Australian broad-nosed', 'Laughing Turtledove',
              'Black Vulture', 'Chinchilla', 'Shiloklyovka', 'Asian Jackal', 'Lapwing', 'Silver Gull', 'Grey Heron',
              'Great White Heron', 'white-browed goose', 'Ussuri Harza', 'Mountain Goose', 'Pink Flamingo',
              'Goose gumennik', 'Red Flamingo', 'Western goose gumennik', 'West Siberian Owl', 'red-headed goose',
              'Fennec', 'Pheasant Tragopan Temminka', "Magellan's goose", 'Silver pheasant', 'Fire-backed Pheasant',
              'Golden Pheasant', 'Brown Peacock Pheasant', "Ross's Goose", 'Grey Goose', 'Dry-nosed goose',
              'Diamond Pheasant', 'Cuban Whistling Duck', 'double-humped camel', 'Toucan toko', 'Blackbird',
              'White-breasted hedgehog', 'Amur tiger', 'Raccoon polosun', 'Red-tailed Jacko', 'Panthera leo',
              'Elephas maximus', 'Ailuropoda melanoleuca', 'Panthera tigris', 'Crocodylidae', 'Gorilla', 'Aquila',
              'Macropodidae', 'Equus zebra', 'Giraffa camelopardalis']


def generate_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(1, (end_date - start_date).days))


def create_file(file_path, header, data_generator, num_rows):
    with open(file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for i in range(num_rows):
            csv_writer.writerow(data_generator(i))


def create_vendors_row(row_id):
    return [row_id, fake.company()]


def create_animals_row(row_id):
    specie = random.choice(specie_arr)

    entry_date = generate_date(datetime.now() - timedelta(days=specie_dict[specie][4] * 365), entry_date_end)
    difference = datetime.now() - entry_date
    height = 0
    weight = 0

    if (difference > timedelta(days=specie_dict[specie][4] * 73)):
        maturity = True
        height = round(random.uniform(specie_dict[specie][1], specie_dict[specie][0]), 2)
        weight = round(random.uniform(specie_dict[specie][3], specie_dict[specie][2]), 2)
    else:
        maturity = False
        height = round(random.uniform(1.0, specie_dict[specie][1]), 2)
        weight = round(random.uniform(1.0, specie_dict[specie][3]), 2)

    gender = random.choice(["Самец", "Самка"])
    return [row_id, fake.name().split()[0], entry_date, specie, maturity, weight, height, gender]


def create_employees_row(row_id):
    employment_date = generate_date(entry_date_start, entry_date_end)
    age = random.randint(18, 80)
    gender = random.choice(["М", "Ж"])
    salary = random.randint(30000, 200000)
    return [row_id, fake.name().split()[0], fake.name().split()[1], fake.name().split()[0], age, gender,
            employment_date, salary]


def create_zoo_row(row_id):
    return [row_id, fake.company(), fake.country(), fake.city()]


entry_date_start = datetime(2005, 1, 9)
entry_date_end = datetime.now()

your_path = '/home/barry/Документы/Data/'
num_rows = 100

vendors_file_path = your_path + 'Vendors.csv'
animals_file_path = your_path + 'Animval.csv'
employees_file_path = your_path + 'Employee.csv'
zoo_file_path = your_path + 'Zoo.csv'

create_file(vendors_file_path, ["Id", "Наименование"], create_vendors_row, num_rows)
create_file(animals_file_path, ["Id", "Кличка", "Дата появления", "Вид", "Зрелость", "Вес", "Рост", "Пол"],
            create_animals_row,
            num_rows)
create_file(employees_file_path,
            ["Id", "Имя", "Фамилия", "Отчество", "Возраст", "Пол", "Дата приема на работу", "Размер зарплаты"],
            create_employees_row, num_rows)
create_file(zoo_file_path, ["Id", "Наименование", "Страна", "Город"], create_zoo_row, num_rows)
