#### ---- LIBRARIES ---- ####
import random
import pygame
pygame.init()

#### ------------------------------- ####
#### ---- DRAW CIRCLES FUNCTION ---- ####
#### ------------------------------- ####
def random_circle(window, color = (255, 255, 255)):
    random_x = random.randint(0, 1018)
    random_y = random.randint(0, 573)
    random_size = random.randint(15, 40)

    pygame.draw.circle(window, (0, 0, 0), (random_x, random_y), random_size + 5)
    pygame.draw.circle(window, color, (random_x, random_y), random_size)

#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
w.fill((0, 0, 0))
c = pygame.time.Clock()
timer = 1000

#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            random_circle(w, (0, 0, 255))

    if timer <= 0:
        random_circle(w)
        timer = 1000

    timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)
