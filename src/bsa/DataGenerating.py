import os
import csv
import datetime
import random
from datetime import datetime, timedelta

yourPath = "C:/Users/Sonya/Documents/"


def gen_datetime(min_year=1960, max_year=datetime.now().year):
    start = datetime(min_year, 1, 1, 00, 00, 00)
    years = max_year - min_year + 1
    end = start + timedelta(days=365 * years)
    return start + (end - start) * random.random()


def CreateProviders(num):
    companyName = ["Pet Paradise", "Paws and Claws Emporium", "Furry Friends Haven", "The Critter Corner",
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
    csvFile = os.path.join(yourPath, "Providers.csv")
    with open(csvFile, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(["Id_provider", "Name_provider"])
        for i in range(num):
            csvWriter.writerow([i + 1, companyName[i]])


def CreateAnimals(num):
    nickNames = ["Shadow", "Sunny", "Buddy", "Lucky", "Rocky", "Princess", "Max", "Lucy", "Daisy", "Charlie", "Coco",
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
    csvFile = os.path.join(yourPath, "Animals.csv")
    with open(csvFile, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(['Id_animal', "Nickname", "Birthday", "Maturity", "Age", "Gender", "Species"])
        for i in range(num):
            maturity = random.choice(["да", "нет"])
            age = random.randint(3, 70)
            gender = random.choice(["Самка", "Самец"])
            csvWriter.writerow(
                [i + 1, random.choice(nickNames), gen_datetime(), maturity, age, gender, random.choice(species)])


def CreateZoos(num):
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
    csvFile = os.path.join(yourPath, "Zoos.csv")
    with open(csvFile, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(['Id_zoo', "NameZoo", "Country", "City"])
        for i in range(num):
            csvWriter.writerow([i + 1, zooName[i], country[i], city[i]])


def CreateEmployees(num):
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
            "Kevin", "Laura", "Lauren", "Leah", "Leo", "Levi", "Liam", "Lillian"]
    surname = ["Anderson", "Brown", "Clark", "Davis", "Evans", "Foster", "Garcia", "Hall", "Jackson", "Johnson", "King",
               "Lee", "Martinez", "Miller", "Moore", "Nelson", "Parker", "Robinson", "Rodriguez", "Smith", "Taylor",
               "Thomas", "Thompson", "Walker", "White", "Williams", "Wilson", "Young", "Adams", "Allen", "Baker",
               "Bennett", "Brooks", "Carter", "Cook", "Cooper", "Cruz", "Davis", "Edwards", "Flores", "Gonzalez",
               "Gray", "Green", "Harris", "Hernandez", "Hughes", "James", "Jenkins", "Jones", "Kelly"]
    csvFile = os.path.join(yourPath, "Employees.csv")
    with open(csvFile, 'w', newline='') as file:
        csvWriter = csv.writer(file)
        csvWriter.writerow(
            ["Id_employee", "Surname", "Name", "Patronymic", "Gener", "Age", "DateOfEmployment", "Salary", "Post"])
        for i in range(num):
            gender = random.choice(["F", "M"])
            age = random.randint(18, 90)
            salary = random.randint(25000, 250000)
            post = random.choice(
                ["veterinarians", "cleaners", "trainers", "construction repairmen", "administration workers"])
            csvWriter.writerow(
                [i + 1, random.choice(surname), random.choice(name), random.choice(name), gender, age, gen_datetime(),
                 salary, post])


path = input("Введите путь для сохранения файла: ")
num_provider = int(input("Введите количество поставщиков: "))
num_animal = int(input("Введите количество животных: "))
num_zoo = int(input("Введите количество зоопарков: "))
num_employee = int(input("Введите количество работников: "))

CreateProviders(num_provider)
CreateAnimals(num_animal)
CreateZoos(num_zoo)
CreateEmployees(num_employee)
