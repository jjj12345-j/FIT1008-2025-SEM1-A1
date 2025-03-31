from __future__ import annotations
from card import Card, CardColor, CardLabel
from config import Config
from data_structures import *

class Player:
    """
    Player class to store the player details
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player

        Returns:
            None

        Complexity:
            assign string- O(1)
            initialising arraysortedlist - O(1)
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.name = name
        self.hand = ArraySortedList(Config.NUM_CARDS_AT_INIT)

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            where k is the cards in hand.
            O(logk) for binary searching where to place card
            O(k) for having to shuffle all cards if card to be place is at beginning (worst)
            O(1) if no shuffling required, where card to be places is at the end (best)
            Best Case Complexity: O(logk)
            Worst Case Complexity: 0(k)
        """
        self.hand.add(card)


    def is_empty(self) -> bool:
        """
        Method to check if the player's hand is empty

        Args:
            None

        Returns:
            bool: True if the player's hand is empty, False otherwise

        Complexity:
            Only checks length of hand, so O(1) for both case
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return self.hand.is_empty()

    def cards_in_hand(self) -> int:
        """
        Method to check the number of cards left in the player's hand

        Args:
            None

        Returns:
            int: The number of cards left in the player's hand

        Complexity:
            Returns length of hand so O(1) for both case
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        return len(self.hand)

    def play_card(
        self, current_color: CardColor, current_label: CardLabel
    ) -> Card | None:
        """
        Method to play a card from the player's hand

        Args:
            current_color (CardColor): The current color of the game
            current_label (CardLabel): The current label of the game

        Returns:
            Card: The first card that is playable from the player's hand

        Complexity:
            Linear scan for hand sortedlist, best case would be where card is at beginning
            of hand and worst case where it is at end

            Best Case Complexity: O(1)
            Worst Case Complexity: O(n)
        """

        #finding lowest card
        for cardIndex in range(len(self.hand)):
            #extra conditional statements for black cards
            if (self.hand[cardIndex].color == current_color or self.hand[cardIndex].label == current_label or(
                self.hand[cardIndex].label == CardLabel.CRAZY) or self.hand[cardIndex].label == CardLabel.DRAW_FOUR):
                cardToBePlayed = self.hand[cardIndex]
                self.hand.remove(self.hand[cardIndex])
                return cardToBePlayed
        return None


    def __str__(self) -> str:
        """
        Return a string representation of the player.

        Optional method for debugging.

        """
        pass

    def __repr__(self) -> str:
        """
        Method to return the string representation of the player

        Args:
            None

        Returns:
            str: The string representation of the player
        """
        return str(self)
