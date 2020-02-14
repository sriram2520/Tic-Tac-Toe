from .board import Board
from .slot_symbol import SlotSymbol

class Game():
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2

  def initGameSetup(self):
    self.board = Board()
    self.currentMovePlayer = self.player1

  def getBoard(self):
    return self.board

  def start(self):
    self.initGameSetup()

  def hasEnded(self):
    # check if board is complete
    # if yes, return true
    if self.board.isComplete():
      print('complete')
      return True
    # check if board has a winner
    # if yes, return true
    if self.board.getWinnerSymbol() != SlotSymbol.EMPTY:
      print(self.board.getWinnerSymbol())
      return True
    return False

  def whoseTurn(self):
    return self.currentMovePlayer

  def changeTurn(self):
    if self.currentMovePlayer == self.player1:
      self.currentMovePlayer = self.player2
    else:
      self.currentMovePlayer = self.player1

  def makeMove(self, key):
    # check if input is valid
    if not self.board.isValidSlotKey(key):
      raise Exception('Invalid key selected')
    # check if slot is available
    if not self.board.isSlotAvailable(key):
      raise Exception('Slot already taken')
    # take the slot for current player
    self.board.takeSlot(key, self.currentMovePlayer.getSymbol())

    # set next player turn
    self.changeTurn()

  def isDecisive(self):
    return self.board.getWinnerSymbol() != SlotSymbol.EMPTY

  def getWinner(self):
    winnerSymbol = self.board.getWinnerSymbol()
    print(winnerSymbol)
    if winnerSymbol == self.player1.getSymbol():
      return self.player1
    elif winnerSymbol == self.player2.getSymbol():
      return self.player2
