from random import shuffle

class Card:
    suits = ['spade',
            'heart',
            'diamond',
            'club']

    values = [None, None, '2', '3',
              '4', '5', '6', '7',
              '8', '9', '10',
              'jack', 'queen',
              'king', 'ace']

    def __init__ (self, v, s):
        """suit and value - integers"""
        self.value = v
        self.suit = s

    def __lt__ (self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__ (self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__ (self):
        v = self.values[self.value] + ' of ' \
            + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__ (self, name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__ (self):
        name1 = input('Player\'s #1 name is: ')
        name2 = input('Player\'s #2 name is: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins (self, winner):
        w = '{} takes cards'
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d = '{} put {}, and {} put {}'
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Let\'s go!')
        while len(cards) >= 2:
            m = 'Press X for exit. Press any other button to start the game.'
            response = input(m)
            if response == 'X':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)

        print('Game over. {} wins!'.format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return 'Drawn game!'
