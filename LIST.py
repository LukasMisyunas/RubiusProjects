import time


class Fighter:
    def __init__(self, name: str, hp: int, attack: int):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0


def create_fighter(number):
    while True:
        print(f"Создание бойца {number}:")
        name = input("Введите имя бойца: ")
        try:
            hp = int(input("HP: "))
            attack = int(input("Сила удара: "))
        except ValueError:
            print("Нужно вводить числа!\n")
            continue

        if 0 < hp <= 50 and 0 < attack <= 8:
            return Fighter(name, hp, attack)

        print("Неправильные данные! (HP: 1-50, атака: 1-8)")
        time.sleep(0.3)
        print("Попробуйте еще раз...\n")


def show_players(players):
    if not players:
        print("Нет живых бойцов...")
        return

    for i, p in enumerate(players, start=1):
        print(f"{i}. {p.name}")
        print(f"HP: {p.hp}")
        print(f"Атака: {p.attack}\n")


def fight(a, b):
    print(f"\nБой начался между {a.name} и {b.name}!")

    first_turn = True  # True = ход "a", False = ход "b"

    while a.is_alive() and b.is_alive():
        if first_turn:
            b.hp -= a.attack
            print(f"{a.name} бьёт {b.name}. У {b.name} осталось {max(b.hp, 0)} HP")
        else:
            a.hp -= b.attack
            print(f"{b.name} бьёт {a.name}. У {a.name} осталось {max(a.hp, 0)} HP")

        first_turn = not first_turn
        time.sleep(1)

    print("Бой окончен!")

    if not a.is_alive() and not b.is_alive():
        print("Ничья!")
    else:
        winner = a if a.is_alive() else b
        print(f"Победитель: {winner.name}!")


players = [create_fighter(1), create_fighter(2)]

print("\nСписок участников:")
show_players(players)

fight(players[0], players[1])

players = [p for p in players if p.is_alive()]

print("\nОставшиеся в живых:")
show_players(players)
