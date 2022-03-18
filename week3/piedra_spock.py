from cProfile import run
import json
import random

def search_by_id(id, data):
    for option in data:
        if option['id'] == id:
            return option

def user_validation():
    try:
        user_choice = int(input("Que eliges: "))
        if user_choice not in range(1,7):
            raise ValueError
    except ValueError:
        print("Solo son válidos números del 1-6")
    else:
        return user_choice

def action_message(win, lose, data):
    winner = search_by_id(win, data)
    action_index = winner['win'].index(lose)
    loser_name = search_by_id(lose, data)['name']
    return f"{winner['name']} {winner['actions'][action_index]} {loser_name}"

def rules_game(user, pc, data):
    if pc in search_by_id(user, data)['win']:
        print(f"Ganaste, {action_message(user, pc, data)}")
    elif user in search_by_id(pc, data)['win']:
        print(f"Perdiste, {action_message(pc, user, data)}")
    elif user == pc:
        print("Empate")

def new_game():
    try:
        again = input("Jugamos de nuevo? Si[S] No[N]: ").lower()
        if again not in ['s', 'n', 'si', 'no']:
            raise TypeError
    except TypeError:
            print("Valor de entrada invalido, los valores admitidos son (S) o (N)")
    else:
        return again



def run():
    with open('piedra-spock.json', 'r') as file:
        data = json.load(file)

    while True: 
        for option in data:
            print(option['id'], option['name'])
        print("6 Salir del Programa")
        
        user_choice = user_validation()
        if user_choice == 6:
            print("Nos vemos!")
            break
        else:
            print(f"Tu eliges: {search_by_id(user_choice, data)['name']}")

        pc_choice = random.randrange(1, 6)
        print(f"PC eligio: {search_by_id(pc_choice, data)['name']}")
        print("...")

        rules_game(user_choice, pc_choice, data)
        again = new_game()
        if again == "s" or again == "si":
            continue
        elif again == "n" or again == "no":
            print("Fue un placer, vuelve pronto")
            break


if __name__ == '__main__':
    run()