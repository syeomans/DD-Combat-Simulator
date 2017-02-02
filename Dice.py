#Import libraries and begin while loop
from random import *

#Loop until user enters a blank input string
running = True
while running:
	#Get text input from user. If blank, stop while loop
	print("\n")
	inStr = "0+" #String evaluation begins at 0
	inStr += str (raw_input  ("Enter a die roll (ex: d20adv+2d4-1): "))
	#If user entered a blank string, break and end script.
	if inStr == "0+":
		running = False
		break

	#Format die roll. Put a delimiting space between every die or bonus and separate into a list.
	inStr = inStr.replace ("+"," +")
	inStr = inStr.replace ("-"," -")
	inStr = inStr.replace ("+d","+1d")
	inStr = inStr.replace ("-d","-1d")
	inStr = inStr.replace ("adv","x") #mark advantage rolls with an x (for ease of use)
	inStr = inStr.replace ("dis","y") #mark disadvantage rolls with a y (for ease of use)
	#Convert input string to a list of dice and bonuses
	inList = inStr.split (" ")
	#example looks like ['0', '+1d20x', '+2d4', '-1']

	#Roll each die and add to roll string. Bonus is tallied separately to make output easier to read.
	bonus = 0
	rollStr = ""
	prntStr = ""
	for die in inList:
		#Detect if list element is a die. Else, it's a bonus.
		if "d" in die:
			#If die is marked with advantage 
			if "x" in die:
				#Preserve the sign (positive or negative) and move to its own variable
				sign = die[0]
				die = die[1:]
				#Remove advantage mark
				die = die.replace("x","")
				#Number before "d" is the number of dice to roll; number after is the value of the die.
				#Roll a [after "d"] die [before "d"] times.
				roll = die.split("d")
				for i in range(0,int(roll[0])):
					#Roll this die twice and take the lower value. Add result to roll string.
					compare = [0,0]
					compare[0] = int(randrange(1,1+int(roll[1])))
					compare[1] = int(randrange(1,1+int(roll[1])))
					rollStr += sign + str(max(compare))
					prntStr += sign + str(compare)
			#If die is marked with disadvantage
			elif "y" in die:
				#Preserve the sign (positive or negative) and move to its own variable
				sign = die[0]
				die = die[1:]
				#Remove disadvantage mark
				die = die.replace("y","")
				#Number before "d" is the number of dice to roll; number after is the value of the die.
				#Roll a [after "d"] die [before "d"] times.
				roll = die.split("d")
				for i in range(0,int(roll[0])):
					#Roll this die twice and take the lower value. Add result to roll string.
					compare = [0,0]
					compare[0] = int(randrange(1,1+int(roll[1])))
					compare[1] = int(randrange(1,1+int(roll[1])))
					rollStr += sign + str(min(compare))
					prntStr += sign + str(compare)
			#Die is marked with neither advantage nor disadvantage
			else:
				#Preserve the sign (positive or negative) and move to its own variable
				sign = die[0]
				die = die[1:]
				#Number before "d" is the number of dice to roll; number after is the value of the die.
				#Roll a [after "d"] die [before "d"] times.
				roll = die.split("d")
				for i in range(0,int(roll[0])):
					val = sign + str(randrange(1,1+int(roll[1])))
					rollStr += val
					prntStr += val
		#This element of inList is not a die; therefore it is a bonus. Tally separately for ease of reading.
		else:
			bonus += int(die)

	#If bonus is positive, add a "+" and add to roll string.
	#If bonus is negative, it already has a "-"; just add to roll string.
	#If bonus is 0, don't bother adding it to the roll string.
	if bonus > 0:
		rollStr += "+" + str(bonus)
		prntStr += "+" + str(bonus)
	elif bonus < 0:
		rollStr += str(bonus)
		prntStr += str(bonus)

	#Evaluate roll string and print result
	#prntStr is the same as rollStr, but prntStr shows both rolls on advantage/disadvantage
	print(prntStr[1:]) #string always starts with unnecessary "+".
	print "Total: " + str(eval(rollStr))

	#Loop again