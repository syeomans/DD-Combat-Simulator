from DDFunctions import damageRoll

class Monster:
    def __init__(self,name,creatureType):
        #stats from initialization
        self.name = name
        self.creatureType = creatureType

        # Find the corresponding entry in the monster tsv file
        # Columns of .tsv file:
        # Name, Size, Type, Subtype, Alignments, CR, HP, AC, STR, DEX, CON, INT
        # WIS, CHA, Speeds, Sav. Throws, Weaknesses, Resistances, Immunities,
        # Senses, Skills, Languages, Feats, Book, Page, Spellcasting?,
        # Attack 1 name, Attack 1 damage, Attack 1 damage type, Attack 2 name,
        # Attack 2 damage, Attack 2 damage type, Terrain
        statList = []
        monsterfile = open("monsters.tsv","r")
        for line in monsterfile:
            lineList = line.split("\t")
            if lineList[0] == self.creatureType:
                lineList[-1] = lineList[-1].replace("\n","")
                statList = lineList
                break
        monsterfile.close()

        self.size = statList[1]
        self.type = statList[2]
        self.subtype = statList[3]
        self.alignments = statList[4]
        self.alignment = None
        self.cr = statList[5]
        self.hp = statList[6]
        self.ac = statList[7]
        self.str = statList[8]
        self.dex = statList[9]
        self.con = statList[10]
        self.int = statList[11]
        self.wis = statList[12]
        self.cha = statList[13]
        self.savingThrows = [] if statList[15] == 'None' else statList[15].lower().split(', ')
        self.weaknesses = [] if statList[16] == '' else statList[16].lower().split(', ')
        self.resistances = [] if statList[17] == '' else statList[17].lower().split(', ')
        self.immunities = [] if statList[18] == '' else statList[18].lower().split(', ')
        self.skills = [] if statList[20] == 'None' else statList[20].lower().split(', ')
        self.languages = [] if statList[21] == 'None' else statList[21].lower().split(', ')
        self.feats = [] if statList[22] == 'None' else statList[22].lower().split(', ')
        self.spellcaster = True if statList[25] == 'YES' else False
        self.terrain = statList[32]

        self.speeds = {}
        speedsTemp = statList[14].split(", ")
        for i in range(0,len(speedsTemp)):
            speedsTemp[i] = speedsTemp[i].split(" ")
            self.speeds[speedsTemp[i][0]] = int(speedsTemp[i][1])

        self.senses = {}
        sensesTemp = statList[19].lower().split(", ")
        if sensesTemp != 'normal':
            for i in range(0,len(sensesTemp)):
                sensesTemp[i] = sensesTemp[i].split(" ")
                self.senses[sensesTemp[i][0]] = int(sensesTemp[i][1])

        self.attacks = []
        self.attacks.append({'name': statList[26], 'damage': statList[27], 'type': statList[28]})
        self.attacks.append({'name': statList[29], 'damage': statList[30], 'type': statList[31]})
        print(self.attacks)

#Test script
Aboleth1 = Monster("Aboleth1","Aboleth")
