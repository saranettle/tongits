# initialize a deck
# deck has ace, 2-10, Jack, Queen, and King
# four suits, Heart, Diamond, Club, and Spade
# define what a card is

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.player = None
        self.location = "deck"

    def show_card(self):
        return self.rank, self.suit

class Deck:
    def __init__(self):
        self.cards = self.build_deck()
        self.quantity = 52

    def build_deck(self):
        
        deck = []
        suits = ["heart", "diamond", "club", "spade"]
        
        for suit in suits:
            for num in range(13):
                match num:
                    case 0:
                        deck.append(Card("ace", suit))
                    case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
                        deck.append(Card(str(num+1), suit))
                    case 10:
                        deck.append(Card("jack", suit))
                    case 11:
                        deck.append(Card("queen", suit))
                    case 12:
                        deck.append(Card("king", suit))
        
        return deck
    
    def print_deck(self):
        
        for card in self.cards:
            print(card.show_card())
    
deck = Deck()
deck.print_deck()
