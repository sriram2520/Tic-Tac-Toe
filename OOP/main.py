from tests.set_context import *

# create 2 players
player1 = Player('Sriram', SlotSymbol.X)
player2 = Player('Krishnan', SlotSymbol.O)

# start a game
game = Game(player1, player2)
game.start()

while (not game.hasEnded()):
  print(game.getBoard().format())
  turnPlayer = game.whoseTurn()
  msg = turnPlayer.getName() + ' to play'
  selectedSlot = int(raw_input(msg))
  try:
    game.makeMove(selectedSlot)
  except Exception as e:
    print(e)

print(game.getBoard().format())

if game.isDecisive():
  wonPlayer = game.getWinner()
  print('Winner is: ' + wonPlayer.getName())
else:
  print('Its a TIE')