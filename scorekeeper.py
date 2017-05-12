import time

class ScoreKeeper(object):
	"""docstring for ScoreKeeper"""
	def __init__(self, players):
		self.players = players
		self.countCards()



	#Check who has the most cards and give them a point
	def countCards(self):
		leaders = [self.players[0]]
		leader = leaders[0]
		for player in self.players:
			if len(player.stack) > len(leader.stack):
				leaders = [player]
			elif len(player.stack) == len(leader.stack):
				leaders.append(player)

		for player in leaders:
			player.score += 1

		self.countSpades()


	#Check who has most spades and give them 2 points
	def countSpades(self):
		leaders = [self.players[0]]
		leading = 0
		for player in self.players:
			spades = 0
			for card in player.stack:
				if card.suit == 'S':
					spades += 1
			if spades > leading:
				leaders = [player]
			elif spades == leading:
				leaders.append(player)

		for player in leaders:
			player.score += 2


		self.countPoints()


	def countPoints(self):
		for player in self.players:
			for card in player.stack:
				player.score += card.points
			print(player.getName() + " has ", player.score , " points.")
			time.sleep(0.3) 

		self.winner()


	def winner(self):
		winners = []
		for player in self.players:
			if player.score >= 16:
				winners.append(player)

		if len(winners) > 1:
			for player in winners:
				if player.score < winners[0].score:
					winners.remove(player)
		if len(winners) > 0:
			if len(winners) > 1:
				print()
				print("The game ended in a tie between ", end = '')
				for i in range(len(winners)-1):
					print(winners[i].getName() + " and ", end = '')

				print(winners[len(winners)].getName() + ".")
				quit()

			else: 
				print()
				print("The winner is " + winners[0].getName() + "!")
				time.sleep(0.5)
				if(winners[0].bot):
					print()
					print("Better luck next time :)")
					print()
				else:
					print()
					print("yeah baby YEAH!")
					print()
				quit()




		