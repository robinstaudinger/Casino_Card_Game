from game import *
from card import *
from player import *
from setofcards import *



def main():
	game = Game()

	print()
	print("================================")
	print("Welcome to the Casino Card Game!")
	print("================================")
	print()
	print("The cards in your hand are indexed 1,2,3,4... if you cannot use a card \n" +
			"please type 0 and you will be able to put down a card on the table")
	print()

	playerCount = int(input("How many players?\n"))

	# create player objects for the players
	for i in range(playerCount):
		name = input("Enter the name of Player " + str(i+1) + "\n")
		game.addPlayer(name)

	botCount = int(input("How many opponents?\n"))

		# create player objects for the bots
	for i in range(botCount):
		name = ("Bot" + str(i+1))
		game.addBot(name)

	game.initDeck()
	game.newRound()
	game.table.displayCards()



if __name__ == '__main__':
	main()
