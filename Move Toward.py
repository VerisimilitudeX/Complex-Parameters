#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### ------------------------------- ####
#### ---- MOVE TOWARDS FUNCTION ---- ####
#### ------------------------------- ####
def move_towards(butterfly, vase, speed):

    x = butterfly.center_x

    if vase.center_x < x - 2:
        butterfly.flip_x = True
        x -= speed
    elif vase.center_x > x + 2:
        butterfly.flip_x = False
        x += speed

    butterfly.center_x = x
    return

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("Grass.jpg", 0, 0)
vase = tsk.Sprite("ShortVase.png", 0, 200)
bug = tsk.Sprite("Butterfly.png", 500, 250)

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            vase.x = random.choice([0, 848])

    move_towards(bug, vase, .1 * c.get_time())

    background.draw()
    vase.draw()
    bug.draw()

    pygame.display.flip()
    c.tick(30)
