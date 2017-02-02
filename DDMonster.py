from random import *
from DDFunctions import damageRoll

class Monster:
    def __init__(self,Name,Monster):
        #stats from initialization
        self.name = Name
        self.Monster = Monster

        #find entry in Aris Monster Sorter matching Monster
        statList = []
        monsterfile = open("Aris-5e-Monster-Sorter.xlsx-Sheet1.tsv","r")
        for line in monsterfile:
            lineList = line.split("\t")
            if lineList[0] == self.Monster:
                lineList[-1] = lineList[-1].replace("\r\n","")
                statList = lineList
                break
        monsterfile.close()
        
        self.CR = statList[1]
        self.type = statList[2]
        self.subtype = statList[3]
        self.size = statList[4]
        self.align = statList[5]
        self.legendary = statList[6]
        self.hasLair = statList[7]
        self.strength = statList[8]
        self.dexterity = statList[9]
        self.constitution = statList[10]
        self.intelligence =  statList[11]
        self.wisdom = statList[12]
        self.charisma = statList[13]
        self.AC = statList[14]
        self.health = statList[15]
        self.maxHealth = damageRoll(self.health)
        self.currentHealth = self.maxHealth
        
#Test script
Aboleth1 = Monster("Aboleth1","Aboleth")

