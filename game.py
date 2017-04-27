from setofcards import *
from card import *
from player import *
from hardbot import *

class Game(object):
	"""docstring for Game"""
	def __init__(self):

		self.players = []
		self.SetOfCards = SetOfCards(self)
		self.deck = Deck(self)
		self.table = Table(self)
		self.round = 1

		self.mainMenu()
		self.addPlayer()
		self.addBots()
		self.newRound()

		for i in range(4):
			self.deck.dealToTable(self.table)


	def mainMenu(self):

		print()
		print("================================")
		print("Welcome to the Casino Card Game!")
		print("================================")
		print()
		print("The cards in your hand are indexed 1,2,3,4... if you cannot use a card \n" +
				"please type 0 and you will be able to put down a card on the table")
		print()


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
			newBot.bot = True
		


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
		self.initDeck()

		if self.round == 1:
			for i in range(4):
				self.deck.dealToTable(self.table)

		#deal the cards
		self.players.append(self.players.pop(0)) # rearrange the players array so that the dealer will be dealt last
		for i in range(4):
			for player in self.players:
				self.deck.dealToHand(player)

		#start the game
		self.gamePlay()



	def gamePlay(self):
		turn = self.players		#make a new list that takes care of the turns
		player = turn[0]
		#play until all cards are used
		while len(player.hand) > 0:
			self.table.displayCards()
			#bot's turn
			if player.bot:
				print()
				print(player.name + "'s turn")
				player.displayCards()
				HardBot(self, player)


			#player's turn
			else:
				print()
				print(player.name + "'s turn")
				player.displayCards()
				self.playerTurn(player)

			#take a card and pass the turn to the next player
			if len(self.deck.cards)>1:
				self.deck.dealToHand(player)
			turn.append(turn.pop(0))
			player = turn[0]

		#start a new round when no cards are left
		self.round += 1
		self.newRound()

	def playerTurn(self,player):

		hand = int(self.handIndex(player))
		self.collect(player, hand)



	def handIndex(self,player):
		try:
			index = int(input("Type the index of the card you want to use: ").strip()) - 1 #convert user friendly index to real
			while index not in range(-1,len(player.hand)):
				print("Index is unavailable, please try again.")
				index = int(input("Type the index of the card you want to use: ").strip()) - 1
			return index
		except:
			print("Index must be type of integer, try again.")
			return self.handIndex(player)
			

	def collect(self, player, handIndex):

		if handIndex != -1:
			capture = []
			cardToUse = player.hand[handIndex]
			try:
				tableIndexes = input("Type the index(es) of the card(s) you want to collect: ").split(",")			
				
				for i in range(len(tableIndexes)):
					pick = tableIndexes[i].split("+")
					collect = 0
					for j in range(len(pick)):
						tableIndex = int(pick[j].strip()) - 1 #convert to real index
						collect += self.table.cards[tableIndex].value

					#invalid choice
					if cardToUse.handValue != collect:
						print("Invalid pick, try again.")
						return self.playerTurn(player)
					else:
						capture += pick

				#move the captured cards to the stack
				if len(capture)>1:
					capture = sorted(capture)
				for j in range(len(capture)):
						tableIndex = int(capture[j].strip()) - (1 + j)
						player.stack.append(self.table.cards.pop(tableIndex))
				player.stack.append(player.hand.pop(handIndex))

			except:
				print("Invalid input, try again!")
				self.playerTurn(player)

			

		#If the player cannot collect cards they will need to lay one on the table 
		else:
			print("Please lay down a card on the table.")
			handIndex = self.handIndex(player)
			while handIndex < 0 or handIndex > 3:
				print("Index is unavailable, please try again.")
				handIndex = self.handIndex(player)
			self.table.cards.append(player.hand.pop(handIndex))
			




