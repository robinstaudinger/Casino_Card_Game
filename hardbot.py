from game import*
from player import*

class HardBot(object):
	"""docstring for HardBot"""
	def __init__(self, game, player):
		self.bot = player
		self.game = game
		self.table = self.game.table.cards
		self.hand = self.bot.hand
		self.collect()

	def arrange(self, cards):

		# arranges the cards by descending worth of the cards
		for i in range(len(cards)-1):
			if (cards[i].points < cards[i+1].points):
				bestPick = cards[i+1]
				cards[i+1] = cards[i]
				cards[i] = bestPick

		# prioritizes spades over other suits 
		for i in range(len(cards)-1):
			if ((cards[i].points == cards[i+1].points) and cards[i+1].isSpades()):
				spades = cards[i+1]
				cards[i+1] = cards[i]
				cards[i] = spades

		return cards

	#collects the best available combination
	def collect(self):
		self.hand = self.arrange(self.hand)
		self.table = self.arrange(self.table)

		for i in range(len(self.hand)):
			picker = self.hand[i].handValue
			for j in range(len(self.table)):
				chosen = 0
				catch = [self.hand[i]]		#first card in the catch is the card the bot uses
				for k in range(j,len(self.table)):
					if(chosen + self.table[k].value <= picker):
						chosen += self.table[k].value
						catch.append(self.table[k])
					if(picker == chosen):
						return self.stack(catch)

		return self.stack([self.hand[len(self.hand)-1]])		#if no card can be picked up, returns the card with lowest value


	#stack the chosen cards, or lay one on the table
	def stack(self, cards):

		if(len(cards)>1):
			self.bot.picked = True
			print(self.bot.getName() + " picked", end = '')
			for ccard in cards:
				for hcard in self.hand:
					if ccard == hcard:
						self.bot.stack.append(self.hand.pop(self.hand.index(hcard)))
			for ccard in cards:
				for tcard in self.table:
					if ccard == tcard:
						print(" " + tcard.getCard(), end = '')
						self.bot.stack.append(self.table.pop(self.table.index(tcard)))
			print(".")

		else:
			self.bot.picked = False
			print(self.bot.getName() + " laid down ", end = '')
			for card in self.hand:
				if(cards[0] == card):
					print(card.getCard() + ".")
					self.table.append(self.hand.pop(self.hand.index(card)))

