colNames = ['Name', 'Size', 'Type', 'Subtype', 'Alignments', 'CR', 'HP', 'AC', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'Speeds', 'Sav. Throws', 'Weaknesses', 'Resistances', 'Immunities', 'Senses', 'Skills', 'Languages', 'Feats', 'Book', 'Page', 'Spellcasting?', 'Attack 1 name', 'Attack 1 damage', 'Attack 1 damage type', 'Attack 2 name', 'Attack 2 damage', 'Attack 2 damage type', 'Terrain']
colIndex = range(0,len(colNames))
for i in colIndex:
    print('self.' + str(colNames[i].lower()) + ' = statList[' + str(i) + ']')
