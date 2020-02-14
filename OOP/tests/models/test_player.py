import unittest

from set_context import *

class TestPlayer(unittest.TestCase):
  def test_create_player(self):
    name = 'Sriram'
    symbol = SlotSymbol('X')
    player = Player(name, symbol)
    self.assertEqual(name, player.getName())
    self.assertEqual(symbol, player.getSymbol())
