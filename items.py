import sys


class Potion(object):
    def __init__(self, amount=2):
        self.name = "Potion"
        self.ammount = amount

    def effect(self, user):
        #gains 10 hp
        user.hp += 10
        if user.hp > user.maxhp:
            user.hp = user.maxhp


class SuperPotion(object):
    def __init__(self, amount=1):
        self.name = "Super Potion"
        self.ammount = amount

    def effect(self, user):
        #gains 20 hp
        user.hp += 20
        if user.hp > user.maxhp:
            user.hp = user.maxhp