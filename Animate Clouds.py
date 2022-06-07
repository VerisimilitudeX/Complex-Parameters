"""
LESSON: 6.3 - Complex Parameters
WARMUP 2
"""

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

    # Mark clouds for removal
    for cloud in cloud_list:
        if cloud.y > 400:
            old_clouds.append(cloud)

    # Remove clouds from cloud_list
    for cloud in old_clouds:
        cloud_list.remove(cloud)
    
#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# Setup
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# Sprites
background = tsk.Sprite("SkyMountains.jpg", 0, 0)
clouds = []

cloud_timer = 1000


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # Make new clouds
    if cloud_timer <= 0:
        new_cloud = tsk.Sprite("Cloud2.png", random.randint(0, 850), -100)
        clouds.append(new_cloud)
        cloud_timer = 1000

    # Move clouds
    for cloud in clouds:
        cloud.y += .07 * c.get_time()

    # Remove old clouds
    remove_clouds(clouds)

    # Draw
    background.draw()
    for cloud in clouds:
        cloud.draw()

    # Finish
    pygame.display.flip()
    c.tick(30)
    cloud_timer -= c.get_time()s