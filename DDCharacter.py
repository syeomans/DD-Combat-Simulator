from random import *
import pickle

# Functions used in class definition
from DDFunctions import *

# Character class
class Player:
    def __init__(self, Name, Race, Class, Str, Dex, Con, Int, Wis, Cha, Xp):
        #initial stats from input
        self.name = Name
        self.race = Race
        self.Class = Class
        self.strength = Str
        self.dexterity = Dex
        self.constitution = Con
        self.intelligence = Int
        self.wisdom = Wis
        self.charisma = Cha
        self.xp = Xp

        #initially calculated stats (not from inputs)
        self.Lv = findLevel(Xp)
        self.strMod = (self.strength-10)/2
        self.dexMod = (self.dexterity-10)/2
        self.conMod = (self.constitution-10)/2
        self.intMod = (self.intelligence-10)/2
        self.wisMod = (self.wisdom-10)/2
        self.chaMod = (self.charisma-10)/2
        self.proficiency = calProf(self.Lv)
        self.hitDie = findHitDie(Class)
        self.maxHealth = self.hitDie
        self.currentHealth = self.maxHealth
        self.aprof = profsDict[Class]['Armor']
        self.wprof = profsDict[Class]['Weapons']
        self.tprof = profsDict[Class]['Tools']
        self.stprof = profsDict[Class]['Saving Throws']
        self.skprof = profsDict[Class]['Skills']
        self.inventory = {'Armor':{},'Weapons':{},'Tools':{},'Apparel':{},'Potions':{},'Purse':{},'Other':{}}
        self.equippedWeapon = {'DC':'1d1','Base price':0, 'Weight':0}
        self.equippedArmor = {'AC':10,'Base price':0, 'Weight':0}

        #create save file
        saveFile = open(Name + ".sav", "wb")
        pickle.dump(self, saveFile)
        saveFile.close()

    def save(self):
        saveFile = open(self.name + ".sav", "wb")
        pickle.dump(self, saveFile)
        saveFile.close()

    def attack(self, ac, adv = 'n'):
        if adv == 'n':
            attackRoll = randrange(1,21) + self.strMod + self.proficiency
        elif adv == 'a':
            roll1 = randrange(1,21) + self.strMod + self.proficiency
            roll2 = randrange(1,21) + self.strMod + self.proficiency
            rollList = [roll1,roll2]
            attackRoll = max(rollList)
        elif adv == 'd':
            roll1 = randrange(1,21) + self.strMod + self.proficiency
            roll2 = randrange(1,21) + self.strMod + self.proficiency
            rollList = [roll1,roll2]
            attackRoll = min(rollList)
        if attackRoll < ac:
            print 'Miss'
            return 'Miss'
        else:
            damage = damageRoll(self.equippedWeapon['DC']) + self.strMod
            if attackRoll == 20:
                damage += damageRoll(self.equippedWeapon['DC'])
                print 'Critical hit!'
            print damage
            return damage

    def heal(self, damage):
        if self.currentHealth <=0:
            uncon = True
        else:
            uncon = False
        if type(damage)==int:
            self.currentHealth += damage
        elif type(damage)==str:
            damage = damageRoll(damage)
            self.currentHealth += damage
        if self.currentHealth > self.maxHealth:
            self.currentHealth = self.maxHealth
        print('Healed'+self.name + " for " + str(damage) + " points.")
        print('Current health: '+str(self.currentHealth))
        if uncon and self.currentHealth >0:
            print(self.name+' is no longer unconscious.')

    def hit(self, damage):
        if type(damage)==int:
            self.currentHealth -= damage
        elif type(damage)==str:
            damage = damageRoll(damage)
            self.currentHealth -= damage
        print(self.name + " took " + str(damage) + " damage.")
        print('Current health: '+str(self.currentHealth))
        if self.currentHealth <= 0:
            print(self.name+' fell unconscious.')
        self.save()

    def stats(self):
        out = "Str: "+str(self.strength)+"\nDex: "+str(self.dexterity)+"\nCon: "+str(self.constitution)
        out = out+"\nInt: "+str(self.intelligence)+"\nWis: "+str(self.wisdom)+"\nCha: "+str(self.charisma)
        return(out)

    def increaseHealth(self): #not intended for player use
        while True:
            usrIn = str(raw_input("Increase health as average or roll? (Enter 'a' or 'r'): "))
            if usrIn =="a":
                newHealth = self.hitDie/2 + 1 + self.conMod
                break
            if usrIn == "r":
                newHealth = randrange(1,self.hitDie+1) + self.conMod
                break
        return newHealth

    def xp(self, points):
        oldLv = self.Lv
        self.xp += points
        newLv = findLevel(self.xp)
        if newLv > oldLv: #if level increased NOTE: assuming level increased by 1
            self.Lv = newLv
            print("Level up! " + self.name + " is now level " + str(self.Lv))
            hIncr= self.increaseHealth()
            self.maxHealth += hIncr
            self.currentHealth += hIncr
            self.proficiency = calProf(self.Lv)
        self.save()

    def setStat(self,stat, value):
        exstr = "self." + str(stat) + "=" + str(value)
        exec exstr
        self.save()

    def addProf(self, pr, val):
        exstr = 'self.' + pr + 'prof.append("' + val + '")'
        exec exstr
        self.save()

    def removeProf(self, pr, val):
        exstr = 'self.' + pr + 'prof.remove("' + val + '")'
        exec exstr
        self.save()

    def check(self, stat, skill, val, adv='n'):
        """ex: Bruenor.check('Dex','Acrobatics',10)
                saving throw example: Bruenor.check('Dex','none',10)"""
        #Check if proficiency is added
        pbonus = 0
        if stat in self.stprof:
            pbonus = self.proficiency
        elif skill in self.skprof:
            pbonus = self.proficiency
        exstr = 'mod = self.'+stat[:3].lower()+'Mod + pbonus'
        exec exstr
        #Check if (dis)advantage is given
        if adv == 'n':
            roll = randrange(1,21)+mod
            if roll < val:
                print "Failed check (" + str(roll) +')'
                return("Fail")
            else:
                print "Passed check (" + str(roll) +')'
                return("Pass")
        elif adv == 'a':
            roll1 = randrange(1,21)+mod
            roll2 = randrange(1,21)+mod
            roll = max([roll1, roll2])
            if roll < val:
                print "Failed check (" + str(roll) +')'
                return("Fail")
            else:
                print "Passed check (" + str(roll) +')'
                return("Pass")
        elif adv == 'd':
            roll1 = randrange(1,21)+mod
            roll2 = randrange(1,21)+mod
            roll = min([roll1, roll2])
            if roll < val:
                print "Failed check (" + str(roll) +')'
                return("Fail")
            else:
                print "Passed check (" + str(roll) +')'
                return("Pass")

    def addItem(self,typ,nam,pri,wt,acdc='',prop='',dam=''):
        if typ == 'Armor' or typ == 'Armors':
            self.inventory['Armor'][nam]={'AC':acdc,'Armor type':prop,'Base price':pri,'Weight':wt}
        elif typ == 'Weapon' or typ == 'Weapons':
            self.inventory['Weapons'][nam]={'DC':acdc,'Property':prop,'Damage type':dam,'Base price':pri,'Weight':wt}
        elif typ == 'Tool' or typ == 'Tools':
            self.inventory['Tools'][nam]={'Base price':pri,'Weight':wt}
        elif typ == 'Potion' or typ == 'Potions':
            self.inventory['Potions'][nam]={'Base price':pri,'Weight':wt}
        else:
            self.inventory[typ][nam]={'Base price':pri,'Weight':wt}
        self.save()

    def removeItem(self, nam):
        for key in self.inventory.keys():
            try:
                del self.inventory[key][nam]
            except:
                pass
        self.save()

    def draw(self,nam):
        if nam in self.inventory['Weapons']:
            self.equippedWeapon = self.inventory['Weapons'][nam]
            self.save()
        else:
            print nam+' is not in '+self.name+"'s inventory."

    def sheath(self):
        self.equippedWeapon = {'DC':'1d1','Base price':0, 'Weight':0}
        self.save()

    def don(self,nam):
        if nam in self.inventory['Armor']:
            self.save()
        else:
            print nam+' is not in '+self.name+"'s inventory."

    def doff(self):
        self.equippedArmor = {'AC':10,'Base price':0, 'Weight':0}
        self.save()

    def viewInventory(self,typ=''):
        if typ == '':
            for key in self.inventory.keys():
                print str(key)+': '+str(self.inventory[key].keys())
        else:
            print self.inventory[typ.capitalize()].keys()


########## Functions outside the class definitions


playerNames = []
playerObjects = []
def loadCharacter(character):
    inFile = open(character + ".sav", "rb")
    outObj = pickle.load(inFile)
    inFile.close()
    playerNames.append(character)
    playerObjects.append(outObj)
    return(outObj)


##########Script

#
# #Bruenor = Player("Bruenor","Dwarf", "Fighter", 15, 14, 13, 12, 10, 8, 0)
# Bruenor = loadCharacter("Bruenor")
# Bruenor.addItem('Weapon','Longsword',15,3,'1d8','Versatile','Slashing')
# Bruenor.viewInventory()
# #Bruenor.draw('Longsword')
#print Bruenor.equippedWeapon
