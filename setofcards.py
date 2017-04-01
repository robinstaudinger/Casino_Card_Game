class SetOfCards(object):
	"""docstring for SetOfCards"""
	def __init__(self, game):
		#super(SetOfCards, self).__init__()
		self.game = game
		self.cards = []
		
	def addCard(self, card):
		self.cards.append(card)

	def empty(self):
		self.cards = []

		

class Table(SetOfCards):
	"""docstring for Table"""
	def __init__(self, game):
		super(SetOfCards, self).__init__()
		self.game = game

		#Player collects a card from the table
	def moveToStack(self, card, player):
		self.cards.remove(card)
		player.cards.append(card)



class Deck(SetOfCards):
	"""docstring for Deck"""
	def __init__(self, game):
		super(SetOfCards, self).__init__()
		self.game = game

		#Deal a card to a player
	def dealToHand(self, card, player):
		self.cards.remove(card)
		player.hand.append(card)

		#Deal a card to the table
	def dealToTable(self, card):
		self.cards.remove(card)
		self.game.table.cards.append(card)

		#Shuffle the deck
	def shuffle(self):
		self.cards.random()

		