##Блок 1 — Начальная строка vs Изменение
Начальный код:
    return Fighter(name, hp, attack)

Конечный код:
        MAX_HP = 50
    BASE_ATTACK = 8
    return Fighter(name, MAX_HP, BASE_ATTACK,)

Логика: вместо введённых hp и attack передаю константы MAX_HP = 50 и BASE_ATTACK = 8

##Блок 2 — create_fighter()
Начальный код:
def create_fighter():
    name = input("Введите имя бойца: ")
    hp = int(input("HP: "))
    attack = int(input("Сила удара: "))
    return Fighter(name, hp, attack)

##Конечный код:
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

Что добавилось: while True, проверка hp > 50 or hp <= 0 or attack > 8 or attack <= 0, print с ошибкой и границами, time.sleep(0.3), print("Попробуйте еще раз... \n"), else: return Fighter(...).

##Блок 3 — show_players()
Начальный код:
def show_players(players):
    for i in range(0, len(players)):
        print(f"{i+1}. {players[i].name}")
        print(f"HP: {players[i].hp}")

Конечный код:
def show_players(players: list):
    # Если все мертвы то сообщяем
    if not players:
        print("Нет живых бойцов...")
        return
        
    for i in range(len(players)):
        print(f"{i+1}. {players[i].name}")
        print(f"HP: {players[i].hp}")
        print(f"Атака: {players[i].attack}\n")

Что добавилось: аннотация players: list, проверка if not players с сообщением и return, вывод атаки, \n для отступа.

##Блок 4 — fight()
Начальный код:
def fight(a, b):
    while a.hp > 0 and  b.hp > 0:
        a.hp -= b.attack
        b.hp -= a.attack
        print(f"{a.name} - HP: {a.hp}")
        print(f"{b.name} - HP: {b.hp}")
        time.sleep(1)
    if a.hp == b.hp: print("Ничья!")
    else: print(a.name if a.hp > b.hp else b.name, "победил!")

Конечный код:
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

Что добавилось: аннотации a: Fighter, b: Fighter, print("Бой начался между ..."), HP обоих в одну строку через |, print("Бой окончен!"), ничья по a.hp <= 0 and b.hp <= 0 вместо ==, переменная winner, print(f"Победитель: {winner.name}!").

##Блок 5 — remove_dead()
Начальный код:
def remove_dead(players):
    for p in players:
        if p.hp <= 0:
            players.remove(p)

Конечный код:
def remove_dead(players: list):
    for p in players.copy(): #безопасный цикл по копии
        if p.hp <= 0:
            players.remove(p)
    return players

Что добавилось: аннотация players: list, players.copy() вместо players, комментарий #безопасный цикл по копии, return players.

##Блок 6 — Основной код
Начальный код:
players = []
for i in range(2):
    players.append(create_fighter())
show_players(players)
fight(players[0], players[1])
remove_dead(players)
show_players(players)

Конечный код:
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

Что добавилось: print(f"Создание бойца {i+1}:"), пустая строка после players = [], print("\nСписок участников:"), комментарий #Отсееваем погибших, players = remove_dead(players), print(f"\nОставшиеся в живых:").
