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


	def addPlayer(self):
		name = input("Enter your name:\n")
		newPlayer = Player(name, len(self.players))
		self.players.append(newPlayer)
		


	def addBots(self):
		try:
			botCount = int(input("How many opponents?\n").strip())
		except:
			print("Please enter your answer in numbers.")
			return self.addBots()
		if botCount > 11 or botCount < 1:
			print("There can be 1-11 opponents.")
			return self.addBots()
		# create player objects for the bots
		for i in range(botCount):
			name = ("Bot" + str(i+1))
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
			#bot's turn
			if player.bot:
				pass  #to be implemented later

			#player's turn
			else:
				print()
				print(player.name + "'s turn")
				player.displayCards()
				self.playerTurn(player)

			#take a card and pass the turn to the next player
			self.deck.dealToHand(player)
			turn.append(turn.pop(0))

	def playerTurn(self,player):

		hand = int(self.handIndex())
		self.collect(player, hand)



	def handIndex(self):
		try:
			index = int(input("Type the index of the card you want to use: ").strip()) - 1 #convert user friendly index to real
			while index not in range(-1,4):
				print("Index is unavailable, please try again.")
				index = int(input("Type the index of the card you want to use: ").strip()) - 1
			return index
		except:
			print("Index must be type of integer, try again.")
			return self.handIndex()
			

	def collect(self, player, handIndex):

		if handIndex != -1:
			cardToUse = player.hand[handIndex]

			tableIndexes = input("Type the index(es) of the card(s) you want to collect: ").split(",")
			
			for i in range(len(tableIndexes)):
				pick = tableIndexes[i].split("+")
				collect = 0
				try:
					for j in range(len(pick)):
						tableIndex = int(pick[j].strip()) - 1 #convert to real index
						collect += self.table.cards[tableIndex].value
				except Exception as e:
					print("Invalid table indexes.")
					return self.collect(player, handIndex)

				#valid choice, move cards to stack
				if cardToUse.handValue == collect:
					player.stack.append(player.hand.pop(handIndex))
					for i in range(len(tableIndexes)):
						pick = tableIndexes[i].split("+")
						for j in range(len(pick)):
							tableIndex = int(pick[j].strip()) - 1
							player.stack.append(self.table.cards.pop(tableIndex-j))
				else:
					print("Invalid pick, try again.")
					self.playerTurn(player)

		#If the player cannot collect cards they will need to lay one on the table 
		else:
			print("Please lay down a card on the table.")
			handIndex = self.handIndex()
			self.table.cards.append(player.hand.pop(handIndex))
			




