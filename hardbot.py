from game import*
from player import*

class HardBot(object):
	"""docstring for HardBot"""
	def __init__(self, game, player):
		self.bot = player
		self.game = game
		self.table = self.game.table
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
		hand = self.arrange(self.hand)
		table = self.arrange(self.table.cards)

		for i in range(len(hand)-1):
			picker = hand[i].handValue
			print("picker: ", picker)
			for j in range(len(table)-1):
				k = j
				chosen = 0
				catch = [hand[i]]		#first card in the catch is the card the bot uses
				for k in range(len(table)-1):
					if(chosen + table[k].value < picker):
						chosen += table[k].value
						print(chosen)
						catch.append(table[k])
					if(picker == chosen):
						return self.stack(catch)
		return self.stack([hand[len(hand)-1]])		#if no card can be picked up, returns the card with lowest value

	#stack the chosen cards, or lay one on the table
	def stack(self, cards):

		if(len(cards)>1):
			self.bot.stack.append(cards.pop(0))
			for i in range(len(cards)):
				self.bot.stack.append(cards.pop(0))

		else:
			self.table.cards.append(cards.pop(0))

