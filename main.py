import pgzrun
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def actor_correct_location(actor):
    """
    A method for determine correction location for actors in game's page (execute by pgzrun.go())
    :param actor:
    :return:
    """
    if actor.x < -actor.width // 2:
        actor.x = WIDTH + actor.width // 2
    if actor.x > WIDTH + actor.width // 2:
        actor.x = -actor.width // 2
    if actor.y < -actor.height // 2:
        actor.y = HEIGHT + actor.height // 2
    if actor.y > HEIGHT + actor.height // 2:
        actor.y = -actor.height // 2


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
        bob.x += 5
    if keyboard.left:
        bob.x -= 5
    if keyboard.up:
        bob.y -= 5
    if keyboard.down:
        bob.y += 5

    actor_correct_location(bob)

    # Patrick section
    if keyboard.d:
        patrick.x += 5
    if keyboard.a:
        patrick.x -= 5
    if keyboard.w:
        patrick.y -= 5
    if keyboard.s:
        patrick.y += 5

    actor_correct_location(patrick)

    # Define Plankton
    actor_correct_location(plankton)


WIDTH = 1280
HEIGHT = 720
TITLE = "SpongeBob"

# Define background
back = Actor("back")

# Define bob
bob = Actor("bob_right_prev_ui")
bob.x = 300
bob.y = 550

# Define patrick
patrick = Actor("patric_left_prev_ui")
patrick.x = 950
patrick.y = 450

# Define plankton
plankton = Actor("plankton_right")
plankton.x = WIDTH // 2
plankton.y = HEIGHT * 0.7

pgzrun.go()
