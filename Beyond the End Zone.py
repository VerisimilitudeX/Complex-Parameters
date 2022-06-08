"""
LESSON: 5.4 - Sprites in Lists
EXERCISE: Beyond the End Zone
"""
import pygame
import random
import tsk
pygame.init()
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()
time= 0
l = ["Bush.png", "Flower.png", "FootballBlocker.png", "Mole.png", "Rabbit.png"]
hedgehog = tsk.Sprite("FootballRunner.png", 100, 300)
background = tsk.Sprite("ForestScrolling.jpg", 0, 0)
sprites = []
while True:
    time+= c.get_time()
    if time>= 2500:
        time= 0
        sprite = tsk.Sprite(l[random.randint(0, len(l) - 1)], 1018, 0)
        sprite.center_y = hedgehog.y + hedgehog.height
        sprites.append(sprite)
    for i in sprites:
        i.x -= 0.2*c.get_time()
        if i.x < (0 - i.width):
            sprites.remove(i)
    background.x -= 0.2*c.get_time()
    if background.x <= -1018:
        background.x = 0
    background.draw()
    hedgehog.draw()
    for i in sprites:
        i.draw()
    pygame.display.flip()
    c.tick(30)