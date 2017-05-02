class Card(object):
	"""creates a card object that has a value (1-13), a suit(Hearts, Diamonds, Clubs and Spades)"""
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
		self.handValue = self.value
		self.points = 0
		if (self.value == 1):
			self.handValue = 14
			self.points = 1
		if (self.value == 2 and self.suit == 'S'):
			self.handValue = 15
			self.points = 1
		if (self.value == 10 and self.suit == 'D'):
			self.handValue = 16
			self.points = 2
		

	def isSpades(self):
		if(self.suit == 'S'):
			return True
		return False


	def getCard(self):
		return str(self.value) + self.suit	#returns the card as a string
