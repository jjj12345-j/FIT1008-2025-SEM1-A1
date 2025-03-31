from __future__ import annotations
from player import Player
from game_board import GameBoard
from card import CardColor, CardLabel, Card
from random_gen import RandomGen
from config import Config
from data_structures import *


class Game:
    """
    Game class to play the game
    """

    def __init__(self) -> None:
        """
        Constructor for the Game class

        Args:
            None

        Returns:
            None

        Complexity:
            assignments - o(1)
            initialising empty arraylist - O(1)
            Best Case Complexity: o(1)
            Worst Case Complexity: O(1)
        """

        self.currentPlayerIndex = -1 #-1 mean game havent start
        self.playerTurnDirection = 1 # changes to negative when in reverse
        self.players = ArrayList()
        self.current_player = None
        self.current_color = None
        self.current_label = None
        self.game_board = None

    def generate_cards(self) -> ArrayList[Card]:
        """
        Method to generate the cards for the game

        Args:
            None

        Returns:
            ArrayList[Card]: The list of Card objects generated

        Complexity:
            where n is the deck size
            complexity is O(n log n) because of shuffle
            Best Case Complexity: O(n log n)
            Worst Case Complexity: O(n log n)
        """
        list_of_cards: ArrayList[Card] = ArrayList(Config.DECK_SIZE)
        idx: int = 0

        # Generate 4 sets of cards from 0 to 9 for each color
        for color in CardColor:
            if color != CardColor.BLACK:
                # Generate 4 sets of cards from 0 to 9 for each color
                for i in range(10):
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1

                # Generate 2 of each special card for each color
                for i in range(2):
                    list_of_cards.insert(idx, Card(color, CardLabel.SKIP))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.REVERSE))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.DRAW_TWO))
                    idx += 1
            else:
                # Generate black crazy and draw 4 cards
                for i in range(4):
                    list_of_cards.insert(idx, Card(CardColor.BLACK, CardLabel.CRAZY))
                    idx += 1
                    list_of_cards.insert(
                        idx, Card(CardColor.BLACK, CardLabel.DRAW_FOUR)
                    )
                    idx += 1

                # Randomly shuffle the cards
                RandomGen.random_shuffle(list_of_cards)

                return list_of_cards

    def initialise_game(self, players: ArrayList[Player]) -> None:
        """
        Method to initialise the game

        Args:
            players (ArrayList[Player]): The list of players

        Returns:
            None

        Complexity:
            where p if the number of players
            where n is the deck size
            where c is the NUM_CARDS_AT_INIT
            where k is the cards in hand.

            populating player attribute - o(p)
            generating cards- O(nlogn)

            players starting hand:
                drawing enough cards - o(c)
                each player drawing a card- 0(p)
                adding card player hand- O(logk) (best), o(k) (worst)

            first card:
                draw_card at first loop and draw_pile isn't empty - O(1) (best case)
                keeps drawing non-number card and draw_pile is empty - O(n^2logn)



            Best Case Complexity: O(p + n log n + p·c·logk)
            Worst Case Complexity: O(p + p·c·n^2logn)
        """
        #populating player attribute
        for player in players:
            self.players.append(player)

        self.game_board = GameBoard(self.generate_cards())

        #each player draw card until limit
        for numOfCardsDrawn in range(Config.NUM_CARDS_AT_INIT):
            for player in self.players:
                player.add_card(self.game_board.draw_card())


        topCard =None
        while topCard is None or topCard.label.value > 9:
            #loop until a number card is drawn
            topCard = self.game_board.draw_card()
            self.game_board.discard_card(topCard)

        self.current_color = topCard.color
        self.current_label = topCard.label




    def next_player(self) -> Player:
        """
        Method to get the next player

        Args:
            None

        Returns:
            Player: The next player

        Complexity:
            math operation has O(1)
            accessing list has O(1)
            Best Case Complexity: O(1)
            Worst Case Complexity:O(1)
        """
        if self.currentPlayerIndex == -1:
            return self.players[0]

        # using modulo so index doesn't go out of range
        nextPlayerIndex = (self.currentPlayerIndex + self.playerTurnDirection) % len(self.players) #new
        return self.players[nextPlayerIndex] #new

    def reverse_players(self) -> None:
        """
        Method to reverse the order of the players

        Args:
            None

        Returns:
            None

        Complexity:
            math operation - O(1)
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.playerTurnDirection *= -1
        if self.currentPlayerIndex == -1:
            self.currentPlayerIndex += 1


    def skip_next_player(self) -> None:
        """
        Method to skip the next player in the game

        Args:
            None

        Returns:
            None

        Complexity:
            calling next_player- O(1)
            math operation- O(1)
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.current_player = self.next_player()
        self.currentPlayerIndex = (self.currentPlayerIndex + self.playerTurnDirection) % len(self.players)


    def play_draw_two(self) -> None:
        """
        Method to play a draw two card

        Args:
            None

        Returns:
            None

        Complexity:
            where k is the number of cards in player hand
            where d in the number of cards in draw pile
            skip player- O(1)
            draw card(arg:false)- O(k + dlogd) (worst), O(logk) (best)

            Best Case Complexity: O(logk)
            Worst Case Complexity: O(k + dlogd)
        """

        self.skip_next_player()
        self.draw_card(self.current_player, False)
        self.draw_card(self.current_player, False)


    def play_black(self, card: Card) -> None:
        """
        Method to play a crazy card

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            where k is the number of cards in player hand
            draw card(arg:false)- O(k + dlogd) (worst), O(logk) (best)
            setting current color using random- O(4)

            Best Case Complexity: O(log k)
            Worst Case Complexity: O(k + dlogd)
        """
        if card.label == CardLabel.DRAW_FOUR:
            self.skip_next_player()
            for cardCount in range(4):
               self.draw_card(self.current_player, False)
        self.current_color = CardColor(RandomGen.randint(0,3))

    def draw_card(self, player: Player, playing: bool) -> Card | None:
        """
        Method to draw a card from the deck

        Args:
            player (Player): The player who is drawing the card
            playing (bool): A boolean indicating if the player is able to play the card

        Returns:
            Card - When drawing a playable card, other return None

        Complexity:
            where n in DECK_SIZE
            where d in number of cards in draw_pile
            where k is the cards in hand.
            calling gameboard draw_card- O(1) (best), O(dlogd) (worst)
            checking if card is playable - O(1)
            adding card- O(logk)(best), 0(k) (worst)
            Best Case Complexity: O(1) (card is playable, so no need add_card)
            Worst Case Complexity: O(k + dlogd)
        """
        newCard = self.game_board.draw_card()
        if playing == True and (
                newCard.color == self.current_color or newCard.label == self.current_label):
            return newCard
        player.add_card(newCard)
        return None

    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game
        """
        self.generate_cards()
        winner = False
        while winner == False:
            self.current_player = self.next_player()
            self.currentPlayerIndex = (self.currentPlayerIndex + self.playerTurnDirection) % len(self.players)
            currentPlayer = self.current_player
            #variable to keep track of current player before it gets changed when other cards are played.
            cardPlayed = self.current_player.play_card(self.current_color,self.current_label)
            if cardPlayed is None:
                cardPlayed = self.draw_card(self.current_player, True)
            if cardPlayed is not None:
                self.game_board.discard_card(cardPlayed)
                match (cardPlayed.label):
                    case CardLabel.DRAW_FOUR:
                        #next player skipped
                        self.play_black(cardPlayed)
                    case CardLabel.CRAZY:
                        self.play_black(cardPlayed)
                    case CardLabel.DRAW_TWO:
                        #next player skipped
                        self.play_draw_two()
                    case CardLabel.REVERSE:
                        self.reverse_players()
                    case CardLabel.SKIP:
                        self.skip_next_player()
                    case _:
                        pass

            #so card color doesn't change after black is played
            #ignore changeing current color and label if no card played
            if cardPlayed is not None and cardPlayed.color != CardColor.BLACK:
                self.current_label = cardPlayed.label
                self.current_color = cardPlayed.color
            elif cardPlayed is not None:
                self.current_label = cardPlayed.label

            if currentPlayer.is_empty():
                return currentPlayer
