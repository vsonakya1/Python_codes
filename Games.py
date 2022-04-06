from binascii import b2a_base64
from os import kill
import random

#-----------------------------------Rock paper scissors----------------------------------------------------------------------------
def rock_paper_sicssors():
	rock = '''
		_______
	---'____)
		(_____)
		(_____)
		(____)
	---.__(___)
	'''

	paper = '''
		_______
	---'   ____)______
				______)
				_______)
			_________)
	---.__________)
	'''

	scissors = '''
		_____
	---' ____)____
		__________)
		__________)
			(____)
	---.__(___)
	'''

	play_again = ""
	while play_again == "" or play_again == "y":
		a = input("Please choose r,p,s: \n")
		if a == "r":
				print(rock)
		elif a == "p":
				print(paper)
		elif a == "s":
				print(scissors)
		else:
				print("Invalid entry")

		b = [rock, paper, scissors]
		c = random.randint(0, 2)
		d = (b[c])
		print(d)

		if (a == "r" and d == rock) or (a == "s" and d == scissors) or (a == "p" and d == paper):
				print("draw")
		elif (a == "r" and d == scissors) or (a == "s" and d == paper) or (a == "p" and d == rock):
				print("you win")
		else:
				print("Losser ")
		play_again = input("You want to play again: type y/n \n")


	print("🎉")

#----------------------------------------Black Jack-----------------------------------------------------------------------
def face_card(card):
	if card == 1:
		return("A")
	elif card ==11:
		return("J")	
	elif card ==12:
		return("Q")
	elif card ==13:
		return("K")
	else:
		return(card)


def blackjack():

	you_choose =input("you want a card y/n:\n")
	your_card = 0
	dealer_card =0

	#while you_choose =="y" or your_card < 16 or dealer_card < 16:
	while your_card < 16 or dealer_card < 16 or you_choose == "y":

		dealer= int(random.choice(range(1,14)))
		print(f"dealers card {face_card(dealer)}")
		dealer_card +=dealer

		your=int(random.choice(range(1,14)))
		print(f"Your card is {face_card(your)}")
		your_card +=your
		
		print (f"Total sum of Dealer cards {dealer_card}")
		print (f"Total sum of Your cards {your_card}")
		

		if your_card > 23:
			print("BUSTED")
			return
		elif dealer_card >23 and your_card < 23:
			print("you win")
			return


		if you_choose =="n" and dealer_card < 23:
			dealer= int(random.choice(range(1,14)))
			print(f"dealers card {face_card(dealer)}")
			dealer_card +=dealer
			
			print (f"Total sum of Dealer cards {dealer_card}")
			print (f"Total sum of Your cards {your_card}")

			if you_choose =="n" or dealer_card >23 or your_card > 23:
				if your_card > 23:
					print("BUSTED")
				elif dealer_card >23 and your_card < 23:
					print("you win")
				elif dealer_card <23 and your_card < dealer_card:
					print("you lost")
				elif dealer_card <23 and your_card > dealer_card and your_card < 23:
					print("You win")
			return ("game ended")
		you_choose =input("you want a card y/n:\n")	
		


#------------------------------Number gussing---------------------------------------------------------------------------------
from random import randint
from art import Guess_a_number

Level_easy = 10
Level_hard = 5

def set_level ():
	level = input("Please enter the level of diffculty E for easy and H for Hard: \n")
	if level.lower() == "e":
		return (Level_easy)
	elif level.lower() == "h":
		return (Level_hard)
	else:
		print("Invalid entry: Please enter correct input")
		game()



def check_answer (guess, answer,turns):
	if guess < answer:
		print ("Too low")
		return turns-1
	elif guess > answer:
		print("Too high")
		return turns-1
	else:
		print(f"You got the answer {answer} YAHOOOOOOO!!!!")	

def game():
	print (Guess_a_number)
	answer = randint(1,100)
	#print(str(answer))
	turns = set_level ()
	guess =0

	while guess != answer:
		print(f"You have {turns} turns to play ")
		guess = int(input ("Make a guess:\n"))
		turns = check_answer (guess, answer,turns)
		if turns ==0:
			print("you lost")
		elif guess != answer:
			print("Guess another number: \n")
	
	play_again = input("You want to play again Y/N:\n")
	
	if play_again=="Y":
		game()			
	else:
		print("GOOD BYE")
		exit()








































#---------------------------------------------------------------------------------------------------------------





#---------------------------------------------------------------------------------------------------------------





#---------------------------------------------------------------------------------------------------------------





#---------------------------------------------------------------------------------------------------------------