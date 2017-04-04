from game import *
from card import *
from player import *
from setofcards import *



def main():
	game = Game()
	print("Welcome to the Casino Card Game!")
	playerCount = int(input("How many players?"))

	# create player objects for the players
	for i in range(playerCount):
		name = input("Enter the name of Player " + i)
		game.addPlayer(name)

		# Check that the players were added
	for player in game.players:
		print(player.getName)

	botCount = input("How many opponents?")

		# create player objects for the bots
	for i in range(botCount):
		name = "Bot" + i
		game.addBot(name)

	game.initDeck()



if __name__ == '__main__':
	main()
