# import the random package so that we can generate a random choice
from random import randint
from gameFunctions import winlose, gamej, compare



while gamej.player is False:
	# set player to True
	print("**********************************")
	print("Computer lives: ", gamej.computer_lives, "/",gamej.total_lives,"\n")
	print("Player lives: ", gamej.player_lives, "/",gamej.total_lives,"\n")
	print("Choose your weapon!\n")
	print("**********************************")

	player = input("choose rock, paper or scissors: ")
	player = player.lower()

	print("computer chose ", gamej.computer, "\n")
	print("player chose ", player, "\n")

	#### this is where you would call compare
	
	compare.comparechoices(gamej.computer, player)

	### end compare stuff


	# handle all lives lost for player or AI
	if gamej.player_lives is 0:
		winlose.winorlose("lost")

	elif gamej.computer_lives is 0:
		winlose.winorlose("won")

	else:
		# need to check all of our conditions after checking for a tie
		gamej.player = False
		gamej.computer = gamej.choices[randint(0, 2)]	

