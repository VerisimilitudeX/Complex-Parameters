"""
LESSON: 6.3 - Complex Parameters
WARMUP 3
"""

#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()


#### ------------------------------- ####
#### ---- MOVE SPRITES FUNCTION ---- ####
#### ------------------------------- ####
def move_sprites(sprite_list, old_mouse, new_mouse):

    # Get position of clicks
    old_x, old_y = old_mouse
    x, y = new_mouse

    # Get the difference between new and old positions
    x_diff = x - old_x
    y_diff = y - old_y

    # Move each sprite based on the difference
    for sprite in sprite_list:
        sprite.center_x += x_diff
        sprite.center_y += y_diff

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("CatRoom.jpg", 0, 0)
box = tsk.Sprite("CatBox.png", 0, 0)
box.center = (0, 0)
cats = []

# Left cats
for i in range(5):
    cat = tsk.Sprite("BoredCat.png", random.randint(-500, -300), random.randint(-200, 50))
    cats.append(cat)

# Right cats
for i in range(5):
    cat = tsk.Sprite("BoredCat.png", random.randint(50, 300), random.randint(-200, 50))
    cat.flip_x = True
    cats.append(cat)


# Click variables
old_click = (0, 0)
click = (0, 0)


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # Move cats on click
        if event.type == pygame.MOUSEBUTTONDOWN:
            old_click = click
            click = pygame.mouse.get_pos()
            box.center = click
            move_sprites(cats, old_click, click)

    # Draw
    background.draw()
    box.draw()
    for cat in cats:
        cat.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)