import pgzrun
import random

from pgzero import clock
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def plankton_random_direction():
    """
    A method for determine a random direction for plankton (execute by pgzrun.go())
    :return:
    """
    plankton.x_dir = random.randint(-plankton.speed, plankton.speed)
    plankton.y_dir = random.randint(-plankton.speed, plankton.speed)
    if plankton.x_dir > 0:
        plankton.image = "plankton_right"
    else:
        plankton.image = "plankton_left"


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
        bob.x += bob.speed
        bob.image = "bob_right_prev_ui"
    if keyboard.left:
        bob.x -= bob.speed
        bob.image = "bob_left_prev_ui"
    if keyboard.up:
        bob.y -= bob.speed
    if keyboard.down:
        bob.y += bob.speed

    actor_correct_location(bob)

    # Patrick section
    if keyboard.d:
        patrick.x += patrick.speed
        patrick.image = "patric_right_prev_ui"
    if keyboard.a:
        patrick.x -= patrick.speed
        patrick.image = "patric_left_prev_ui"
    if keyboard.w:
        patrick.y -= patrick.speed
    if keyboard.s:
        patrick.y += patrick.speed

    actor_correct_location(patrick)

    # Define Plankton
    plankton.x += plankton.x_dir
    plankton.y += plankton.y_dir
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
bob.speed = 5

# Define patrick
patrick = Actor("patric_left_prev_ui")
patrick.x = 950
patrick.y = 450
patrick.speed = 5

# Define plankton
plankton = Actor("plankton_right")
plankton.speed = 7
plankton_random_direction()
clock.schedule_interval(plankton_random_direction, 4)

pgzrun.go()
