import sys

import pgzrun
import random

from pgzero import clock
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds


def collide_hamburger(actor):
    """
    A method for define actors (bob or patric) with hamburger (execute by pgzrun.go())
    :param actor:
    :return:
    """
    if actor.colliderect(ham):
        sounds.point.play()
        actor.score += ham.point
        random_location(ham)


def random_location(actor):
    """
    A method for determine a random location for each actors in game's page (execute by pgzrun.go())
    :param actor:
    :return:
    """
    actor.x = random.randint(actor.width // 2, WIDTH - actor.width // 2)
    actor.y = random.randint(actor.height // 2, HEIGHT - actor.height // 2)


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
    ham.draw()
    mode.screen.draw.text("SpongeBob score: " + str(bob.score), (10, 10), fontsize=50, color="yellow", gcolor="red",
                          scolor="black", shadow=(1, 1), alpha=0.9)
    mode.screen.draw.text("Patrick Star score: " + str(patrick.score), (880, 10), fontsize=50, color="yellow", gcolor="red",
                          scolor="black", shadow=(1, 1), alpha=0.9)


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
    collide_hamburger(bob)

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
    collide_hamburger(patrick)

    # Define Plankton
    plankton.x += plankton.x_dir
    plankton.y += plankton.y_dir
    actor_correct_location(plankton)


WIDTH = 1280
HEIGHT = 720
TITLE = "SpongeBob"
mode = sys.modules["__main__"]

# Define background
back = Actor("back")

# Define bob
bob = Actor("bob_right_prev_ui")
random_location(bob)
bob.speed = 5
bob.score = 0

# Define patrick
patrick = Actor("patric_left_prev_ui")
random_location(patrick)
patrick.speed = 5
patrick.score = 0

# Define plankton
plankton = Actor("plankton_right")
plankton.speed = 7
random_location(plankton)
plankton_random_direction()
clock.schedule_interval(plankton_random_direction, 4)

# Define hamburger
ham = Actor("ham1_prev_ui")
random_location(ham)
ham.point = 10

pgzrun.go()
