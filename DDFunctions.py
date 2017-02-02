from random import *
from DDprofsDict import profsDict
import pickle

def findLevel (xp):
    levelChart = [0,300,900,2700,6500,14000,23000,34000,48000,64000,85000,100000,
                              120000,140000,165000,195000,225000,225000,265000,305000,355000]
    for i in range(0,21):
        if xp >= 355000:
            return(20)
        elif xp< levelChart[i]:
            return(i)

def findXP(lv):
    return(levelChart[lv - 1])
    def proficiency(self):
        return((self.Lv-1)/4+2)

classList = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger',
                         'Rogue','Sorcerer','Warlock','Wizard']
hitDieList = [12,8,8,8,10,8,10,10,8,6,8,6]
def findHitDie(cls):
    i = classList.index(cls)
    return(hitDieList[i])

def calProf(level):
    return((level-1)/4 + 2)

def damageRoll(ddice):
    '''ex: 2d8+2'''
    num, val = ddice.split('d')
    add = 0
    if '+' in val:
        val, add = val.split('+')
    elif '-' in val:
        val, add = val.split('-')
        add = -int(add)
    roll = 0
    for i in range(0,int(num)):
        roll += randrange(1,int(val)+1)
    return roll+int(add)


