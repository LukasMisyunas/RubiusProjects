import time
import random


class Fighter:
    """Обычный боец. От него будем делать других."""

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack

    def is_alive(self):
        # Живой, если hp больше нуля
        return self.hp > 0

    def hit(self, damage):
        # Получить урон
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        # В базовом классе не знаем, как бить — это делают наследники
        pass

    def fight(self, enemy):
        # Бой 1 на 1
        while self.is_alive() and enemy.is_alive():
            self.attack_enemy(enemy)
            if enemy.is_alive():       # мёртвый не отвечает
                enemy.attack_enemy(self)

            print(self.name, "-", self.hp, "HP  |  ", enemy.name, "-", enemy.hp, "HP")
            time.sleep(1)

        if self.hp == enemy.hp:
            print("Ничья!")
            return None
        elif self.hp > enemy.hp:
            print(self.name, "победил!")
            return self
        else:
            print(enemy.name, "победил!")
            return enemy

    def __add__(self, other):
        # Складываем двух бойцов в одного нового
        new_name = self.name + "+" + other.name
        new_hp = self.hp + other.hp
        new_attack = self.attack + other.attack
        return Fighter(new_name, new_hp, new_attack)

    def __str__(self):
        return self.name + " [" + str(self.hp) + "/" + str(self.max_hp) + " HP]"


# ===== Наследники =====

class Warrior(Fighter):
    """Воин — крепкий, получает меньше урона."""

    def hit(self, damage):
        # Броня: урон минус 2, но хотя бы 1
        damage = damage - 2
        if damage < 1:
            damage = 1
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0

    def attack_enemy(self, enemy):
        print("Воин", self.name, "рубит мечом!")
        enemy.hit(self.attack)


class Assassin(Fighter):
    """Ассасин — иногда бьёт в два раза сильнее."""

    def attack_enemy(self, enemy):
        if random.random() < 0.3:      # 30% шанс крита
            damage = self.attack * 2
            print("Ассасин", self.name, "наносит КРИТ:", damage)
        else:
            damage = self.attack
            print("Ассасин", self.name, "бьёт кинжалом:", damage)
        enemy.hit(damage)


class Mage(Fighter):
    """Маг — лечится, когда бьёт."""

    def attack_enemy(self, enemy):
        print("Маг", self.name, "кидает огненный шар:", self.attack)
        enemy.hit(self.attack)

        # Восстанавливаем половину от своего удара
        heal = self.attack // 2
        self.hp = self.hp + heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print("Маг", self.name, "лечится на", heal, "HP")


# ===== Проверка =====

warrior = Warrior("Арагорн", 120, 15)
assassin = Assassin("Локи", 80, 20)
mage = Mage("Гэндальф", 90, 18)

print(warrior)
print(assassin)
print(mage)

print("\n--- Бой ---")
warrior.fight(mage)

print("\n--- Сложение ---")
fusion = warrior + assassin
print(fusion)
