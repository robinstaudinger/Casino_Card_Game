class Card(object):
	"""creates a card object that has a value (1-13), a suit(Hearts, Diamonds, Clubs and Spades)"""
	def __init__(self, value, suit):
		##super(Card, self).__init__()
		self.value = value
		self.suit = suit
		self.handValue = value

	#we define the value for the special cards
	def setHandValue(self, value, suit):
		if (value == 1):
			self.handValue = 14
		if (value == 2 and suit == 'S'):
			self.handValue = 15
		if (value == 10 and suit == 'D'):
			self.handValue = 16

	


	
