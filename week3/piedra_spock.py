import json
import random

with open('piedra-spock.json', 'r') as file:
    data = json.load(file)

while True: 
    random_number = random.randrange(0, 5)
    choose_pc = ""
    for rule in data['rules']:
        print(rule['id'], rule['name'])
    print("6 Salir del Programa")
    choose_user = int(input("Que eliges: "))

    user_validation()
    


