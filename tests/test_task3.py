from copy import copy
from unittest import TestCase

from ed_utils.decorators import number, visibility
from data_structures import ArrayList
from ed_utils.timeout import timeout

from game import Game
from random_gen import RandomGen
from card import CardColor, CardLabel
from player import Player
from config import Config
from card import Card


class TestGame(TestCase):
    def setUp(self) -> None:
        # Set seed
        RandomGen.set_seed(112)

        self.players: ArrayList[Player] = ArrayList(4)
        a = Player("Alice")
        b = Player("Bob")
        c = Player("Charlie")
        d = Player("David")
        self.players.insert(0, a)
        self.players.insert(1, b)
        self.players.insert(2, c)
        self.players.insert(3, d)

        # Set number of cards at init
        Config.NUM_CARDS_AT_INIT = 7

        # Set up a game
        self.game: Game = Game()
        self.game.initialise_game(self.players)

    @number("3.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_black_crazy(self) -> None:
        # Check the current color
        self.assertEqual(
            self.game.current_color,
            CardColor.YELLOW,
            f"Current color should be YELLOW, but is {self.game.current_color}",
        )

        # Play a crazy card
        card: Card = Card(CardColor.BLACK, CardLabel.CRAZY)
        self.game.play_black(card)

        # Check the new color
        self.assertEqual(
            self.game.current_color,
            CardColor.BLUE,
            f"Current color should be BLUE, but is {self.game.current_color}",
        )

    @number("3.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_black_draw_four(self) -> None:
        # Assume `next_player` is Alice for testing purpose

        # Check the current color
        self.assertEqual(
            self.game.current_color,
            CardColor.YELLOW,
            f"Current color should be YELLOW, but is {self.game.current_color}",
        )

        # Check the number of cards for the next player
        self.assertEqual(
            self.players[0].cards_in_hand(),
            7,
            f"Alice should have 7 cards, but has {self.players[0].cards_in_hand()}",
        )

        # Play a crazy card
        card: Card = Card(CardColor.BLACK, CardLabel.DRAW_FOUR)
        self.game.play_black(card)

        # Check the new color
        self.assertEqual(
            self.game.current_color,
            CardColor.BLUE,
            f"Current color should be BLUE, but is {self.game.current_color}",
        )

        # Check the number of cards for the next player
        self.assertEqual(
            self.players[0].cards_in_hand(),
            11,
            f"Alice should have 11 cards, but has {self.players[0].cards_in_hand()}",
        )

        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(
            next_player.name,
            "Bob",
            f"Next player should be Bob, but is {next_player.name}",
        )

    @number("3.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_draw_card_not_playing(self) -> None:
        # Check the number of cards for the next player
        self.assertEqual(
            self.players[0].cards_in_hand(),
            7,
            f"Alice should have 7 cards, but has {self.players[0].cards_in_hand()}",
        )

        # Draw a card
        self.game.draw_card(self.players[0], False)

        # Check the number of cards for the next player
        self.assertEqual(
            self.players[0].cards_in_hand(),
            8,
            f"Alice should have 8 cards, but has {self.players[0].cards_in_hand()}",
        )

    @number("3.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_draw_card_playing(self) -> None:
        # Check current color and label
        self.assertEqual(
            self.game.current_color,
            CardColor.YELLOW,
            f"Current color should be YELLOW, but is {self.game.current_color}",
        )
        self.assertEqual(
            self.game.current_label,
            CardLabel.SEVEN,
            f"Current label should be SEVEN, but is {self.game.current_label}",
        )

        # Check the number of cards for the next player
        self.assertEqual(
            self.players[0].cards_in_hand(),
            7,
            f"Alice should have 7 cards, but has {self.players[0].cards_in_hand(),} cards",
        )

        # Draw a card
        self.game.draw_card(self.players[0], True)

        # Check the number of cards for the next player
        self.assertEqual(
            self.players[0].cards_in_hand(),
            8,
            f"Alice should have 8 cards after playing the drawn card, but has {self.players[0].cards_in_hand()}",
        )

    @number("3.5")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_next_player(self) -> None:
        # Check the next player
        next_player: Player = self.game.next_player()

        self.assertIsInstance(
            next_player,
            Player,
            f"Next player should be an instance of Player, but is {type(next_player)}",
        )
        self.assertEqual(
            next_player.name,
            "Alice",
            f"Next player should be Alice, but is {next_player.name}",
        )

    @number("3.6")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_reverse(self) -> None:
        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(
            next_player.name,
            "Alice",
            f"Next player should be Alice, but is {next_player.name}",
        )

        # Call the reverse method
        self.game.reverse_players()

        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(
            next_player.name,
            "David",
            f"Next player should be David, but is {next_player.name}",
        )

    @number("3.7")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_skip(self) -> None:
        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(
            next_player.name,
            "Alice",
            f"Next player should be Alice, but is {next_player.name}",
        )

        # Call the skip method
        self.game.skip_next_player()

        # Check the next player
        next_player: Player = self.game.next_player()
        self.assertEqual(
            next_player.name,
            "Bob",
            f"Next player should be Bob, but is {next_player.name}",
        )
