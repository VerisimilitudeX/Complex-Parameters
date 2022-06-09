"""
LESSON: 6.3 - Complex Parameters
WARMUP 4
"""

#### ---- LIBRARIES ---- ####
import pygame
pygame.init()


#### ---------------------------------- ####
#### ---- FILL BACKGROUND FUNCTION ---- ####
#### ---------------------------------- ####

# Define the function
def fill_background(window, back_color, circle_color=(0, 0, 0)):

    # Fill the background
    window.fill(back_color)

    # Draw a circle
    pygame.draw.circle(window, circle_color, (200, 200), 50)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([400, 400])
w.fill((255, 255, 255))
pygame.display.flip()

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # On click, fill background with black and a
        # white circle
        if event.type == pygame.MOUSEBUTTONDOWN:
            fill_background(w, (0, 0, 0), (255, 255, 255))

        # On key presses, fill background with other
        # color and black circle
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                fill_background(w, (255, 0, 255))

            if event.key == pygame.K_s:
                fill_background(w, (255, 0, 0))

            if event.key == pygame.K_d:
                fill_background(w, (0, 0, 255))

            if event.key == pygame.K_f:
                fill_background(w, (0, 255, 255))

            if event.key == pygame.K_g:
                fill_background(w, (0, 255, 0))

            if event.key == pygame.K_h:
                fill_background(w, (255, 255, 0))

    pygame.display.flip()