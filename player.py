from card import Card

class Player(object):
	"""creates a player object that has a name, type (computer or human) and a score"""

	def __init__(self, name, seat):
		#super(Player, self).__init__()
		self.name = name
		self.score = 0
		self.hand = []
		self.stack = []
		self.npc = False
		self.seat = seat



	def addCardToHand(self, card):
		self.hand.append(card)
		
	def getPoints(self):
		pass

	def getHand(self):
		return self.hand

	def isNpc(self):
		return self.npc

