from setofcards import *
from card import *
from player import *

class Game(object):
	"""docstring for Game"""
	def __init__(self):
		
		self.players = []
		self.SetOfCards = SetOfCards(self)
		self.deck = Deck(self)
		self.table = Table()


	def initDeck(self)

		#create cards
        suits = ['S', 'D', 'C', 'H']
        values = [str(x) for x in range(1, 14)]
        cards = [Card(x, y) for x in values for y in suits]
        random.shuffle(cards) # shuffle cards
        
        #add cards to deck
        for card in cards: 
            self.deck.addCard(card)


	def addPlayer(self, name):

		newPlayer = Player(name, len(self.players))
		self.players.append(newPlayer)
		return newPlayer


	def newRound(self):
		pass

