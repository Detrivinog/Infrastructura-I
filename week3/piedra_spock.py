from cProfile import run
import json
import random

def search_by_id(id, data):
    for option in data:
        if option['id'] == id:
            return option

def percentage(user_score, pc_score):
    if user_score == 0:
        return user_score
    else:
        return user_score*100/(user_score + pc_score)

def print_score(user_score, pc_score):
    print("---" * 10)
    print(f'Puntajes: \nUsuario: {user_score} puntos \nPC: {pc_score} puntos')
    print(f'Porcentaje de victorias: {percentage(user_score, pc_score):.1f}%')

def action_message(win, lose, data):
    winner = search_by_id(win, data)
    action_index = winner['win'].index(lose)
    loser_name = search_by_id(lose, data)['name']
    return f"{winner['name']} {winner['actions'][action_index]} {loser_name}"

def rules_game(user, pc, data, user_points, pc_points):
    if pc in search_by_id(user, data)['win']:
        print(f"Ganaste, {action_message(user, pc, data)}")
        user_points += 1
    elif user in search_by_id(pc, data)['win']:
        print(f"Perdiste, {action_message(pc, user, data)}")
        pc_points += 1
    elif user == pc:
        print("Empate")
    return user_points, pc_points

def new_game():
    try:
        again = input("Jugamos de nuevo? Si[S] No[N]: ").lower()
        if again not in ['s', 'n', 'si', 'no']:
            raise TypeError
    except TypeError:
            print("Valor de entrada invalido, los valores admitidos son (S) o (N)\nSi desea salir del programa ingrese el número 7")
    else:
        return again

def run():
    with open('piedra-spock.json', 'r') as file:
        data = json.load(file)

    user_points = 0
    pc_points = 0
    while True:
        print("---" * 10) 
        for option in data:
            print(option['id'], option['name'])
        print("6 Mostrar puntajes")
        print("7 Salir del Programa")
        print("---" * 10)
        try:
            user_input = input("Que eliges: ")
            if not user_input.isnumeric():
                raise TypeError
            elif user_input.isnumeric():
                user_input = int(user_input)
                if user_input not in range(1,8):
                    raise ValueError("Solo son válidos números del 1-7")
                user_choice = user_input
        except ValueError as ve:
            print(ve)
            continue
        except TypeError:
            print("Solo son válidos números")
            continue

        if user_choice == 6:
            print_score(user_points, pc_points)
            continue
        elif user_choice == 7:
            print_score(user_points, pc_points)
            print("---" * 10)
            print("Nos vemos!")
            break
        elif user_choice in range(1,8):
            print(f"Tu eliges: {search_by_id(user_choice, data)['name']}")

        pc_choice = random.randrange(1, 6)
        print(f"PC eligio: {search_by_id(pc_choice, data)['name']}")
        print("---" * 10)

        user_points, pc_points = rules_game(user_choice, pc_choice, data, user_points, pc_points)
        print("---" * 10)
        again = new_game()
        if again == "s" or again == "si":
            continue
        elif again == "n" or again == "no":
            print("Fue un placer, vuelve pronto")
            break

if __name__ == '__main__':
    run()