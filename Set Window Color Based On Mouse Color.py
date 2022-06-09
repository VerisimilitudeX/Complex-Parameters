#### ---- LIBRARIES ---- ####
import pygame
pygame.init()

#### ---------------------------------- ####
#### ---- FILL BACKGROUND FUNCTION ---- ####
#### ---------------------------------- ####
def fill_background(window, back_color, circle_color=(0, 0, 0)):
    window.fill(back_color)
    pygame.draw.circle(window, circle_color, (200, 200), 50)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([400, 400])
w.fill((255, 255, 255))
pygame.display.flip()

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            fill_background(w, (0, 0, 0), (255, 255, 255))

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
