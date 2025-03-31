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
            where n is the number of cards
            assigning card - O(1)
            initialising empty circularqueue and arraylist - O(1)
            appending daw pile - O(n)

            Best Case Complexity: O(n)
            Worst Case Complexity: O(n)
        """
<<<<<<< Updated upstream
        raise NotImplementedError
=======
        self.cards = cards
        #use queue so order of card will be in same order when drawn
        self.draw_pile = CircularQueue(Config.DECK_SIZE)
        #use arraylist so reshuffle will work
        self.discard_pile = ArrayList(Config.DECK_SIZE)
        for card in cards:
            self.draw_pile.append(card)
>>>>>>> Stashed changes

    def discard_card(self, card: Card) -> None:
        """
        Discards the specified card from the player's hand.

        Args:
            card (Card): The card to be discarded.

        Returns:
            None

        Complexity:
            appending card is O(1)
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
<<<<<<< Updated upstream
        raise NotImplementedError
=======
        self.discard_pile.append(card)
>>>>>>> Stashed changes

    def reshuffle(self) -> None:
        """
        Reshuffles cards from the discard pile and add them back to the draw pile.

        Args:
            None

        Returns:
            None

        Complexity:
            where n is number of cards in discard_pile
            shuffling discard_pile - O(nlogn)
            appending draw_pile - O(n)

            Best Case Complexity: O(nlogn)
            Worst Case Complexity: O(nlogn)
        """
<<<<<<< Updated upstream
        raise NotImplementedError
=======
        RandomGen.random_shuffle(self.discard_pile)
        for card in self.discard_pile:
            self.draw_pile.append(card)
        self.discard_pile.clear() #empty discard pile
>>>>>>> Stashed changes

    def draw_card(self) -> Card:
        """
        Draws a card from the draw pile.

        Args:
            None

        Returns:
            Card: The card drawn from the draw pile.

        Complexity:
            where n is the number of cards in discard_pile
            drawing card with serve method- O(1)
            if draw pile is empty and reshuffle is called - O(nlogn)
            Best Case Complexity: O(1)
            Worst Case Complexity: O(nlogn)
        """
<<<<<<< Updated upstream
        raise NotImplementedError
=======
        if self.draw_pile.is_empty():
            self.reshuffle()

        return self.draw_pile.serve()

>>>>>>> Stashed changes
