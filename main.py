import pgzrun
from pgzero.actor import Actor


def draw():
    """
    A method for drawing anything with any change (execute by pgzrun.go())
    :return:
    """
    back.draw()
    bob.draw()
    patrick.draw()
    plankton.draw()


def update():
    """
    A method for updating and refresh anything 60 times per second (execute by pgzrun.go())
    :return:
    """
    pass


WIDTH = 1280
HEIGHT = 720
TITLE = "SpongeBob"

# Define background
back = Actor("back")

# Define bob
bob = Actor("bob_right_prev_ui")
bob.x = 300
bob.y = 550

# Define patric
patrick = Actor("patric_left_prev_ui")
patrick.x = 950
patrick.y = 450

# Define plankton
plankton = Actor("plankton_right")
plankton.x = WIDTH//2
plankton.y = HEIGHT * 0.7

pgzrun.go()
