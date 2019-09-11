import arcade
import math

def Player(player):
        
    backRight = (25, -50)
    backLeft = (-25, -50)
    front = (0, 0)

    x = player.xPos
    y = player.yPos

    arcade.draw_triangle_filled(x+front[0],     y+front[1],
                                x+backLeft[0],  y+backLeft[1],
                                x+backRight[0], y+backRight[1],

                                arcade.color.ALLOY_ORANGE)