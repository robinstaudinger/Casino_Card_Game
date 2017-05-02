from setofcards import *
from card import *
from player import *
from hardbot import *
from scorekeeper import *
from saveload import *
import random
import sys

class Game(object):
	"""docstring for Game"""
	def __init__(self):

		self.players = []
		self.deck = Deck(self)
		self.table = Table(self)
		self.round = 0
		self.lastPick = None

		self.mainMenu()
		self.addPlayer()
		self.addBots()
		self.newRound()


	def mainMenu(self):

		print()
		print("		================================")
		print("		Welcome to the Casino Card Game!")
		print("		================================")
		print()
		print("The cards in your hand are indexed 1,2,3,4... if you cannot use a card \n" +
				"please type 0 and you will be able to put down a card on the table\n" +
				"To collect a sum add a '+' between indexes, to separate sums add ','.")
		print()
		print("You can save the game by typing 'SAVE', if you wish to exit the game, type 'QUIT'.")
		print()

		try:
			open("saved.txt", mode='r') #check for a saved file
			load = input("Do you wish to load your saved game? (Y/N)\n")
			print()
			if(load == "Y"):
				SaveLoad(self).load()
				quit()
		except:
			pass



	def addPlayer(self):
		name = input("Enter your name:\n")
		self.command(name) 	#check if command
		print()
		newPlayer = Player(name)
		self.players.append(newPlayer)
		


	def addBots(self):
		botCount = input("How many opponents?\n").strip()
		self.command(botCount) 	#check if command

		try:
			botCount = int(botCount)
		except:
			print("Please enter your answer in numbers.")
			return self.addBots()
		if botCount > 11 or botCount < 1:
			print("There can be 1-11 opponents.")
			return self.addBots()
		names = ["Börje", "Ivan", "Albert", "Kaesar", "Lisa", "Eivor", "Seppo", "Ismo", "Göran", "Gilbert", "Jere"]
		# create player objects for the bots
		for i in range(botCount):
			name = random.choice(names)
			names.remove(name)
			name = ("Bot " + name)
			newBot = Player(name)
			self.players.append(newBot)
			newBot.bot = True

		if self.round == 0:
			random.shuffle(self.players)	#give players random seats
	    		
	    		
	def newRound(self):
		self.round += 1
		dealer = self.players[0].getName()

		print()
		print("All set, " + dealer + " is the dealer.")
		print()

		self.initDeck()

	
		for i in range(4):
			self.deck.dealToTable(self.table)

		#deal the cards
		self.players.append(self.players.pop(0)) # rearrange the players array so that the dealer will be dealt last
		for i in range(4):
			for player in self.players:
				self.deck.dealToHand(player)

		#start the game
		self.gamePlay()


	def initDeck(self):
		# create cards
	    suits = ['H', 'D', 'C', 'S']
	    values = [x for x in range(1, 14)]
	    cards = [Card(x, y) for x in values for y in suits]

	    # add the cards to the deck and shuffle
	    for card in cards: 
	        self.deck.addCard(card)
	    self.deck.shuffleCards()



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
				#give bot a point if it empties table
				if len(self.table.cards) == 0:
					player.score += 1
				if player.picked:
					self.lastPick = player


			#player's turn
			else:
				print()
				print(player.name + "'s turn")
				player.displayCards()
				self.playerTurn(player)
				if player.picked:
					self.lastPick = player

			#take a card and pass the turn to the next player
			if len(self.deck.cards)>1:
				self.deck.dealToHand(player)
			turn.append(turn.pop(0))
			player = turn[0]

		#last player to collect gets the rest of the cards
		self.collectRest(self.lastPick)

		#count the score of the round for all the players
		print()
		print("Scores after round " , self.round)
		print()

		ScoreKeeper(self.players)

		#empty the stacks after the score is updated
		for player in self.players:
			player.stack = []

		#start a new round when no cards are left
		self.newRound()

	def playerTurn(self,player):

		hand = int(self.handIndex(player))
		self.collect(player, hand)
		#give a point if the player emptied the table
		if len(self.table.cards) == 0:
			player.score += 1



	def handIndex(self,player):
		index = input("Type the index of the card you want to use: ").strip()
		self.command(index)	#test if command
		try:
			index = int(index) - 1 #convert user friendly index to real
			while index not in range(-1,len(player.hand)):
				print("Index is unavailable, please try again.")
				index = input("Type the index of the card you want to use: ").strip()
				self.command(index)	#test if command
				index = int(index) - 1
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
				self.command(tableIndexes)	#test if command
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

				player.picked = True

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
			player.picked = False
			print("Please lay down a card on the table.")
			handIndex = self.handIndex(player)
			while handIndex < 0 or handIndex > 3:
				print("Index is unavailable, please try again.")
				handIndex = self.handIndex(player)
			self.table.cards.append(player.hand.pop(handIndex))

	#get the player that last collected from the table and give them the rest of the cards 
	def collectRest(self, lastPick):
		try:
			for i in range(len(self.table.cards)):
				lastPick.stack.append(self.table.cards.pop(0))
		except:
			self.table.empty()

	def command(self, string):
		command = string
		if command == 'SAVE':
			SaveLoad(self).save()
		if command == 'QUIT':
			quit()



			




