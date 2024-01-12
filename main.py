import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


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
    # Bob section
    if keyboard.right:
        bob.x += bob.speed
    if keyboard.left:
        bob.x -= bob.speed
    if keyboard.up:
        bob.y -= bob.speed
    if keyboard.down:
        bob.y += bob.speed


WIDTH = 1280
HEIGHT = 720
TITLE = "SpongeBob"

# Define background
back = Actor("back")

# Define bob
bob = Actor("bob_right_prev_ui")
bob.x = 300
bob.y = 550
bob.speed = 5

# Define patrick
patrick = Actor("patric_left_prev_ui")
patrick.x = 950
patrick.y = 450

# Define plankton
plankton = Actor("plankton_right")
plankton.x = WIDTH//2
plankton.y = HEIGHT * 0.7

pgzrun.go()
