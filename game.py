from setofcards import *
from card import *
from player import *

class Game(object):
	"""docstring for Game"""
	def __init__(self):

		self.players = []
		self.SetOfCards = SetOfCards(self)
		self.deck = Deck(self)
		self.table = Table(self)


	def addPlayer(self, name):
		if len(self.players) == 12:
			raise ValueError("Max 12 players allowed")
		newPlayer = Player(name, len(self.players))
		self.players.append(newPlayer)
		


	def addBot(self, name):
		if len(self.players) == 12:
			raise ValueError("Max 12 players allowed")
		newBot = Player(name, len(self.players))
		self.players.append(newBot)
		newBot.isBot = True
		


	def initDeck(self):
		# create cards
	    suits = ['H', 'D', 'C', 'S']
	    values = [str(x) for x in range(1, 14)]
	    cards = [Card(x, y) for x in values for y in suits]

	    # add the cards to the deck and shuffle
	    for card in cards: 
	        self.deck.addCard(card)
	    self.deck.shuffleCards()


	def newRound(self):

		#deal the cards
		self.players.append(self.players.pop(0)) # rearrange the players array so that the dealer will be dealt last
		for i in range(4):
			for player in self.players:
				self.deck.dealToHand(player)
			self.deck.dealToTable(self.table)
		self.gamePlay()

	def gamePlay(self):
		while len(self.deck.cards) > 0:
			turn = self.players		#make a new list that takes care of the turns
			player = turn[0]

			self.table.displayCards()
			if player.bot:
				pass  #to be implemented later
			else:
				print()
				print(player.name + "'s turn")
				player.displayCards()

				handIndex = int(input("Type the index of the card you want to use: ").strip()) - 1 #convert user friendly index to real
				
				if handIndex >= 0 and handIndex < 4:
					cardToUse = player.hand[handIndex]

					tableIndexes = input("Type the index(es) of the card(s) you want to collect: ")
					tableIndexes = tableIndexes.split(",")
					collect = 0
					for i in range(len(tableIndexes)):
						pick = tableIndexes[i].split("+")
						for j in range(len(pick)):
							tableIndex = int(pick[j].strip()) - 1 #convert to real index
							collect += self.table.cards[tableIndex].value

						#valid choice, move cards to stack
						if cardToUse.handValue == collect:
							player.stack.append(player.hand.pop(handIndex))
							for i in range(len(tableIndexes)):
								pick = tableIndexes[i].split("+")
								for j in range(len(pick)):
									tableIndex = int(pick[j].strip()) - 1
									player.stack.append(self.table.cards.pop(tableIndex-j))

						else:
							raise IOError("Invalid choice of cards!")
					
				#If the player cannot collect cards they will need to lay one on the table 
				elif handIndex == -1:
					handIndex = int(input("Type the index of the card you want to place on the table: ").strip()) - 1
					self.table.cards.append(player.hand.pop(handIndex))

				else:
					raise IOError("Invalid choice of cards!")

			#take a card and pass the turn to the next player
			self.deck.dealToHand(player)
			turn.append(turn.pop(0))	




