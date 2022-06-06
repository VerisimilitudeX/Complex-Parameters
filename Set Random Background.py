"""
LESSON: 6.3 - Complex Parameters
WARMUP 1
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()

#### --------------------------- ####
#### ---- RANDOM BACKGROUND ---- ####
#### --------------------------- ####
listt = ["AlienSpace.jpg", "Hills.jpg", "SchoolHallway.jpg"]
def random_background():
    back = random.randint(1, 3)
    if back == 1:
        return "AlienSpace.jpg"
    elif back == 2:
        return "Hills.jpg"
    elif back == 3:
        return "SchoolHallway.jpg"

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("Hills.jpg", 0, 0)

# Sprites
panda = tsk.Sprite("Panda.png", 100, 100)
rock = tsk.Sprite("BigMossyRock.png", 400, 20)
vase = tsk.Sprite("ShortVase.png", 670, 280)


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Change and print background image
            back = random_background()
            background.image = back
            print("The new background is " + str(back))

    # Draw
    background.draw()
    rock.draw()
    panda.draw()
    vase.draw()
    pygame.display.flip()
