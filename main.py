import sys
import pgzrun
import random
import pygame.display

from pgzero import clock
from ctypes import windll
from pgzero.actor import Actor
from pgzero.keyboard import keyboard
from pgzero.loaders import sounds


def resat_all():
    """
    A method for reset anything when redirect from play page (execute by pgzrun.go())
    :return:
    """
    global pearl_flag
    pearl_flag = True
    bob.score = patrick.score = 0
    bob.speed = patrick.speed = 5
    bob.power = bob.collide_pearl_flag = bob.collide_snail_flag = False
    patrick.power = patrick.collide_pearl_flag = patrick.collide_snail_flag = False
    random_location(bob)
    random_location(patrick)
    random_location(plankton)
    random_location_snail()
    reset_pearl()


def collide_snail(actor):
    """
    A method for when each actor collide with snail, it's speed will be slow (execute by pgzrun.go())
    :param actor:
    :return:
    """
    global pearl_flag
    if snail.colliderect(actor) and actor.power:
        sounds.jump.play()
        random_location_snail()
    if snail.colliderect(actor) and not actor.power:
        sounds.snail.play()
        actor.speed = snail.speed
        actor.collide_snail_flag = True
        clock.schedule_unique(reset_actor, 5)


def random_location_snail():
    """
    A method for determine a correct random location for snail (execute by pgzrun.go())
    :return:
    """
    snail.x = random.randint(snail.width // 2, WIDTH - snail.width // 2)
    snail.y = random.randint(HEIGHT // 2, HEIGHT - snail.height // 2)


def collide_plankton(actor):
    """
    A method for reset points of every actor (bob and patric) when collide actor with plankton (execute by pgzrun.go())
    :param actor:
    :return:
    """
    if actor.colliderect(plankton) and actor.power:
        sounds.jump.play()
        random_location(plankton)
    elif actor.colliderect(plankton) and not actor.power:
        sounds.lose.play()
        actor.score = 0
        actor.speed = 5
        random_location(actor)


def reset_pearl():
    """
    A method for reset pearl location (execute by pgzrun.go())
    :return:
    """
    global pearl_list, pearl_flag
    pearl_flag = True
    if random.randint(0, 100) >= 20:
        pearl.image = pearl_list[0]
    else:
        pearl.image = pearl_list[1]


def reset_actor():
    """
    A method for reset attributes of bob (execute by pgzrun.go())
    :return:
    """
    if bob.collide_pearl_flag:
        bob.speed = 5
        bob.power = bob.collide_pearl_flag = False
    if patrick.collide_pearl_flag:
        patrick.speed = 5
        patrick.power = patrick.collide_pearl_flag = False
    if bob.collide_snail_flag:
        bob.speed = 5
        bob.collide_snail_flag = False
    if patrick.collide_snail_flag:
        patrick.speed = 5
        patrick.collide_snail_flag = False


def collide_pearl(actor, pearl):
    """
    A method for determine each actors (bob or patric) when collide with specific pearl (execute by pgzrun.go())
    :param actor:
    :param pearl:
    :return:
    """
    global pearl_flag
    if actor.colliderect(pearl) and pearl_flag:
        pearl_flag = False
        actor.speed = pearl.full_speed
        actor.collide_pearl_flag = True
        if pearl.image == "pearl2":
            sounds.power.play()
            actor.power = True
        else:
            sounds.energetic.play()
        clock.schedule_unique(reset_actor, 10)
        clock.schedule_unique(reset_pearl, 15)


def collide_hamburger(actor):
    """
    A method for define actors (bob or patric) with hamburger (execute by pgzrun.go())
    :param actor:
    :return:
    """
    global status
    if actor.colliderect(ham):
        sounds.point.play()
        actor.score += ham.point
        random_location(ham)
        if actor == bob and actor.score >= 50:
            status = "bob_win"
        if actor == patrick and actor.score >= 50:
            status = "patric_win"


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


def quit_func():
    """
    A method for existing from game after 4 seconds delay (execute by pgzrun.go())
    :return:
    """
    quit()


def on_key_down():
    """
    A method for occurrence en event when press down a specific key on keyboard (execute by pgzrun.go())
    :return:
    """
    global status, pearl_list
    if keyboard.space and status == "home":
        status = "play"
        clock.schedule_interval(plankton_random_direction, 4)
    if keyboard.h and status != "home":
        status = "home"
        resat_all()
    if keyboard.p and status != "play":
        status = "play"
        resat_all()
    if keyboard.f:
        mode.screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    if keyboard.n:
        mode.screen.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    if keyboard.escape:
        status = "end"
        clock.schedule(quit_func, 4)
    if keyboard.c and status != "end":
        quit()


def draw():
    """
    A method for drawing anything with any change (execute by pgzrun.go())
    :return:
    """
    global pearl_flag
    if status == "home":
        mode.screen.blit("home", (0, 0))
        box1 = pygame.Rect((0, 0), (600, 70))
        box1.center = (WIDTH//2, HEIGHT * 0.88)
        mode.screen.draw.filled_rect(box1, (255, 255, 0))
        mode.screen.draw.text("Press space for play", center=(WIDTH//2, HEIGHT * 0.88), fontsize=60, color="blue",
                              scolor="black", shadow=(1, 1))
        box2 = pygame.Rect((0, 0), (600, 55))
        box2.center = (WIDTH//2, HEIGHT * 0.963)
        mode.screen.draw.filled_rect(box2, (0, 255, 0))
        mode.screen.draw.text("f: full screen, n: normal, h: home,\np: play, Esc, c: exit", center=(WIDTH//2, HEIGHT * 0.963), fontsize=40, color="black")
    elif status == "play":
        back.draw()
        snail.draw()
        shell.draw()
        if pearl_flag:
            pearl.draw()
        bob.draw()
        patrick.draw()
        plankton.draw()
        ham.draw()
        mode.screen.draw.text("SpongeBob score: " + str(bob.score), (10, 10), fontsize=50, color="yellow", gcolor="red",
                              scolor="black", shadow=(1, 1), alpha=0.9)
        mode.screen.draw.text("Patrick Star score: " + str(patrick.score), (880, 10), fontsize=50, color="yellow",
                              gcolor="red", scolor="black", shadow=(1, 1), alpha=0.9)
    elif status == "bob_win":
        mode.screen.blit("bob_win", (0, 0))
        mode.screen.draw.text("SpongeBob score: " + str(bob.score), (10, 10), fontsize=60, color="red", gcolor="blue"
                              , scolor="green", shadow=(2, 2), alpha=0.9)
        mode.screen.draw.text("Patrick Star score: " + str(patrick.score), (880, 10), fontsize=50, color="red", gcolor="blue"
                              , scolor="black", shadow=(1, 1), alpha=0.9)
    elif status == "patric_win":
        mode.screen.blit("patric_win", (0, 0))
        mode.screen.draw.text("SpongeBob score: " + str(bob.score), (10, 10), fontsize=50, color="red", gcolor="blue"
                              , scolor="black", shadow=(1, 1), alpha=0.9)
        mode.screen.draw.text("Patrick Star score: " + str(patrick.score), (790, 10), fontsize=60, color="red", gcolor="blue"
                              , scolor="green", shadow=(2, 2), alpha=0.9)
    elif status == "end":
        mode.screen.blit("end", (0, 0))


def update():
    """
    A method for updating and refresh anything 60 times per second (execute by pgzrun.go())
    :return:
    """
    # Bob section
    if status == "play":
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
        collide_pearl(bob, pearl)
        collide_plankton(bob)
        collide_snail(bob)

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
        collide_pearl(patrick, pearl)
        collide_plankton(patrick)
        collide_snail(patrick)

        # Define Plankton
        plankton.x += plankton.x_dir
        plankton.y += plankton.y_dir
        actor_correct_location(plankton)

        # Define snail
        if snail.image == "snail_right":
            snail.x += snail.speed
            if snail.x >= WIDTH - snail.width // 2:
                snail.image = "snail_left"
                # random_location_snail()
        if snail.image == "snail_left":
            snail.x -= snail.speed
            if snail.x <= snail.width // 2:
                snail.image = "snail_right"
                # random_location_snail()


WIDTH = 1280
HEIGHT = 720
status = "home"
TITLE = "SpongeBob"
pearl_flag = True
pearl_center = (940, 550)
mode = sys.modules["__main__"]

# Define background
hwnd = pygame.display.get_wm_info()["window"]
windll.user32.MoveWindow(hwnd, 310, 150, WIDTH, HEIGHT, False)
back = Actor("back")

# Define bob
bob = Actor("bob_right_prev_ui")
random_location(bob)
bob.speed = 5
bob.score = 0
bob.power = bob.collide_pearl_flag = bob.collide_snail_flag = False

# Define patric
patrick = Actor("patric_left_prev_ui")
random_location(patrick)
patrick.speed = 5
patrick.score = 0
patrick.power = patrick.collide_pearl_flag = patrick.collide_snail_flag = False

# Define plankton
plankton = Actor("plankton_right")
plankton.speed = 7
random_location(plankton)
plankton_random_direction()

# Define hamburger
ham = Actor("ham1_prev_ui")
random_location(ham)
ham.point = 10

# Define shel
shell = Actor("shell")
shell.center = pearl_center

# Define pearls
pearl_list = ["pearl1", "pearl2"]
if random.randint(0, 100) >= 20:
    random_pearl = pearl_list[0]
else:
    random_pearl = pearl_list[1]
pearl = Actor(random_pearl)
pearl.full_speed = 12
pearl.center = pearl_center

# Define snail
snail_directions = ["snail_right", "snail_left"]
rand_snail_dir = random.choice(snail_directions)
snail = Actor(rand_snail_dir)
random_location_snail()
snail.image = rand_snail_dir
snail.speed = 1

pgzrun.go()
