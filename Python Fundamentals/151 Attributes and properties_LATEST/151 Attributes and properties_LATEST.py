# 151 Attributes and properties 

import random

class Suit: 
    Club="♣" 
    Diamond="♦" 
    Heart="♥" 
    Spade="♠" 

class BlackJackCard:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self):
        return f'{self.__class__.__name__}(face={self.face}, suit={self.suit})'
    
    def __str__(self):
        return f'{self.face} {self.suit}'
    
    @property
    def hard(self):
        if self.face in ('Jack', 'Queen', 'King'):
            return 10
        elif self.face == 'Ace':
            return 1
        else:
            return int(self.face)
    
    @property    
    def soft(self):
        if self.face == 'Ace':
            return 11
        else:
            return self.hard
        
class Deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return ', '.join(map(str, self.cards))
    
    def populate_deck(self):
        suits = [Suit.Club, Suit.Diamond, Suit.Heart, Suit.Spade]
        faces = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        for f in faces:
            for s in suits:
                self.cards.append(BlackJackCard(f, s))
        return self.cards

    def pop_card(self):
        popped = self.cards.pop()
        return popped

    def shuffle_deck(self):
        random.shuffle(self.cards)
        return self.cards
    
    
class Hand_Lazy:
    def __init__(self, *cards):
        self.cards = list(cards)

    def __str__(self):
        return ', '.join(map(str, self.cards))
    
    @property 
    def total(self):
        delta_soft = max(c.soft - c.hard for c in self.cards)
        hard_total = sum(c.hard for c in self.cards)
        if delta_soft + hard_total <= 21:
            return delta_soft + hard_total
        else:
            return hard_total



if __name__ == '__main__':

    d = Deck()
    d.populate_deck()
    print(d)

    h = Hand_Lazy(d.pop_card(),d.pop_card(), d.pop_card())
    print(h)
    print(h.total)

    d.shuffle_deck()
    print(d)

    h2 = Hand_Lazy(d.pop_card(),d.pop_card(), d.pop_card())
    print(h2)
    print(h2.total)
