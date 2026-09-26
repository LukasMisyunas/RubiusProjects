#---------1. Класс Fighter — добавил аннотации типов---------------
#Было:  
def __init__(self, name, hp, attack):
#Стало: 
def __init__(self, name: str, hp: int, attack: int):

#-2. create_fighter() — добавил цикл, проверку, константы, sleep---
#Было:
    name = input("Введите имя бойца: ")
    hp = int(input("HP: "))
    attack = int(input("Сила удара: "))
    return Fighter(name, hp, attack)
#Стало:
    MAX_HP = 50
    BASE_ATTACK = 8
    while True: #беск цикл
        name = input("Введите имя бойца: ")
        hp = int(input("HP: "))
        attack = int(input("Сила удара: "))
        # Проверка корректности введенных данных
        if hp > 50 or hp <= 0 or attack > 8 or attack <= 0:
            print(f"Вы ввели неправильные данные! (Макс HP: 50, Мин HP: 1; Макс атака: 8, Мин атака: 1)")
            time.sleep(0.3)
            print(f"Попробуйте еще раз... \n")
        else:
            return Fighter(name, hp, attack)

#3.--- show_players() — добавил аннотацию, проверку пустоты, вывод атаки----
#Было:
    for i in range(0, len(players)):
        print(f"{i+1}. {players[i].name}")
        print(f"HP: {players[i].hp}")
#Стало:
def show_players(players: list):
    # Если все мертвы то сообщяем
    if not players:
        print("Нет живых бойцов...")
        return
    for i in range(len(players)):
        print(f"{i+1}. {players[i].name}")
        print(f"HP: {players[i].hp}")
        print(f"Атака: {players[i].attack}\n")

#4. fight() — добавил аннотации, сообщения, ничью по <=0, winner
#Было:
    while a.hp > 0 and  b.hp > 0:
        a.hp -= b.attack
        b.hp -= a.attack
        print(f"{a.name} - HP: {a.hp}")
        print(f"{b.name} - HP: {b.hp}")
        time.sleep(1)
    if a.hp == b.hp: print("Ничья!")
    else: print(a.name if a.hp > b.hp else b.name, "победил!")
#Стало:
def fight(a: Fighter, b: Fighter):
    print(f"Бой начался между {a.name} и {b.name}!")
    while a.hp > 0 and b.hp > 0:
        a.hp -= b.attack
        b.hp -= a.attack
        print(f"{a.name} - HP: {a.hp} | {b.name} - HP: {b.hp}")
        time.sleep(1)
    print("Бой окончен!")
    if a.hp <= 0 and b.hp <= 0:
        print("Ничья!")
    else:
        if a.hp > b.hp:
            winner = a
        else:
            winner = b
        print(f"Победитель: {winner.name}!")

#5. remove_dead() — добавил аннотацию, copy, return
#Было:
    for p in players:
        if p.hp <= 0:
            players.remove(p)
#Стало:
def remove_dead(players: list):
    for p in players.copy(): #безопасный цикл по копии
        if p.hp <= 0:
            players.remove(p)
    return players

#6. Основной код — добавил подписи, присвоение результата
#Было:
players = []
for i in range(2):
    players.append(create_fighter())
show_players(players)
fight(players[0], players[1])
remove_dead(players)
show_players(players)
#Стало:
players = []
for i in range(2):
    print(f"Создание бойца {i+1}:")
    players.append(create_fighter())
print("\nСписок участников:")
show_players(players)
fight(players[0], players[1])
#Отсееваем погибших
players = remove_dead(players)
print(f"\nОставшиеся в живых:")
show_players(players)

#================итоговый код=================
#================итоговый код=================
#================итоговый код=================

import time

class Fighter:
    def __init__(self, name: str, hp: int, attack: int):
        self.name = name
        self.hp = hp
        self.attack = attack

def create_fighter():
    while True: #беск цикл
        name = input("Введите имя бойца: ")
        hp = int(input("HP: "))
        attack = int(input("Сила удара: "))
        
        # Проверка корректности введенных данных
        if hp > 50 or hp <= 0 or attack > 8 or attack <= 0:
            print(f"Вы ввели неправильные данные! (Макс HP: 50, Мин HP: 1; Макс атака: 8, Мин атака: 1)")
            time.sleep(0.3)
            print(f"Попробуйте еще раз... \n")
        else:
            return Fighter(name, hp, attack)

def show_players(players: list):
    # Если все мертвы то сообщяем
    if not players:
        print("Нет живых бойцов...")
        return
        
    for i in range(len(players)):
        print(f"{i+1}. {players[i].name}")
        print(f"HP: {players[i].hp}")
        print(f"Атака: {players[i].attack}\n")

def fight(a: Fighter, b: Fighter):
    print(f"Бой начался между {a.name} и {b.name}!")
    while a.hp > 0 and b.hp > 0:
        a.hp -= b.attack
        b.hp -= a.attack
        print(f"{a.name} - HP: {a.hp} | {b.name} - HP: {b.hp}")
        time.sleep(1)
    print("Бой окончен!")
    if a.hp <= 0 and b.hp <= 0:
        print("Ничья!")
    else:
        if a.hp > b.hp:
            winner = a
        else:
            winner = b
        print(f"Победитель: {winner.name}!")        

def remove_dead(players: list):
    for p in players.copy(): #безопасный цикл по копии
        if p.hp <= 0:
            players.remove(p)
    return players

players = []

for i in range(2):
    print(f"Создание бойца {i+1}:")
    players.append(create_fighter())

print("\nСписок участников:")
show_players(players)

fight(players[0], players[1])

#Отсееваем погибших
players = remove_dead(players)

print(f"\nОставшиеся в живых:")
show_players(players)

