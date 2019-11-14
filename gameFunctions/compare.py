# what are you trying to compare inside this functions?
# you will need to pass those things in as arguments
# insde the round brackets 
from gameFunctions import winlose, gamej 
def comparechoices(comp, play):
	if play == "quit":
		exit()
	elif gamej.computer == play:
		print("tie! no one wins, play again")

	elif play == "rock":
		if gamej.computer == "paper":
			print("You lose!", gamej.computer, "covers", play, "\n")
			gamej.player_lives = gamej.player_lives - 1
		else:
			print("You win!", play, "smashes", gamej.computer, "\n")
			gamej.computer_lives = gamej.computer_lives - 1

	elif play == "paper":
		if gamej.computer == "scissors":
			print("You lose!", gamej.computer, "cuts", play, "\n")
			gamej.player_lives = gamej.player_lives - 1
		else:
			print("You win!", play, "covers", gamej.computer, "\n")
			gamej.computer_lives = gamej.computer_lives - 1

	elif play == "scissors":
		if gamej.computer == "rock":
			print("You lose!", gamej.computer, "smashes", play, "\n")
			gamej.player_lives = gamej.player_lives - 1
		else:
			print("You win!", player, "cuts", gamej.computer, "\n")
			gamej.computer_lives = gamej.computer_lives - 1

	else:
		print("That's not a valid choice, try again")