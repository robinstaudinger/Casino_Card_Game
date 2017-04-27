from card import Card

class Player(object):
	"""creates a player object that has a name, type (computer or human) and a score"""

	def __init__(self, name, seat):
		
		self.name = name
		self.score = 0
		self.hand = []
		self.stack = []
		self.bot = False
		self.seat = seat

	def getName(self):
		return self.name

	def addCardToHand(self, card):
		self.hand.append(card)
		
	def getScore(self):
		return self.score

	def displayCards(self):
		print()
		print("	 	YOUR CARDS 		")
		print("		========== 		")
		print()

		print("Cards: \t", end = '')
		for card in self.hand:
			print('\t' + card.getCard() , end = '')	#print cards without newline
		print("\n")			#add newline to the end

		print("Indexes: ", end = '')
		for i in range(len(self.hand)):
			print('\t', i+1, end = '') #print indexes
		print("\n")

	def isBot(self):
		return self.bot

