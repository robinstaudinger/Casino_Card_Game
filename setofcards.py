import random

class SetOfCards(object):
	"""docstring for SetOfCards"""
	def __init__(self, game):
		
		self.game = game
		
	def addCard(self, card):
		self.cards.append(card)

	def empty(self):
		self.cards = []

	

class Table(SetOfCards):
	"""docstring for Table"""
	def __init__(self, game):
		super(SetOfCards, self).__init__()
		self.game = game
		self.cards = []

		#Player collects a card from the table
	def moveToStack(self, card, player):
		self.cards.remove(card)
		player.cards.append(card)

	def displayCards(self):
		print()
		print("		*   CARDS ON THE TABLE   *	")
		print("		    ================== 		")
		print()
		
		print("Cards: \t", end = '')
		for card in self.cards:
			print('\t' + card.getCard() , end = '')	#print cards without newline
		print("\n")			#add newline to the end

		print("Indexes: ", end = '')
		for i in range(len(self.cards)):
			print('\t', i+1, end = '') #print indexes
		print("\n")



class Deck(SetOfCards):
	"""docstring for Deck"""
	def __init__(self, game):
		super(SetOfCards, self).__init__()
		self.game = game
		self.cards = []

		#Deal a card to a player
	def dealToHand(self, player):
		card = self.cards.pop(0)
		player.addCardToHand(card)

		#Deal a card to the table
	def dealToTable(self, table):
		card = self.cards.pop(0)
		table.addCard(card)

		#Shuffle the deck
	def shuffleCards(self):
		random.shuffle(self.cards)
