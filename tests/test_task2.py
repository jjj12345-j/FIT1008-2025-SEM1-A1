from unittest import TestCase

from data_structures.referential_array import ArrayR
from ed_utils.decorators import number, visibility
from data_structures import ArrayList
from ed_utils.timeout import timeout

from game_board import GameBoard
from random_gen import RandomGen
from card import Card, CardColor, CardLabel
from player import Player
from config import Config


class TestGame(TestCase):

    def setUp(self) -> None:
        self.three_cards: ArrayList[Card] = ArrayList(3)
        self.three_cards.insert(0, Card(CardColor.BLUE, CardLabel.FIVE))
        self.three_cards.insert(1, Card(CardColor.RED, CardLabel.THREE))
        self.three_cards.insert(2, Card(CardColor.RED, CardLabel.FIVE))

    @number("2.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_game_board_init(self):
        game_board: GameBoard = GameBoard(self.three_cards)
        self.assertTrue(
            hasattr(game_board, "draw_pile"),
            f"draw_pile not found in GameBoard, please ensure your spelling is correct",
        )
        self.assertTrue(
            hasattr(game_board, "discard_pile"),
            f"discard_pile not found in GameBoard, please ensure your spelling is correct",
        )
        self.assertEqual(len(game_board.draw_pile), 3)
        self.assertEqual(len(game_board.discard_pile), 0)

    @number("2.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_discard_card(self) -> None:
        game_board: GameBoard = GameBoard(self.three_cards)
        self.assertEqual(len(game_board.discard_pile), 0)

        card: Card = Card(CardColor.BLUE, CardLabel.SEVEN)
        game_board.discard_card(card)
        self.assertEqual(
            len(game_board.discard_pile),
            1,
            f"There should be one card in the discard pile, but there are {len(game_board.draw_pile)}",
        )
        self.assertEqual(
            game_board.discard_pile.array[0].color,
            card.color,
            f"First card in discard pile should be BLUE, but is {game_board.discard_pile.array[0].color}",
        )
        self.assertEqual(
            game_board.discard_pile.array[0].label,
            card.label,
            f"First card in unused pile should be SEVEN, but is {game_board.discard_pile.array[0].label}",
        )

    @number("2.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_reshuffle(self) -> None:
        RandomGen.set_seed(5678)
        cards = ArrayList(3)
        cards.insert(0, Card(CardColor.YELLOW, CardLabel.FOUR))
        cards.insert(1, Card(CardColor.BLUE, CardLabel.FIVE))
        cards.insert(2, Card(CardColor.RED, CardLabel.SEVEN))

        game_board: GameBoard = GameBoard(cards)
        self.assertEqual(len(game_board.discard_pile), 0)
        for i in range(3):
            game_board.discard_card(game_board.draw_card())
        self.assertEqual(len(game_board.discard_pile), 3)

        game_board.reshuffle()
        self.assertEqual(len(game_board.draw_pile), 3)
        self.assertEqual(len(game_board.discard_pile), 0)

        first_card = game_board.draw_card()
        second_card = game_board.draw_card()
        third_card = game_board.draw_card()
        self.assertEqual(
            first_card.color,
            CardColor.YELLOW,
            f"First card in draw pile should be YELLOW, but is {first_card.color}",
        )
        self.assertEqual(
            first_card.label,
            CardLabel.FOUR,
            f"First card in draw pile should be FOUR, but is {first_card.label}",
        )
        self.assertEqual(
            second_card.color,
            CardColor.BLUE,
            f"Second card in draw pile should be BLUE, but is {second_card.color}",
        )
        self.assertEqual(
            second_card.label,
            CardLabel.FIVE,
            f"Second card in draw pile should be FIVE, but is {second_card.label}",
        )
        self.assertEqual(
            third_card.color,
            CardColor.RED,
            f"Third card in draw pile should be RED, but is {second_card.color}",
        )
        self.assertEqual(
            third_card.label,
            CardLabel.SEVEN,
            f"Third card in draw pile should be SEVEN, but is {second_card.label}",
        )

    @number("2.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_draw_card(self) -> None:
        game_board: GameBoard = GameBoard(self.three_cards)
        self.assertEqual(len(game_board.discard_pile), 0)
        self.assertEqual(len(game_board.draw_pile), 3)
        card = game_board.draw_card()
        self.assertEqual(
            card.color,
            CardColor.BLUE,
            f"First card drawn should be BLUE, but is {card.color}",
        )
        self.assertEqual(
            card.label,
            CardLabel.FIVE,
            f"First card drawn should be FIVE, but is {card.label}",
        )
        card = game_board.draw_card()
        self.assertEqual(
            card.color,
            CardColor.RED,
            f"First card drawn should be RED, but is {card.color}",
        )
        self.assertEqual(
            card.label,
            CardLabel.THREE,
            f"First card drawn should be THREE, but is {card.label}",
        )
        card = game_board.draw_card()
        self.assertEqual(
            card.color,
            CardColor.RED,
            f"Third card drawn should be RED, but is {card.color}",
        )
        self.assertEqual(
            card.label,
            CardLabel.FIVE,
            f"Third card drawn should be FIVE, but is {card.label}",
        )
