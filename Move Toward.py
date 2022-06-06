"""
LESSON: 6.3 - Complex Parameters
TECHNIQUE 1: Move Toward
DEMO
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### ------------------------------- ####
#### ---- MOVE TOWARDS FUNCTION ---- ####
#### ------------------------------- ####
def move_towards(butterfly, vase, speed):
    # Get start position
    x = buttefly.center_x

    # Calculate position
    if vase.center_x < x:
        x -= speed
    elif vase.center_x > x:
        x += speed
        
    # Move butterfly

    return


#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("Grass.jpg", 0, 0)
vase = tsk.Sprite("ShortVase.png", 0, 200)
bug = tsk.Sprite("Butterfly.png", 500, 250)

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            vase.x = random.choice([0, 848])

    # Move butterfly
    move_towards(bug, vase, .1 * c.get_time())

    # Draw
    background.draw()
    vase.draw()
    bug.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)