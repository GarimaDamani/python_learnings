/**
    Code randomly generates a number between 1 to 100. User is asked to guess the number.
    User is given 3 chances to guess the number, When user enters a integer then code checks if its close to number guessed if so then displays "Your guess is close" else "Your guess is far".
    Code decides the close or far, If difference in guessed number and user's guessed number is 10 or more then 10.
**/

import random

print ("\n***Welcome to Guess My Number Python Program***")

userName = input ("Please Enter Your Name: ")

print ("Hi!", userName)
print ("\nMy name is XYZ.")
print ("\nSo, Let's start. I have thought of a number in range of 1 to 100")
print ("You have 3 chances to guess the number.\n")

def generateNumber():
	return random.randint(1, 100)

randomNumber = generateNumber()

for i in range(3):
	print ("Chance", i,":")
	try:
		userNumber = int(input())
		difference = abs (randomNumber - userNumber)
		if randomNumber == userNumber:
			print ("Wow!!",userName,", You guessed it right")
			break
		elif  difference > 10:
			print ("Your guess is Far")
		elif  difference < 10:
			print ("Your guess is Close")
		elif  difference > 20:
			print ("Your guess is Too Far")
		
	except ValueError:
		print("That's not an number!")
	if i == 2:
		print ("\nI had guessed number: ", randomNumber)
		print ("Thank you for playing",userName,". Have a nice day!")
