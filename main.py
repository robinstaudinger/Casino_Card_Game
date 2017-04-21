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


	game.addPlayer()
	game.addBots()

	game.initDeck()
	game.newRound()
	game.table.displayCards()



if __name__ == '__main__':
	main()
