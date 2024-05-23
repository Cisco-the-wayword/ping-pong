from turtle import *

def line(x1, y1, x2, y2):
    """Draw a line from (x1, y1) to (x2, y2)."""
    up()
    goto(x1, y1)
    down()
    goto(x2, y2)
    up()

def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

def drawx(x, y):
    """Draw X player."""
    color('red')
    width(5)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)

def drawo(x, y):
    """Draw O player."""
    color('blue')
    width(5)
    up()
    goto(x + 67, y + 5)
    down()
    circle(62)

def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200

state = {'player': 0, 'board': {}}
players = [drawx, drawo]

def check_winner():
    """Check if there is a winner."""
    board = state['board']
    for player in [0, 1]:
        # Check rows
        for y in range(-200, 200, 133):
            if all((x, y) in board and board[(x, y)] == player for x in range(-200, 200, 133)):
                return True
        # Check columns
        for x in range(-200, 200, 133):
            if all((x, y) in board and board[(x, y)] == player for y in range(-200, 200, 133)):
                return True
        # Check diagonals
        if all((d, d) in board and board[(d, d)] == player for d in range(-200, 200, 133)):
            return True
        if all((d, -d) in board and board[(d, -d)] == player for d in range(-200, 200, 133)):
            return True
    return False

def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    if (x, y) in state['board']:
        return
    player = state['player']
    draw = players[player]
    draw(x, y)
    state['board'][(x, y)] = player
    update()
    if check_winner():
        print("Player", player, "wins!")
        return
    state['player'] = not player

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
