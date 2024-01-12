import sys

import pgzrun
import random

from pgzero import clock
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds


def collide_plankton(actor):
    """
    A method for reset points of every actor (bob and patric) when collide actor with plankton (execute by pgzrun.go())
    :param actor:
    :return:
    """
    if actor.colliderect(plankton):
        sounds.lose.play()
        actor.score = 0
        actor.speed = 5
        random_location(actor)


def reset_pearl():
    """
    A method for reset pearl location (execute by pgzrun.go())
    :return:
    """
    global pearl_flag
    pearl_flag = True


def reset_bob():
    """
    A method for reset attributes of bob (execute by pgzrun.go())
    :return:
    """
    bob.speed = 5


def reset_patric():
    """
    A method for reset attributes of bob (execute by pgzrun.go())
    :return:
    """
    patrick.speed = 5


def update_actor(actor, pearl):
    """
    A method for updating attributes of each actor when collide with specific pearl (execute by pgzrun.go())
    :param actor:
    :param pearl:
    :return:
    """
    global pearl_flag
    if pearl_flag:
        sounds.energetic.play()
        actor.speed = pearl.full_speed
        pearl_flag = False


def collide_pearl(actor, pearl):
    """
    A method for determine each actors (bob or patric) when collide with specific pearl (execute by pgzrun.go())
    :param actor:
    :param pearl:
    :return:
    """
    global pearl_flag
    if pearl_flag:
        if actor.colliderect(pearl) and pearl == speed_pearl and actor == bob:
            update_actor(actor, pearl)
            clock.schedule_unique(reset_bob, 10)
            clock.schedule_unique(reset_pearl, 15)
        if actor.colliderect(pearl) and pearl == speed_pearl and actor == patrick:
            update_actor(actor, pearl)
            clock.schedule_unique(reset_patric, 10)
            clock.schedule_unique(reset_pearl, 15)


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
    global pearl_flag
    back.draw()
    shell.draw()
    if pearl_flag:
        speed_pearl.draw()
    bob.draw()
    patrick.draw()
    plankton.draw()
    ham.draw()
    mode.screen.draw.text("SpongeBob score: " + str(bob.score), (10, 10), fontsize=50, color="yellow", gcolor="red",
                          scolor="black", shadow=(1, 1), alpha=0.9)
    mode.screen.draw.text("Patrick Start score: " + str(patrick.score), (880, 10), fontsize=50, color="yellow", gcolor="red",
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
    collide_pearl(bob, speed_pearl)
    collide_plankton(bob)

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
    collide_pearl(patrick, speed_pearl)
    collide_plankton(patrick)

    # Define Plankton
    plankton.x += plankton.x_dir
    plankton.y += plankton.y_dir
    actor_correct_location(plankton)


WIDTH = 1280
HEIGHT = 720
TITLE = "SpongeBob"
pearl_flag = True
pearl_center = (940, 550)
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

# Define shel
shell = Actor("shell")
shell.center = pearl_center

# Define speed pearl
speed_pearl = Actor("pearl1")
speed_pearl.full_speed = 12
speed_pearl.center = pearl_center

pgzrun.go()
