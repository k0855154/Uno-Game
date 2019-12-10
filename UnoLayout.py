"""
if Card =  whatever color it currently is OR if the current number matches the previous number
"""
from pprint import pprint
#from colorama import init, Fore, Back, Style
import random
#init(convert=True)
#COLORS = [Fore.RED  + 'Red' + Style.RESET_ALL, Fore.BLUE + 'Blue' + Style.RESET_ALL, Fore.GREEN + 'Green' + Style.RESET_ALL, Fore.YELLOW + 'Yellow' + Style.RESET_ALL]
COLORS = ['Red','Blue','Green','Yellow']
WildCardAmount = 4
DrawFourCardAmount = 4
ReverseCardAmount = 2
DrawTwoCardAmount = 2
SkipCardAmount = 2
NUMBERS = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9]
NumOfPlayers = 5
NumberOfCardsToStartWith = 7
class Card(object):
    def __init__(self,number,color):
        self.__number = number
        self.__color = color
    def __str__(self):
        return f"{self.__number} {self.__color}"

    def soft_value(self):
        return self.__color

    def hard_value(self):
        return self.__number

class ReverseCard(Card):
    """
    Reverses The Player Turns
    """
    def __init__(self, color):
        Card.__init__(self, u'\u27f2' + " ", color)
        self.__color = color
    def soft_value(self):
        return self.__color

    def hard_value(self):
        return 12

class SkipCard(Card):
    """
    Skips a player's turn
    """
    def __init__(self,color):
        Card.__init__(self,u"\u2298", color)
        self.__color = color
    def soft_value(self):
        return self.__color

    def hard_value(self):
        return 14

class DrawFourWild(Card):
    """
    Draw Four Cards and Pick a Different Color
    """
    def __init__(self):
        Card.__init__(self,"+4", "Pick Color")

    def soft_value(self):
        return 5

    def hard_value(self):
        return 16
class ZeroCard(Card):
    """
    Just another Number Card
    """
    def __init__(self, color):
        Card.__init__(self,"0",color)
        self.__color = color
    def soft_value(self):
        return self.__color

    def hard_value(self):
        return 0

class WildCard(Card):
    """
    Pick a different Color
    """
    def __init__(self):
        Card.__init__(self,"Pick a Color","")

    def soft_value(self):
        return 5

    def hard_value(self):
        return 11
class DrawTwo(Card):
    """
    Pick a different Color
    """
    def __init__(self,color):
        Card.__init__(self,"+2",color)
        self.__color = color
    def soft_value(self):
        return self.__color

    def hard_value(self):
        return 15
class Deck:
    """
    A Deck represents the table's deck of cards, which is used to create
    a Hand (colleciton of cards).
    """
    def __init__(self):
        self.__cards = self.__load_deck()

    def __shuffle(self, deck):
        random.shuffle(deck)

    def __load_deck(self):
        """
        Creates a deck of 102 cards. Consists of 4 suits, each of which 
        contain, 1-10, Eight Skips, Eight Reverses, Eight Draw 2s, Four Draw 4s, and  Four Wild Cards.
        """
        ###################################################################
        DeckOfCards = []
        for c in COLORS:
            ZCard = ZeroCard(c)
            DeckOfCards.append(ZCard)
            for n in NUMBERS:
                NumCard = Card(n, c)
                DeckOfCards.append(NumCard)
            for r in range(ReverseCardAmount):
                RevCard = ReverseCard(c)
                DeckOfCards.append (RevCard)
            for dt in range(DrawTwoCardAmount):
                DT = DrawTwo(c)
                DeckOfCards.append(DT)
            for s in range(SkipCardAmount):
                Skip = SkipCard(c)
                DeckOfCards.append(Skip)
        for df in range(DrawFourCardAmount):
            DF = DrawFourWild()
            DeckOfCards.append(DF)
        for w in range(WildCardAmount):
            W = WildCard()
            DeckOfCards.append(W)
        self.__shuffle(DeckOfCards)
        """
        for i in range(len(DeckOfCards)):
            print(DeckOfCards[i])
        print(len(DeckOfCards))
        """
        return DeckOfCards
        ###################################################################
    def deal_card(self):
        """
        Removes a Card from the Deck and returns it so that it can
        enter play. If the deck is empty, deal_card() should create a 
        new deck, shuffle it, and deal a card.
        """
        ###################################################################
        DealtCard = self.__cards.pop()
        return DealtCard
        ###################################################################
    def readd_card(self,Card):
        """
        Readds a Card to the Deck. If the deck is empty, deal_card() should create a 
        new deck, shuffle it, and deal a card.
        """
        ###################################################################
        self.__cards.append(Card)
        ###################################################################

class Hand(object):
    """
    A Hand represents a player's current hand of cards.
    """
    def __init__(self):
        self.__cards = []
        self.__index = 1

    def __iter__(self):
        """
        Called when an iterator is requested for this object
        """
        self.__index = 1
        return self

    def __next__(self):
        """
        Called when the next() method is called on an iterator of this
        object.
        """
        try:
            card = self.__cards[self.__index]
            self.__index += 1
        except IndexError:
            raise StopIteration
        else:
            return card

    def get_hole_card(self):
        """
        Returns the hole card, but doesn't remove it from the Hand.
        """
        return self.__cards[0]

    def clear(self):
        """
        Removes all cards from the Hand in prep for another round
        """
        self.__index = 1
        ###################################################################
        self.__cards.clear()
        ###################################################################
    
    def add_card(self, card):
        """
        Adds a Card to the Hand. If the Hand is empty, the card should go
        into the hole; otherwise, the card should be showing.
        """
        ###################################################################
        self.__cards.append(card)
        ###################################################################

    def get_color(self,DiscardPile):
        """
        Loops over the Cards in the Hand and returns the soft score
        """
        ###################################################################
        """
        total = 0
        for i in range(len(self.__cards)):
            total += int(self.__cards[i].soft_value()) 
        return total
        """
    
    
        #Coloring = self.__cards[len(DiscardPile)-1].soft_value()
        #return Coloring
        
        ###################################################################

    def get_number(self,DiscardPile):
        """
        Loops over the Cards in the Hand and returns the hard score
        """
        ###################################################################
        """
        total = []
        for i in range(len(self.__cards)):
            total.append(self.__cards[i].hard_value()) 
        return total
        """
        Number = 0
        Number = self.__cards[len(DiscardPile)-1].hard_value()
        return Number
        ###################################################################
class PlayerList(dict):
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value
"""
class Discarding(list):
    def __init__(self):
        self.__DiscardPile = []
        self.__CurrentColor = []
        self.__CurrentNumber = []
    
    def __Add_to_discard(self,discard):
        self.__DiscardPile.append(discard)
        self.__CurrentColor.append(Hand.get_color(self.__DiscardPile))
        self.__CurrentNumber.append(Hand.get_number(self.__DiscardPile))
    
    def __Get_color(self):
        return self.__CurrentColor[len(self.__DiscardPile)-1]
    
    def __Get_number(self):
        return self.__CurrentNumber[len(self.__DiscardPile)-1]    
 """   
class Game(object):
    """
    Represents a (Amount of players ex: 3) player game of Uno. Has a deck, the player's
    hand.
    """
    def __init__(self):
        self.__deck = Deck()
        self.__player = Hand()
        self.__players = PlayerList() 
        self.__DiscardPile = []
        self.__CurrentColor = []
        self.__CurrentNumber = []
        self.__First_Card()
        self.__PlayersTurn = -1
        for i in range(NumOfPlayers):
            self.__players.add(f'Player{i}',self.DealCardsToPlayers(NumberOfCardsToStartWith))
        self.__Turn = self.__Turn_Calculations()
        for i in range(2):
            self.__PlayedCard = self.__Play_Card(self.__Turn)
        #self.__Play_Card()
    """
    Deal Cards to Each Player, Starting the game"
    """
    def __Add_to_discard(self,discard):
        self.__DiscardPile.append(discard)
        CC = discard.soft_value()
        self.__CurrentColor.append(CC)
        CN = discard.hard_value()
        self.__CurrentNumber.append(CN)
        return self.__DiscardPile, self.__CurrentColor, self.__CurrentNumber
        #, self.__CurrentColor
        #, self.__CurrentNumber
    def __Get_color(self):
        return self.__CurrentColor[len(self.__DiscardPile)-1]
    
    def __Get_number(self):
        return self.__CurrentNumber[len(self.__DiscardPile)-1]    
    
    
    def __First_Card(self):
        card = self.__deck.deal_card()
        x,color,number = self.__Add_to_discard(self.__deck.deal_card())
        print(color[len(color)-1])
        print(number[len(number)-1])
        if color[len(color)-1] == int(5):
            self.__deck.readd_card(card)
            self.__First_Card()
        else:
            print()
        self.__CurrentNumber.append(number[len(number)-1])
        self.__CurrentColor.append(color[len(color)-1])
    
    def DealCardsToPlayers(self,number):
        CARDS = []
        CardDisplay = []
        for i in range(number):
            Card = []
            card = self.__deck.deal_card()
            self.__player.add_card(card)
            CARDS.append(card)
            CardDisplay.append(f'{card}')
            Card.append(CARDS)
            Card.append(CardDisplay)
        return Card
    
    def __Print_Players_Cards(self):
        self.__player0 = self.__players.get("Player0")
        print(f'Your Hand Of Cards: {self.__player0[1]}')
    
    def __Take_From_Deck(self,number,player):
        for _ in range(number):
            card = self.__deck.deal_card()
            self.__players[player].append(card)
    def __Turn_Calculations(self):
        self.__PlayersTurn += 1
        playerTurns = []
        for key in self.__players.keys():
            playerTurns.append(key)
        print(playerTurns)
        return playerTurns[self.__PlayersTurn]
    
    def __Next_Turn(self):
        playerTurns = self.__Turn_Calculations
        if playerTurns == "Player0":
            self.__Play_Card()
        else:
            self.__PlayAI()
    
    def __Get_Card_Amount(self):
        CardAmount = self.__player0[1]
        CardAmount = len(CardAmount)
        Card_Selection = []
        for _ in (number+1 for number in range(CardAmount)):
            Card_Selection.append(str(_))
        return Card_Selection
    
    def __prompt(self,prompt,choices):
        action = input(prompt)
        if action in choices:
            return action
        else:
            print("Invalid selection")
            return self.__prompt(prompt, choices)
    
    def __Play_Card(self,turn):
        if turn == "Player0":
            self.__ValidCardInHand()
            self.__Print_Players_Cards()
            selectionCards = self.__Get_Card_Amount()
            select = self.__prompt("Which card would you like to play? ",selectionCards)
            """
            0 for self.__player is the object itself
            1 for self.__player is the object decoded so it is readable
            """
            Hand = self.__player0[0]
            hand = self.__player0[1]
            """
            The following removes the selected card from self.__prompt from the hand
            """
            card = Hand[int(select)-1]
            cards = hand[int(select)-1]
            SelectedCard = int(select)-1
            self.__player0 = cards
            self.__color = card.soft_value()
            self.__number = card.hard_value()
            if self.__ValidateCard() == True:
                card = Hand.pop(SelectedCard)
                cards = hand.pop(SelectedCard)
            else:
                self.__Play_Card(self.__Turn)
            #x,self.__color,self.__number = self.__Add_to_discard(card)
            #print(self.__color[len(self.__color)-1])
            #print(self.__number[len(self.__number)-1])
        else:
            self.__PlayAI()
        return self.__color,self.__number
    
    def __Get_Card_Type(self,PreviousCard):
        self.__previousCard = PreviousCard



    def __ValidateCard(self):
        print(self.__CurrentColor)
        print(self.__CurrentNumber)
        print(self.__color)
        print(self.__number)
        if self.__color == self.__CurrentColor[len(self.__CurrentColor)-1] or self.__number == self.__CurrentNumber[len(self.__CurrentNumber)-1]:
            print("Valid Card")
            if self.__color == self.__CurrentColor[len(self.__CurrentColor)-1]:
                self.__CurrentNumber.append(self.__number)
            else:
                self.__CurrentColor.append(self.__color)
            Statement = True
        elif self.__color == 5:
            print("WILD CARD")
            self.__WildCard()
            Statement = True
        else:
            print("Invalid Card")
            Statement = False
        return Statement
    def __WildCard(self):
        self.__CurrentColor.append(self.__prompt("Select a Color: ",COLORS))

    #def __WildCardAI(self,player):


    def __ValidCardInHand(self):
        self.__player0 = self.__players.get(self.__PlayerNumber)
        Crd = []
        print(self.__player0[1])
        for card in self.__playerNumber[0]:
            Crd.append(card.soft_value())
            print(Crd)
        print(self.__CurrentColor)
        if self.__CurrentColor[len(self.__CurrentColor)-1] in Crd:
            print("Good Card in Hand")
        else:
            self.__Take_From_Deck(1,self.__Turn)
    def __GetTurn(self):
        
    def __PlayAI(self):
        self.__


Game()
