import time
import random


class Fighter:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.alive = True
        self.money = 0

    def is_alive(self):
        return self.alive

    def is_dead(self):
        return not self.alive

    def hit(self, damage):
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def attack_enemy(self, enemy):
        # тут ничего нет — это делают наследники
        pass

    def fight(self, other):
        while self.is_alive() and other.is_alive():
            self.attack_enemy(other)
            if other.is_alive():
                other.attack_enemy(self)
            print(self.name, "- HP:", self.hp)
            print(other.name, "- HP:", other.hp)
            time.sleep(1)

        if self.hp == other.hp:
            print("Ничья!")
        elif self.hp > other.hp:
            print(self.name, "победил!")
        else:
            print(other.name, "победил!")

    def __add__(self, other):
        new = Fighter(
            self.name + other.name,
            self.hp + other.hp,
            self.attack + other.attack
        )
        new.money = self.money + other.money
        return new

    def __repr__(self):
        return self.name + " [HP: " + str(self.hp) + "]"


# ===== наследники =====

class Warrior(Fighter):
    def hit(self, damage):
        damage = damage - 2
        if damage < 1:
            damage = 1
        self.hp = self.hp - damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def attack_enemy(self, enemy):
        print("Воин", self.name, "рубит мечом!")
        enemy.hit(self.attack)


class Assassin(Fighter):
    def attack_enemy(self, enemy):
        if random.random() < 0.3:
            damage = self.attack * 2
            print("Ассасин", self.name, "КРИТ:", damage)
        else:
            damage = self.attack
            print("Ассасин", self.name, "бьёт кинжалом:", damage)
        enemy.hit(damage)


class Mage(Fighter):
    def attack_enemy(self, enemy):
        print("Маг", self.name, "кидает огонь:", self.attack)
        enemy.hit(self.attack)

        heal = self.attack // 2
        self.hp = self.hp + heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print("Маг", self.name, "лечится на", heal)


# ===== проверка =====

w = Warrior("Арагорн", 120, 15)
a = Assassin("Локи", 80, 20)
m = Mage("Гэндальф", 90, 18)

players = [w, a, m]

for p in players:
    print(p)

print()
print("--- бой ---")
w.fight(m)

print()
print("--- сложение ---")
fusion = w + a
print(fusion)

# убираем мёртвых
alive = []
for p in players:
    if p.is_alive():
        alive.append(p)
players = alive

print()
print("живые:")
for p in players:
    print(p)
