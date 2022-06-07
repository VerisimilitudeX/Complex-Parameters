#### ---- LIBRARIES ---- ####
import random
import tsk
import pygame
pygame.init()

#### -------------------------------- ####
#### ---- REMOVE CLOUDS FUNCTION ---- ####
#### -------------------------------- ####
def remove_clouds(cloud_list):
    old_clouds = []

    for cloud in cloud_list:
        if cloud.y > 400:
            old_clouds.append(cloud)

    for cloud in old_clouds:
        cloud_list.remove(cloud)
    
#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

background = tsk.Sprite("SkyMountains.jpg", 0, 0)
clouds = []

cloud_timer = 1000

drawing = True
while drawing:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    if cloud_timer <= 0:
        new_cloud = tsk.Sprite("Cloud2.png", random.randint(0, 850), -100)
        clouds.append(new_cloud)
        cloud_timer = 1000

    for cloud in clouds:
        cloud.y += .07 * c.get_time()

    remove_clouds(clouds)

    background.draw()
    for cloud in clouds:
        cloud.draw()

    pygame.display.flip()
    c.tick(30)
    cloud_timer -= c.get_time()s
