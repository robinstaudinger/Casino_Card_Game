
class SaveLoad(object):
	def __init__(self, game):
		self.game = game

	def save(self):
		try:
			with open("saved.txt", mode='w') as f:
				f.write("round: " + str(self.game.round) + "\n")

				f.write("deck: ")
				self.writer(f, self.game.deck.cards)

				f.write("table: ")
				self.writer(f, self.game.table.cards)

				for player in self.game.players:
					f.write("player: " + player.getName() + "\n")

					f.write("hand: ")
					self.writer(f, player.hand)

					f.write("stack: ")
					self.writer(f, player.stack)

					f.write("score: " + str(player.score) + "\n")

					f.write("picked: " + str(player.picked) + "\n")
		except OSError:
			print("paska ei toimi")
		if(f):
			f.close()
		quit()
				


	def writer(self, file, domain):
		for card in domain:
			file.write(str(card.value) + "-" + card.suit + " ")
		file.write("\n")