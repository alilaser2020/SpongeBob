import pgzrun
from pgzero.actor import Actor


def draw():
    """
    A method for drawing anything with any change (execute by pgzrun.go())
    :return:
    """
    back.draw()


def update():
    """
    A method for updating and refresh anything 60 times per second (execute by pgzrun.go())
    :return:
    """
    ...


WIDTH = 1280
HEIGHT = 720
TITLE = "SpongeBob"

# Define background
back = Actor("back")

pgzrun.go()
