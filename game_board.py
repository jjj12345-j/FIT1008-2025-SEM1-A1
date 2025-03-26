from __future__ import annotations
from card import Card
from random_gen import RandomGen
from config import Config
from data_structures import *


class GameBoard:
    """
    GameBoard class to store cards in draw pile and discard pile
    """

    def __init__(self, cards: ArrayList[Card]):
        """
        Constructor for the GameBoard class

        Args:
            cards (ArrayList[Card]): The list of cards to be used in the game

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.cards = cards
        #use queue so order of card will be in same order when drawn
        self.draw_pile = CircularQueue(Config.DECK_SIZE)
        #use arraylist so reshuffle will work
        self.discard_pile = ArrayList(Config.DECK_SIZE)
        for card in cards:
            self.draw_pile.append(card)
        # raise NotImplementedError

    def discard_card(self, card: Card) -> None:
        """
        Discards the specified card from the player's hand.

        Args:
            card (Card): The card to be discarded.

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.discard_pile.append(card)
        # raise NotImplementedError

    def reshuffle(self) -> None:
        """
        Reshuffles cards from the discard pile and add them back to the draw pile.

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        print(len(self.discard_pile))
        RandomGen.random_shuffle(self.discard_pile)
        for card in self.discard_pile:
            self.draw_pile.append(card)
        self.discard_pile.clear() #empty discard pile
        # raise NotImplementedError

    def draw_card(self) -> Card:
        """
        Draws a card from the draw pile.

        Args:
            None

        Returns:
            Card: The card drawn from the draw pile.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        if self.draw_pile.is_empty():
            self.reshuffle()

        return self.draw_pile.serve()
        # raise NotImplementedError
