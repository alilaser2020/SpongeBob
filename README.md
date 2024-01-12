
# pygame zero

A project written for **Sponge Bob** game with *pygame* library and it's very useful package *'pgzero'* and also their modules (like *pgzrun*)


## Install
Required instructions for installation:

**pip install pygame**

**pip install pgzero**
## Main items
There is a class in actor module of pgzero *(pgzero.actor)* named *'Actor'* for define:

**from pgzero.actor import Actor**

and import image items for game that called *'actors'* im program, For instance:

*bob = Actor("bob_right_prev_ui")**
## main functions
When we used with *pgzero*, there are 2 main functions that very important and efficient:

1. **def draw():**
A function for drawing any actor with any change

2. **def update():**
A function run 60 times per second for check, refresh and update position of actors,
also we need import *pgzrun* package for run these 2 function, actually this module is the backbone of program which acts like a *while True loop*:

**pgzrun.go()**

## debug
According to run *update()* function 60 times per second for updating each actors, As a result, we cannot debug the code in a traditional way, so the only way to debug it is to use the built-in *'print()'* function repeatedly in different places and see the result in the console.
## run program in Pycharm
Use **shift + F10** to run code in *Pycharm*
