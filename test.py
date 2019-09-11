import arcade
import math
import draw

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "test"


class MyGame(arcade.Window):

    def __init__(self):

        self.player = PlayerEntity
        self.W_down = False
        self.S_down = False
        self.A_down = False
        self.D_down = False

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.player.xPos = SCREEN_WIDTH * 0.5
        self.player.yPos = SCREEN_HEIGHT * 0.5
        self.player.speed = 4

    def on_key_press(self, key, modifiers):
        self.KeyEvent(key, True)
    
    def on_key_release(self, key, modifiers):
        self.KeyEvent(key, False)

    def update(self, delta_time):
        if self.W_down: self.player.ModifyY(self.player,  1)
        if self.S_down: self.player.ModifyY(self.player, -1)
        if self.A_down: self.player.ModifyX(self.player, -1)
        if self.D_down: self.player.ModifyX(self.player,  1)

    def on_draw(self):
        arcade.start_render()
        draw.Player(self.player)        

    def KeyEvent(self, key, state):
        if   key == arcade.key.W: self.W_down = state
        elif key == arcade.key.S: self.S_down = state
        elif key == arcade.key.A: self.A_down = state
        elif key == arcade.key.D: self.D_down = state
        
class PlayerEntity:
    
    def __init__(self):
        self.xPos
        self.yPos
        self.speed

    def ModifyY(self, modifier):
        self.yPos += modifier * self.speed
    
    def ModifyX(self, modifier):
        self.xPos += modifier * self.speed

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()