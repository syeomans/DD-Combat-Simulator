from random import randrange
from math import floor

class creature:
    def __init__(self, hp, ac, attackBonus, damageBonus, damageDie, initiativeBonus, name):
        self.hp = hp
        self.ac = ac
        self.attackBonus = attackBonus
        self.damageBonus = damageBonus
        self.damageDie = damageDie
        self.initiative = randrange(1,21) + initiativeBonus
        self.name = name

    def attack(self, target):
        attackRoll = randrange(1,21) + self.attackBonus
        if attackRoll >= target.ac:
            damage = randrange(1,self.damageDie+1) + self.damageBonus
        else:
            damage = 0
        return(damage)

    def damage(self, hpLoss):
        self.hp = self.hp - hpLoss

vadaVictories = 0
goblinVictories = 0
for a in range(1000):
    numGoblins = 3
    vada = creature(15, 14, 5, 3, 12, 1, "Vada")
    goblins = [creature(7, 13, 4, 2, 6, 2, "Goblin" + str(i)) for i in range(numGoblins)]
    combatants = []
    combatants.append(vada)
    combatants.extend(goblins)

    playing = True
    initiativeCount = 30
    goblinsRemaining = numGoblins
    while playing:
        for c in combatants:
            if c.initiative == initiativeCount and c.hp > 0:
                # This creature's turn
                if c.name == "Vada":
                    damageDealt = c.attack(combatants[goblinsRemaining])
                    combatants[goblinsRemaining].damage(damageDealt)
                    #print("Vada deals " + str(damageDealt) + " damage")
                else:
                    damageDealt = floor(c.attack(combatants[0])/2)
                    combatants[0].damage(damageDealt)
                    #print(c.name + " deals " + str(damageDealt) + " damage")

        # Check which creatuers are still alive
        if combatants[0].hp <= 0:
            playing = False
            #print("Goblins win")
            goblinVictories += 1
            break
        else:
            goblinsRemaining = 0
            for i in range(1,len(combatants)):
                if combatants[i].hp > 0:
                    goblinsRemaining += 1
            if goblinsRemaining == 0:
                playing = False
                #print("Vada wins")
                vadaVictories += 1
                break

        initiativeCount -= 1
        if initiativeCount <= -10:
            initiativeCount = 30

print("Goblin victories: " + str(goblinVictories))
print("Vada victories: " + str(vadaVictories))
