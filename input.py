import arcade

W_down = False
S_down = False
A_down = False
D_down = False


def KeyEvent(key, modifier, state):
    global W_down, S_down, A_down, D_down
    if   key == arcade.key.W: W_down = state
    elif key == arcade.key.S: S_down = state
    elif key == arcade.key.A: A_down = state
    elif key == arcade.key.D: D_down = state

def WSADtoXY():
    x, y = 0, 0
    if W_down: y += 1
    if S_down: y -= 1
    if A_down: x -= 1
    if D_down: x += 1
    return (x, y)