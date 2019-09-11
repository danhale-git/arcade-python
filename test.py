import arcade
import math
import draw
import input

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "test"


class MyGame(arcade.Window):

    def __init__(self):

        self.player = PlayerEntity

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player.xPos = SCREEN_WIDTH * 0.5
        self.player.yPos = SCREEN_HEIGHT * 0.5
        self.player.speed = 4

    def on_key_press(self, key, modifiers):
        input.KeyEvent(key, modifiers, True)
    
    def on_key_release(self, key, modifiers):
        input.KeyEvent(key, modifiers, False)

    def update(self, delta_time):
        self.player.Move(self.player, input.WSADtoXY())

    def on_draw(self):
        arcade.start_render()
        draw.Player(self.player)        

class PlayerEntity:
    __slots__ = ['xPos', 'yPos', 'speed']    
    def __init__(self):
        self.xPos
        self.yPos
        self.speed

    def Move(self, xy):
        x, y = xy
        self.xPos += x * self.speed
        self.yPos += y * self.speed

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()