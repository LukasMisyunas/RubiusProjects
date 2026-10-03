import time

class Fighter:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.__is_alive = True
        self.__money = 0

    def __add__(self, other):
        new = Fighter(
            self.name + other.name,
            self.hp + other.hp,
            self.attack + other.attack
        )
        new.__money = self.__money + other.__money
        return new

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.__is_alive = False

    def is_alive(self):
        return self.__is_alive

    def is_dead(self):
        return not self.__is_alive

    def __repr__(self):
        return f"{self.name} [HP: {self.hp}]"

    def __str__(self):
        return self.__repr__()

    def fight(self, other):
        while self.is_alive() and other.is_alive():
            other.hit(self.attack)
            if other.is_alive():
                self.hit(other.attack)
            print(f"{self.name} - HP: {self.hp}")
            print(f"{other.name} - HP: {other.hp}")
            time.sleep(1)
        if self.hp == other.hp:
            print("Ничья!")
        else:
            print(self.name if self.hp > other.hp else other.name, "победил!")


def create_fighter():
    name = input("Введите имя бойца: ")
    hp = int(input("HP: "))
    attack = int(input("Сила удара: "))
    return Fighter(name, hp, attack)


# ===== проверка =====
players = []
for i in range(2):
    players.append(create_fighter())

print(players[0])
print(players[1])

print(players[0] + players[1])

players[0].fight(players[1])

# убираем мёртвых
alive = []
for p in players:
    if p.is_alive():
        alive.append(p)
players = alive
print("Живые:", players)
