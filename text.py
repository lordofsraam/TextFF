from random import randint as rand
import sys
from items import *


def dprint(s):
    print s


def itemcount(lst, tpe):
    return len([item for item in lst if isinstance(item, tpe)])


class Fighter:
    def __init__(self, name, hp, mp, att, defense, spd, acc, intel, run, itemlist={}):
        self.maxhp = 100
        self.name = name
        self.hp = hp
        self.mp = mp
        self.att = att
        self.defense = defense
        self.intel = intel
        self.spd = spd
        self.acc = acc
        self.run = run
        self.reset = True
        self.mobroll = rand(1, 10)
        self.itemlist = [Potion(), Potion(), SuperPotion()]

    def playername(self):
        print self.name

    def space(self):
        pass

    def health(self):
        if self.hp > 0:
            str_hp = "="*(self.hp/10)
            print "[" + str_hp + " "*(10-len(str_hp)) + "]" + " " + str(self.hp) + "/" + str(self.maxhp) + "\n"
        else:
            print "[" + " DEAD! " + "] \n"
            print self.name + "has been defeated!"
            sys.exit()

    def fight(self, opponent):
        #roll 1-20, 19,20 crit, crit dmg val x2
        print("Using attack value: " + str(self.att) + "\n")
        hitluck = rand(1, 10)
        if self.acc >= opponent.spd or hitluck > 6:
            crit = rand(1, 20)
            dprint("Using crit value (1-20): " + str(crit) + "\n")
            if crit > 18:
                print self.name + " has struck a critical blow! \n"
                print self.name, "has dealt", self.att*2, "damage to", opponent.name, "\n"
                opponent.hp -= self.att*2
            else:
                print self.name, "has dealt", self.att, "damage to", opponent.name, "\n"
                opponent.hp -= self.att
        else:
            print self.name + " missed! \n"

    def skill(self):
        pass

    def magic(self):
        pass

    def useitem(self, it):
        theitem = None
        for i in self.itemlist:
            if isinstance(i, it):
                theitem = i
                break
        theitem.effect(self)
        del self.itemlist[self.itemlist.index(theitem)]

    def item(self):
        if len(self.itemlist) > 0:
            potion_num = itemcount(self.itemlist, Potion)
            superpotion_num = itemcount(self.itemlist, SuperPotion)
            print "\nWhich item would you like to use?: \n"

            while True:
                if potion_num > 0:
                    print "[" + "potion" + "  x" + str(potion_num) + "]"
                if superpotion_num > 0:
                    print "[" + "super potion" + "  x" + str(superpotion_num) + "]"
                print "[Exit]"
                itemaction = raw_input(":")
                if itemaction == "potion":
                    self.useitem(Potion)
                    print "\n" + self.name + " gained 10 health!"
                    break
                elif itemaction == "super potion":
                    self.useitem(SuperPotion)
                    print "\n" + self.name + " gained 20 health!"
                    break
                elif itemaction == "exit" or "Exit":
                    self.reset = True
                    break
                else:
                    print "You have not typed a valid option!"

        else:
            print "\nYou have no items!\n"
            self.reset = True


    def escape(self):
        if self.mobroll > 8:
            print self.name + " cannot run from this battle! \n"
            self.reset = True
        else:
            runcheck = rand(0, 100)
            if runcheck >= 75:
                print self.name + " has successfully fled from battle!"
                sys.exit()
            else:
                print self.name + " has failed to flee from battle! \n"


    def autoturn(self):
        print "\n" + self.name + "'s Turn! \n" + "========================== \n"
        autoroll = rand(7, 10)
        if autoroll >= 7 and autoroll < 9:
            badguy.fight(goodguy)
        #elif autoroll >= 4 and autoroll < 7:
            #print "hey"
            #  skill
        #elif autoroll >= 7 and autoroll < 10:
            #pass
            #  magic
        if autoroll == 10:
            badguy.escape()

goodguy = Fighter("Thunder", rand(20, 100), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10))

badguy = Fighter("Dark-Death Evilman", rand(20, 100), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10))

def heroturn():
    #Hero Turn
    #while goodguy.Run == "no":
    #If run is successful, the encounter ends.
    goodguy.reset = True
    while goodguy.reset:
    #resets menu in case of incorrect input and "cant escape"
        goodguy.reset = False
        healthstat()
        print "\n" + goodguy.name + "'s turn!\n========================"
        action = raw_input("What do you want to do?: \n(Fight, Skill, Magic, Item, Run)\n:")
        if action == "Fight":
            goodguy.fight(badguy)
            healthstat()
        elif action == "Skill":
            goodguy.skill()
        elif action == "Magic":
            goodguy.magic()
        elif action == "Item":
            goodguy.item()
        elif action == "Run":
            goodguy.escape()
        else:
            print "Incorrect input, Try Again.\n"
            goodguy.reset = True



def healthstat():
    goodguy.playername()
    goodguy.health()
    badguy.playername()
    badguy.health()

#Que enemy
print "Wild " + badguy.name + " Appeared!" + "\n" + "================================="

while True:
    heroturn()
    badguy.autoturn()