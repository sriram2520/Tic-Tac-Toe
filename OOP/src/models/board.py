from slot_symbol import SlotSymbol

class Board():
  '''
  1|2|3
  -+-+-
  4|5|6
  -+-+-
  7|8|9
  '''
  def __init__(self):
    self.board = { i: SlotSymbol.EMPTY for i in range(1, 10) }
    self.winSlots = [
      # rows
      [1, 2, 3], [4, 5, 6], [7, 8, 9],
      # columns
      [1, 4, 7], [2, 5, 8], [3, 6, 9],
      # diagonals
      [1, 5, 9], [3, 5, 7]
    ]

  def isFresh(self):
    return all(self.board[i] == SlotSymbol.EMPTY for i in self.board)

  def isComplete(self):
    return not SlotSymbol.EMPTY in self.board.values()

  def isValidSlotKey(self, key):
    return key in self.board

  def isSlotAvailable(self, key):
    return SlotSymbol.EMPTY == self.board[key]

  def takeSlot(self, key, symbol):
    self.board[key] = symbol

  def isWinner(self, symbol):
    for eachCombination in self.winSlots:
      if all(self.board[i] == symbol for i in eachCombination):
        return True
    return False

  def getWinnerSymbol(self):
    for symbol in [SlotSymbol.X, SlotSymbol.O]:
      if self.isWinner(symbol):
        return symbol
    return SlotSymbol.EMPTY

  def format(self):
    return ("\n"
+ "   |   |\n"
+ " " + self.board[1].value + " | " + self.board[2].value + " | " + self.board[3].value + "\n"
+ "   |   |\n"
+ "-----------\n"
+ "   |   |\n"
+ " " + self.board[4].value + " | " + self.board[5].value + " | " + self.board[6].value + "\n"
+ "   |   |\n"
+ "-----------\n"
+ "   |   |\n"
+ " " + self.board[7].value + " | " + self.board[8].value + " | " + self.board[9].value + "\n"
+ "   |   |\n")

# if __name__ == '__main__':
#   board = Board()
#   print(board.format())
