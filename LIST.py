import time


class Fighter:
    def __init__(self, name: str, hp: int, attack: int):
        self.name = name
        self.hp = hp
        self.attack = attack

    @property
    def is_alive(self):
        return self.hp > 0


def create_fighter():
    while True:
        name = input("Введите имя бойца: ")
        hp = int(input("HP: "))
        attack = int(input("Сила удара: "))

        if 0 < hp <= 50 and 0 < attack <= 8:
            return Fighter(name, hp, attack)

        print("Неправильные данные! (HP: 1-50, атака: 1-8)")
        time.sleep(0.3)
        print("Попробуйте еще раз...\n")


def show_players(players: list):
    if not players:
        print("Нет живых бойцов...")
        return

    for i, p in enumerate(players, start=1):
        print(f"{i}. {p.name}")
        print(f"HP: {p.hp}")
        print(f"Атака: {p.attack}\n")


def fight(a: Fighter, b: Fighter):
    print(f"Бой начался между {a.name} и {b.name}!")

    attacker, defender = a, b
    while a.is_alive and b.is_alive:
        defender.hp -= attacker.attack
        print(f"{a.name} - HP: {max(a.hp, 0)} | {b.name} - HP: {max(b.hp, 0)}")
        time.sleep(1)
        attacker, defender = defender, attacker

    print("Бой окончен!")

    if not a.is_alive and not b.is_alive:
        print("Ничья!")
    else:
        winner = a if a.is_alive else b
        print(f"Победитель: {winner.name}!")


def remove_dead(players: list):
    return [p for p in players if p.is_alive]


players = []

for i in range(2):
    print(f"Создание бойца {i + 1}:")
    players.append(create_fighter())

print("\nСписок участников:")
show_players(players)

fight(players[0], players[1])

players = remove_dead(players)

print("\nОставшиеся в живых:")
show_players(players)
