import os
import csv
import datetime
import random
from datetime import datetime, timedelta

yourPath = "C:/Users/Sonya/Documents/"

# provider
companyName_arr = ["Pet Paradise", "Paws and Claws Emporium", "Furry Friends Haven", "The Critter Corner",
                   "Whiskers & Wags", "Creature Comforts Co.", "The Pet Haven", "Animal Antics Store",
                   "Happy Tails Emporium", "Paw Prints Boutique", "The K9 Kingdom", "The Purrfect Place",
                   "Furball Frenzy", "Feathers & Fins Emporium", "Pet Palooza Store", "Wild Whiskers Shop",
                   "The Pet Nest", "Safari Pets Store", "Wags to Whiskers", "Critter Craze Corner", "The Paw Pad",
                   "Furry Fins Market", "Creature Comfort Co.", "The Loyal Companion", "Happy Hounds Haven",
                   "Purrfect Paws Boutique", "Animal Magic Store", "The Critter Clubhouse", "Whisker Wonderland",
                   "Furry Friends’ Faves", "The Pet Stop Shop", "Tails & Scales Emporium", "Pet Parade Place",
                   "Wild Wags Market", "Feathered Friends Haven", "The Pet Patch", "Zoo-tastic Store",
                   "Bark and Meow Emporium", "Finned Friends’ Corner", "Wagging Whiskers", "Pet Central Place",
                   "Whisker Wonders Shop", "Furry Finery Store", "The Pet Perch", "Tail Waggers’ Emporium",
                   "Creature Comforts Haven", "Happy Howls Boutique", "Feathered Frenzy Corner", "The Pet Carousel",
                   "Paws and Scales Emporium", "Critter Capers Store", "The Pet Zone", "Fluffy Friends’ Fun",
                   "The Jungle Pets Store", "Finned Finds Emporium", "Wagging Tail Treasures", "Paw Prints Emporium",
                   "The Pet Oasis", "Whisker Wonderland Store", "Furry Favorites Emporium", "ZooGalore", "PawsRUs",
                   "CritterCraze", "ThePetPantry", "FurEverFriends", "WhiskerWorld", "PurrFectPlace", "WildWagsMart",
                   "FeatheredFinds", "TheCritterClub", "HappyTailsHaven", "PetParadise", "FurryFriendsEmporium",
                   "AnimalAnticsShop", "TailWaggersDelight", "ThePetNest", "SafariPetSupplies", "BarkAndMeowMart",
                   "WhiskerWonderland", "CreatureComfortsCo", "PawprintsBoutique", "FinsAndFeathersStore", "PetPalooza",
                   "FurballFrenzy", "TheHappyHowl", "HoundHeaven", "MansionOfMeows", "BeaksAndSqueaks",
                   "CritterCarnival", "CritterCreations", "PawsomePlace", "WildWhiskers", "FishAndChipsShop",
                   "PurrfectionStore", "PetParlor", "WingsAndTails", "ThePetStop", "FluffyFriendsWorld",
                   "FeatheredFriendsFantasy", "HappyPawsPetStore", "FurryFinsCorner", "TailsAndWhales",
                   "PawAndClawCreations", "CreatureCommune", "NoseToTailTreats", "ThePetPatch",
                   "RainingCatsAndDogsShop", "CritterCabana", "ExoticCritterCorner", "PurrfectPawsPlace",
                   "AnimalEnchantment", "CritterCoveMarket", "PetPleasantries", "TheRabbitHutch", "WildlifeWonderland",
                   "RoyalReptilesShop", "TropicalTreats", "CritterCrazyCloset", "WhiskerWishes", "PawsAndPlay",
                   "AnimalAlley", "CritterComforts", "FinsAndFriendship", "PawprintsParadise", "ThePetPerch",
                   "TheDoggyDen", "ClawAndOrderStore", "FurryFortune", "WhiskerWagsWarehouse", "AvianAvenues",
                   "BarkBoutique", "CritterCarousel", "EnchantedEars", "ZooZenith", "TailsOfJoy", "CreatureCollection",
                   "CritterCubbyhole", "ReptileRendezvous", "FurryFiesta", "PawPleasures", "CritterComfort",
                   "FeatheredFriendsFusion", "ThePetPiazza", "FinsAndPawsPlaza", "WhiskerWorldWide", "CritterCottage",
                   "PawsAndPurrfections", "ThePamperedPet", "WildWhispers", "BirdBazaar", "FurryFeathers",
                   "PurrsAndWhiskers", "WaggingTailTreasures", "FeatheredFunStore", "ThePetOasis",
                   "TailsAndScalesSanctuary"]

# animal
nickNames_arr = ["Shadow", "Sunny", "Buddy", "Lucky", "Rocky", "Princess", "Max", "Lucy", "Daisy", "Charlie", "Coco",
                 "Tiger", "Molly", "Bear", "Jack", "Bella", "Milo", "Misty", "Oscar", "Ginger", "Oliver", "Sophie",
                 "Sam", "Rosie", "Buster", "Ruby", "Roxy", "Buddy", "Maggie", "Teddy", "Mia", "Baxter", "Luna",
                 "Bailey", "Sadie", "Simba", "Angel", "Milo", "Max", "Minnie", "Chloe", "Jake", "Zoe", "Cooper", "Emma",
                 "Harley", "Stella", "Duke", "Molly", "Axel", "Zara", "Bruno", "Gracie", "Sammy", "Jasmine", "Toby",
                 "Nala", "Rusty", "Sadie", "Ollie", "Mia", "Benji", "Frankie", "Gizmo", "Lola", "Bear", "Penny",
                 "Hunter", "Zoey", "Rocco", "Dakota", "Lucky", "Daisy", "Zeus", "Nova", "Gigi", "Cody", "Lily", "Louie",
                 "Sugar", "Sky", "Sasha", "Gus", "Bailey", "Angel", "Kona", "Casper", "Belle", "Riley", "Lexi",
                 "Oliver", "Sophie", "Simba", "Annie", "Zeus", "Zoe", "Scout", "Mocha", "Koda", "Lexi", "Gracie",
                 "Cleo", "Cooper", "Olive", "Hugo", "Heidi", "Daisy", "Samson", "Molly", "Louie", "Bella", "Tucker",
                 "Finn", "Marley", "Lola", "Minnie", "Riley", "Shadow", "Buddy", "Ginger", "Roxy", "Stella", "Bailey",
                 "Charlie", "Baxter", "Lilly", "Toby", "Maggie", "Maisie", "Apollo", "Dixie", "Rosie", "Bruno", "Lily",
                 "Rufus", "Luna", "Max", "Willow", "Bella", "Duke", "Mia", "Teddy", "Misty", "Prince", "Abby", "Millie",
                 "Cleo", "Otis", "Molly", "Bruce", "Zara", "Cody", "Nina", "Ruby", "Thor", "Lucy", "Sammy", "Hazel",
                 "Pepper", "Rusty", "Coco", "Sam", "Luna", "Charlie", "Maddie", "Thunderbolt", "Midnight", "Whisper",
                 "Sapphire", "Blaze", "Shadow", "Luna", "Echo", "Stella", "Jasper", "Willow", "Apollo", "Nova",
                 "Phoenix", "Athena", "Ghost", "Dakota", "Skyler", "Hunter", "Raven", "Loki", "Zara", "Gizmo", "Sasha",
                 "Dexter", "Misty", "Bandit", "Rocco", "Amber", "Cleo", "Koda", "Nyx", "Cosmo", "Jinx", "Maverick",
                 "Ziggy", "Finn", "Nala", "Leo", "Harley", "Juno", "Milo", "Lola", "Oscar", "Hazel", "Rusty", "Storm",
                 "Ruby", "Axel", "Sunny", "Zelda", "Mika", "Legend", "Skye", "Bruno", "Gypsy", "Casper", "Remy", "Kai",
                 "Coco", "Thor", "Chloe", "Arrow", "Fiona", "Rocky", "Cinnamon", "Blitz", "Trinity", "Moose", "Holly",
                 "Cyrus", "Callie", "Dash", "Xena", "Buddy", "Piper", "Rogue", "Toby", "Scout", "Kiara", "Rex", "Amira",
                 "Ace", "Sage", "Alaska", "Zorro", "Sable", "Diesel", "Serena", "Mars", "Roxy", "Tyson", "Zola",
                 "Rocket", "Ruby", "Aries", "Maximus", "Layla", "Atlas", "Mila"]
species = ["Elephant", "Lion", "Tiger", "Giraffe", "Monkey", "Bear", "Kangaroo", "Zebra", "Penguin", "Snake",
           "Rabbit", "Dolphin", "Fox", "Wolf", "Horse", "Cow", "Sheep", "Goat", "Pig", "Chicken", "Duck", "Owl",
           "Eagle", "Squirrel", "Raccoon", "Deer", "Moose", "Hippo", "Rhino", "Gorilla", "Panda", "Koala", "Sloth",
           "Leopard", "Cheetah", "Jaguar", "Ostrich", "Polar Bear", "Seal", "Walrus", "Otter", "Komodo Dragon",
           "Octopus", "Starfish", "Shark", "Whale", "Seahorse"]

# zoo
country = ["United States", "Canada", "United Kingdom", "Australia", "Germany", "France", "Japan", "China",
           "Brazil", "India", "Italy", "Russia", "South Africa", "Mexico", "Spain", "Netherlands", "Switzerland",
           "Sweden", "South Korea", "Argentina", "New Zealand", "Norway", "Singapore", "Ireland", "Denmark",
           "Belgium", "Finland", "Austria", "Chile", "Portugal"]
city = ["New York", "Toronto", "London", "Sydney", "Berlin", "Paris", "Tokyo", "Beijing", "Sao Paulo", "Mumbai",
        "Rome", "Moscow", "Cape Town", "Mexico City", "Madrid", "Amsterdam", "Zurich", "Stockholm", "Seoul",
        "Buenos Aires", "Auckland", "Oslo", "Singapore", "Dublin", "Copenhagen", "Brussels", "Helsinki", "Vienna",
        "Santiago", "Lisbon"]
zooName = ["Central Park Zoo", "Toronto Zoo", "London Zoo", "Taronga Zoo", "Berlin Zoological Garden",
           "Paris Zoological Park", "Ueno Zoo", "Beijing Zoo", "Sao Paulo Zoo", "Sanjay Gandhi National Park",
           "Bioparco di Roma", "Moscow Zoo", "Cape of Good Hope Nature Reserve", "Chapultepec Zoo",
           "Madrid Zoo Aquarium", "Artis Amsterdam Royal Zoo", "Zoo Zürich", "Skansen Open-Air Museum and Zoo",
           "Seoul Grand Park Zoo", "Lujan Zoo", "Auckland Zoo", "Oslo Reptile Park", "Singapore Zoo", "Dublin Zoo",
           "Copenhagen Zoo", "Planckendael Zoo", "Helsinki Zoo", "Tiergarten Schönbrunn Zoo",
           "Parque Metropolitano de Santiago", "Lisbon Zoo"]

# staff
name = ["Abigail", "Alexander", "Amelia", "Andrew", "Anna", "Anthony", "Ava", "Benjamin", "Charlotte",
        "Christopher", "Claire", "Daniel", "David", "Elizabeth", "Emily", "Emma", "Ethan", "Grace", "Hannah",
        "Henry", "Isabella", "Jacob", "James", "Joseph", "Joshua", "Liam", "Lily", "Lucas", "Madison", "Mason",
        "Matthew", "Mia", "Michael", "Natalie", "Noah", "Oliver", "Olivia", "Owen", "Ryan", "Samuel", "Sarah",
        "Sophia", "Thomas", "Victoria", "William", "Abigail", "Alexander", "Amelia", "Andrew", "Anna", "Anthony",
        "Ava", "Benjamin", "Charlotte", "Christopher", "Claire", "Daniel", "David", "Elizabeth", "Emily", "Emma",
        "Ethan", "Grace", "Hannah", "Henry", "Isabella", "Jacob", "James", "Joseph", "Joshua", "Liam", "Lily",
        "Lucas", "Madison", "Mason", "Matthew", "Mia", "Michael", "Natalie", "Noah", "Oliver", "Olivia", "Owen",
        "Ryan", "Samuel", "Sarah", "Sophia", "Thomas", "Victoria", "William", "Abigail", "Alexander", "Amelia",
        "Andrew", "Anna", "Anthony", "Ava", "Benjamin", "Charlotte", "Christopher", "Claire", "Daniel", "David",
        "Elizabeth", "Emily", "Emma", "Ethan", "Grace", "Hannah", "Henry", "Isabella", "Jacob", "James", "Joseph",
        "Joshua", "Liam", "Lily", "Lucas", "Madison", "Mason", "Matthew", "Mia", "Michael", "Natalie", "Noah",
        "Oliver", "Olivia", "Owen", "Ryan", "Samuel", "Sarah", "Sophia", "Thomas", "Victoria", "William",
        "Alexandra", "Alice", "Amber", "Ashley", "Audrey", "Austin", "Avery", "Brandon", "Brian", "Brooklyn",
        "Caleb", "Caroline", "Chloe", "Christian", "Christopher", "Claire", "Daniel", "David", "Eleanor", "Elijah",
        "Elizabeth", "Ella", "Ethan", "Evelyn", "Gabriel", "Grace", "Hailey", "Hannah", "Isaac", "Isabella", "Jack",
        "Jackson", "Jacob", "James", "Jason", "Jennifer", "John", "Jonathan", "Julia", "Julian", "Katherine",
        "Kevin", "Laura", "Lauren", "Leah", "Leo", "Levi", "Liam", "Lillian", "Alexander", "Alexey", "Andrey", "Anton",
        "Artem", "Boris", "Vasiliy", "Vladimir", "Georgy", "Gregory", "Denis", "Dmitry", "Evgeny", "Ivan", "Igor",
        "Ilya", "Kirill", "Konstantin", "Leo", "Leonid", "Maksim", "Michael", "Nikita", "Nikolay", "Oleg", "Pavel",
        "Peter", "Novel", "Sergei", "Stanislav", "Stepan", "Timofey", "Fedor", "Philip", "Yuri", "Yakov", "Abram",
        "Adam", "Azariy", "Akim"]
surname = ["Anderson", "Brown", "Clark", "Davis", "Evans", "Foster", "Garcia", "Hall", "Jackson", "Johnson", "King",
           "Lee", "Martinez", "Miller", "Moore", "Nelson", "Parker", "Robinson", "Rodriguez", "Smith", "Taylor",
           "Thomas", "Thompson", "Walker", "White", "Williams", "Wilson", "Young", "Adams", "Allen", "Baker",
           "Bennett", "Brooks", "Carter", "Cook", "Cooper", "Cruz", "Davis", "Edwards", "Flores", "Gonzalez",
           "Gray", "Green", "Harris", "Hernandez", "Hughes", "James", "Jenkins", "Jones", "Kelly",
           "Zhulev", "Romanyugin", "Atgeriev", "Rybakin", "Belonosov", "Litovtsev", "Pupynin", "Silin", "Fortieth",
           "Bakhterev", "Losenkov", "Efimkin", "Fedkov", "Muldakhmetov", "Perko", "Burziev", "Kornilin", "Podgorsky",
           "Samborsky", "Nozdrovsky", "Merezhnikov", "Aleshchukin", "Gudochkin", "Vitovsky", "Mamchenko", "Burmatov",
           "Malinovsky", "Aeroplanes", "Karachentsev", "Nikonorov", "Nurkadilov", "Borisevich", "Voropanov",
           "Abzalilov", "Skorobogatykh", "Balobin", "Baranyuk", "Barchukov", "Shvedchikov", "Kosyakov", "Antonikov",
           "Makar", "Borilko", "Bazylin", "Soloshenko", "Batalin", "Umergalin", "Murzaev", "Zhuravok", "Poskrebyshev"]

# specie(adult height	child's height	adult weight	child's weight	Life expectancy)
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

#with time
def gen_datetime(min_year=1960, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()

#staff
def gen_date(start_year, end_year):
    start = datetime(year=start_year, month=1, day=1)
    end = datetime(year=end_year, month=1, day=1)

    if start > end:
        end, start = start, end  # Поменять местами, если начальная дата больше

    return start + timedelta(days=random.randint(0, (end - start).days))

def generate_date(start_date, end_date):
    return start_date + timedelta(days=random.randint(1, (end_date - start_date).days))

def FileCreate(file_path, header, data_generator, num_entries):
    with open(file_path, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        for i in range(num_entries):
            csv_writer.writerow(data_generator(i))


def ProviderCreate(num):
    return [num, f"'{companyName_arr[num]}'"]


def AnimalCreate(num):
    specie = random.choice(specie_arr)
    birthday_date = generate_date(datetime.now() - timedelta(days=specie_dict[specie][4] * 365), entry_date_end)
    entry_date = generate_date(max(datetime.now() - timedelta(days=specie_dict[specie][4] * 365), birthday_date),
                               entry_date_end)

    difference = datetime.now() - entry_date
    height = 0
    weight = 0

    if difference > timedelta(days=specie_dict[specie][4] * 73):
        maturity = True
        height = round(random.uniform(specie_dict[specie][1], specie_dict[specie][0]), 2)
        weight = round(random.uniform(specie_dict[specie][3], specie_dict[specie][2]), 2)
    else:
        maturity = False
        height = round(random.uniform(1.0, specie_dict[specie][1]), 2)
        weight = round(random.uniform(1.0, specie_dict[specie][3]), 2)

    gender = random.choice(["Male", "Female"])

    return [num, f"'{random.choice(nickNames_arr)}'", f"'{birthday_date}::date'", f"'{entry_date}::date'",
            f"'{specie}'", maturity, weight, height, f"'{gender}'"]


# specie_id, name, is_predator, warm_aviary
#def SpecieCreate(num):
#    return [num, random.choice(specie_arr), random.choice(True, False), random.choice(True, False)]


def ZooCreate(num):
    return [num, f"'{zooName[num]}'", f"'{country[num]}'", f"'{city[num]}'"]


def StaffCreate(num):
    gender = random.choice(["F", "M"])
    today = datetime.today()

    start_date_birth = today - timedelta(days=365 * 18)
    end_date_birth = today - timedelta(days=365 * 18)
    birth_date = gen_date(end_date_birth.year - 18, end_date_birth.year)

    start_date_employment = birth_date + timedelta(days=365 * 18)
    end_date_employment = today
    date_of_employment = gen_date(start_date_employment.year, end_date_employment.year)

    salary = random.randint(25000, 250000)
    post = random.choice(
        ["veterinarians", "cleaners", "trainers", "construction repairmen", "administration workers"])

    return [f"'{random.choice(surname)}'", f"'{random.choice(name)}'", f"'{random.choice(name)}'", f"'{gender}'",
            f"'{birth_date.date()}'",
            f"'{date_of_employment.date()}'", salary, f"'{post}'"]

entry_date_start = datetime(2004, 11, 17)
entry_date_end = datetime.now()

#path = input("Введите путь для сохранения файла: ")
path = "C:/Users/Sonya/Documents/"
num_row = int(input("Введите количество строк: "))
num_row -= 1


#FileCreate(specie_file_path, ['specie_id', 'name', 'is_predator', 'warm_aviary'], SpecieCreate, num_row)
