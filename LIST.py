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
