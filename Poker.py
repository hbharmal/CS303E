import random

class Card (object):

	# 14 different cards
	RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

	# Clubs, Diamond, Hears, Spades
	SUITS = ('C', 'D', 'H', 'S')

	def __init__ (self, rank = 12, suit = 'S'):
		if (rank in Card.RANKS):
			self.rank = rank
		else:
			self.rank = 12
		
		if (suit in Card.SUITS):
			self.suit = suit
		else:
			self.suit = 'S'

	def __str__ (self):
		if (self.rank == 14):
			rank = 'A'
		elif (self.rank == 13):
			rank = 'K'
		elif (self.rank == 12):
			rank = 'Q'
		elif (self.rank == 11):
			rank = 'J'
		else:
			rank = str(self.rank)
		return rank + self.suit

	def __eq__ (self, other):
		return (self.rank == other.rank)

	def __ne__ (self, other):
		return (self.rank != other.rank)

	def __lt__ (self, other):
		return (self.rank < other.rank)

	def __le__ (self, other):
		return (self.rank <= other.rank)

	def __gt__ (self, other):
		return (self.rank > other.rank)

	def __ge__ (self, other):
		return (self.rank >= other.rank)


class Deck (object):
	def __init__ (self):
		self.deck = []
		for suit in Card.SUITS:
			for rank in Card.RANKS:
				card = Card (rank, suit)
				self.deck.append (card)

	def shuffle (self):
		random.shuffle (self.deck)

	def deal (self):
		if (len(self.deck) == 0):
			return None
		else:
			return self.deck.pop(0)


class Poker (object):
	def __init__ (self, num_players):
		self.deck = Deck()
		self.deck.shuffle()
		self.players = []
		numcards_in_hand = 5

		# assign cards to each player
		for i in range (num_players):
			hand = []
			for j in range (numcards_in_hand):
				hand.append (self.deck.deal())
			self.players.append (hand)

	def play (self):
		# sort the hands of each player and print
		for i in range (len(self.players)):
			sortedHand = sorted (self.players[i], reverse = True)
			self.players[i] = sortedHand
			hand = ''
			for card in sortedHand:
				hand = hand + str (card) + ' '
			print ('Player ' + str (i + 1) + " : " + hand)
		print()

		# determine the each type of hand and print
		points_hand = []  # create list to store points for each hand
		rankings_hand = []
		for i in range (len(self.players)):
			c1 = self.players[i][0].rank
			c2 = self.players[i][1].rank
			c3 = self.players[i][2].rank
			c4 = self.players[i][3].rank
			c5 = self.players[i][4].rank 
			points = 0
			hand = self.players[i]
			if self.is_royal(hand):
				points += 10 
				print("Player %s: Royal Hand" %(i + 1))
			elif self.is_straight_flush(hand):
				points += 9
				print("Player %s: Straight Flush" %(i + 1))
			elif self.is_four_kind(hand):
				points += 8
				print("Player %s: Four of a Kind" %(i + 1))
				# exception in rule
				if (c1 != c2):
					c1 = self.players[i][4]
					c5 = self.players[i][0]
			elif self.is_full_house(hand):
				points += 7
				print("Player %s: Full House" %(i + 1))
				# exception in rule
				if (c1 != c3):
					c1 = self.players[i][3].rank
					c2 = self.players[i][4].rank
					c3 = self.players[i][0].rank
					c4 = self.players[i][1].rank
					c5 = self.players[i][2].rank 
			elif self.is_flush(hand):
				points += 6
				print("Player %s: Flush" %(i + 1))
			elif self.is_straight(hand):
				points += 5
				print("Player %s: Straight" %(i + 1))
			elif self.is_three_kind(hand):
				points += 4
				print("Player %s: Three of a Kind" %(i + 1))
				# exception in rule
				if (c2 == c3 and c3 == c4):
					c1 = self.players[i][1].rank
					c2 = self.players[i][2].rank
					c3 = self.players[i][3].rank
					c4 = self.players[i][0].rank
					c5 = self.players[i][4].rank
				elif (c3 == c4 and c4 == c5):
					c1 = self.players[i][2].rank
					c2 = self.players[i][3].rank
					c3 = self.players[i][4].rank
					c4 = self.players[i][0].rank
					c5 = self.players[i][1].rank
			elif self.is_two_pair(hand):
				points += 3
				print("Player %s: Two Pair" %(i + 1))
				# exception in rule
				if (c1 != c2):
					c1 = self.players[i][1].rank
					c2 = self.players[i][2].rank
					c3 = self.players[i][3].rank
					c4 = self.players[i][4].rank
					c5 = self.players[i][0].rank
				elif (c3 != c4):
					c3 = self.players[i][3].rank
					c4 = self.players[i][4].rank
					c5 = self.players[i][2].rank					
			elif self.is_one_pair(hand):
				points += 2
				print("Player %s: One Pair" %(i + 1))
				# exception in rule
				if (c1 != c2 and c2 != c3):
					c1 = self.players[i][1].rank
					c2 = self.players[i][2].rank
					c3 = self.players[i][3].rank
					c4 = self.players[i][4].rank
					c5 = self.players[i][0].rank				
			else:
				points += 1
				print("Player %s: High Card" %(i + 1))

			# calculate rankings 
			rankings_hand.append(points)

			# calculate total points based on hand
			points = (points * (13 ** 5)) + (c1 * (13 ** 4)) + (c2 * (13 ** 3)) + (c3 * (13 ** 2)) + (c4 * (13 ** 1)) + c5

			# add to the list that store points for each hand
			points_hand.append(points)

		print()

		# determine winner and print
		winner_players = []
		winner_points = max(rankings_hand)

		for i in range(len(points_hand)):
			if (rankings_hand[i] == winner_points):
				winner_players.append(i + 1)
		print(winner_players)
		print(points_hand)

		if (len(winner_players) < 2):
			print("Player %s wins." %(winner_players[0]))
		else:
			sorted(points_hand, reverse = True)
			for i in range(len(points_hand)):
				for j in range(len(winner_players)):
					if (points_hand[winner_players[j] - 1] == points_hand[i]):
						print("Player %s ties." %(winner_players[j]))

	# determine if a hand is a royal flush
	def is_royal (self, hand):
		same_suit = True
		for i in range (len(hand) - 1):
			same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

		if (not same_suit):
			return False

		rank_order = True
		for i in range (len(hand)):
			rank_order = rank_order and (hand[i].rank == 14 - i)
		
		return (same_suit and rank_order)

	
	def is_straight_flush (self, hand):
		# check ranks
		for i in range (1, len(hand)):
			if (hand[i].rank != (hand[i - 1].rank + 1)):
				return False
		
		# check suits
		for i in range (1, len(hand)):
			if (hand[i].suit != hand[i - 1].suit):
				return False

		return True

	def is_four_kind (self, hand):
		# check ranks
		count = 1
		for i in range (1, len(hand)):
			if (hand[i].rank == hand[i - 1].rank):
				count += 1
			else:
				count = 1

		return (count >= 4)


	def is_full_house (self, hand):
		# check ranks
		counts = []
		count = 1
		for i in range (1, len(hand)):
			if (hand[i].rank == hand[i - 1].rank):
				count += 1
			elif (i == len(hand) - 1):
				counts.append(count);
			else:
				counts.append(count)
				count = 1

		return (counts[0] == 2 and counts[1] == 3) or (counts[0] == 3 or counts[1] == 2)

	def is_flush (self, hand):
		# check suits
		for i in range (1, len(hand)):
			if (hand[i].suit != hand[i -1].suit):
				return False

		return True

	def is_straight (self, hand):
		# check ranks
		for i in range (1, len(hand)):
			if (hand[i].rank != (hand[i - 1].rank + 1)):
				return False

		return True

	def is_three_kind (self, hand):
		# check ranks
		count = 0
		for i in range (1, len(hand)):
			if (hand[i].rank == hand[i - 1].rank):
				count += 1

		return (count >= 3)

	def is_two_pair (self, hand):
		# check ranks
		rank_prev = 0
		count = 0
		for i in range (1, len(hand)):
			if (hand[i].rank == hand[i - 1].rank and hand[i].rank != rank_prev):
				rank_prev = hand[i].rank
				count += 1

		return (count == 2)

	
	# determine if a hand is one pair
	def is_one_pair (self, hand):
		for i in range (len(hand) - 1):
			if (hand[i].rank == hand[i + 1].rank):
				return True

		return False

	
	def is_high_card (self, hand):
		return hand[0].rank
		

	

def main():
	# prompt user to enter the number of players
	num_players = int (input ('Enter number of players: '))
	while ((num_players < 2) or (num_players > 6)):
		num_players = int (input ('Enter number of players: '))

	# create the Poker object
	game = Poker (num_players)

	# play the game (poker)
	game.play()

main()















main()