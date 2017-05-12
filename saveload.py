from game import *
from card import *
from player import *
from setofcards import *


class SaveLoad(object):
	def __init__(self, game):
		self.game = game

	def save(self):
		try:
			with open("saved.txt", mode='w') as f:
				f.write("round:\n" + str(self.game.round) + "\n")

				f.write("deck:\n")
				self.cardWriter(f, self.game.deck.cards)

				f.write("table:\n")
				self.cardWriter(f, self.game.table.cards)

				for player in self.game.players:
					f.write("player:\n" + player.getName() + "\n")

					f.write("hand:\n")
					self.cardWriter(f, player.hand)

					f.write("stack:\n")
					self.cardWriter(f, player.stack)

					f.write("score:\n" + str(player.score) + "\n")

					f.write("picked:\n" + str(player.picked) + "\n")
		except OSError:
			print("Error saving game.")
		if(f):
			f.close()
		quit()
				
	#writes cards into the file
	def cardWriter(self, file, domain):
		for card in domain:
			file.write(str(card.value) + "-" + card.suit + " ")
		file.write("\n")


	def load(self):
		try:
			with open("saved.txt", mode='r') as f:
				read = f.readline()
				while read != '':
					if(read == "round:\n"):
						self.game.round = int(f.readline())

					if(read == "deck:\n"):
						read = f.readline()
						cards = self.cardReader(read.split())
						for card in cards:
							self.game.deck.addCard(card)

					if(read == "table:\n"):
						read = f.readline().split()
						cards = self.cardReader(read)
						for card in cards:
							self.game.table.addCard(card)

					if(read == "player:\n"):
						read = f.readline().split()
						if(read[0] == "Bot"):
							name = str(read[0] + ' ' + read[1])
							newplayer = Player(name)
							newplayer.bot = True
							self.game.players.append(newplayer)

						else:
							name = read[0]
							newplayer = Player(name)
							self.game.players.append(newplayer)

					if(read == "hand:\n"):
						read = f.readline().split()
						cards = self.cardReader(read)
						for card in cards:
							self.game.players[len(self.game.players)-1].addCardToHand(card)

					if(read == "stack:\n"):
						read = f.readline().split()
						cards = self.cardReader(read)
						for card in cards:
							self.game.players[len(self.game.players)-1].stack.append(card)

					if(read == "score:\n"):
						score = int(f.readline())
						self.game.players[len(self.game.players)-1].score = score

					if(read == "picked:\n"):
						picked = f.readline()
						if picked == "True":
							self.game.lastPick = self.game.players[len(self.game.players)-1]


					read = f.readline()

		except OSError:
			print("There is no saved game to load!")

		if(f):
			f.close()

		try:
			#game successfully loaded, start the game
			return self.game.gamePlay()

		except:
			return


	#reads cards from the saved file into card objects
	def cardReader(self, line):
		cards = []
		for i in range(len(line)):
			card = line[i].split('-')
			value = int(card[0])
			suit = card[1]
			cards.append(Card(value, suit))
		return cards
