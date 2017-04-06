

class HardBot(object):
	"""docstring for HardBot"""
	def __init__(self, game, player):
		self.bot = player
		self.game = game

	def arrange(self):
		hand = self.bot.hand
		table = self.game.table
		worth = 0

		# arranges the table by descending worth of the cards
		for i in range(table):
			if (table[i-1].special < table[i].special):
				bestPick = table[i]
				table[i] = table[i-1]
				table[i-1] = bestPick

		# prioritizes spades over other suits
		for i in range(table):
			if (table[i-1].special == table[i].special and table[i].isSpades):
				spades = table[i]
				table[i] = table[i-1]
				table[i-1] = spades
