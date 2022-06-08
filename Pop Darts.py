#### ---- LIBRARIES ---- ####
import tsk
import random
import pygame
pygame.init()

#### ----------------------- ####
#### ---- SPAWN BALLOON ---- ####
#### ----------------------- ####

# Create a spawn function that takes two lists, one of
# sprites and one of strings for the travel direction
def spawn(spritelist, traveldirectionlist):

    # Pick a random x and y and spawn a balloon sprite
    # at that location with BalloonAngry.png
    tsk.Sprite("BalloonAngry", random.randint(0, 1018), random.randint(0, 573))

    # Add the balloon to the list of sprites and add
    # "r" or "l" to the directions list based on
    # whether the balloon is traveling right (started
    # on the left side) or left (started on the right)
    # ---> TEST AFTER THIS LINE <--- #
    






#### ----------------------- ####
#### ---- MOVE BALLOONS ---- ####
#### ----------------------- ####

# Create a move function that takes two lists, one of
# sprites and one of strings, and a speed number


    # Go through the sprite list by index and get the
    # current balloon



        # If the direction at the matching index is "r",
        # move the balloon right
        # ---> TEST AFTER THIS LINE <--- #



            # If the balloon hits the right edge of the
            # window, change the entry in the directions
            # list to "l"
            # ---> TEST AFTER THIS LINE <--- #



        # Otherwise, move the balloon left
        # ---> TEST AFTER THIS LINE <--- #



            # If the balloon hits the left edge of the
            # window, change the entry in the directions
            # list to "r"
            # ---> TEST AFTER THIS LINE <--- #




#### -------------------------- ####
#### ---- DESTROY BALLOONS ---- ####
#### -------------------------- ####

# Create a destroy function that takes a list of
# balloon sprites and the dart sprite


    # Create an empty list for marked sprites


    # Go through the list of sprites and append them
    # to the list of marked sprites if they collide
    # with the dart




    # Go through the list of marked sprites and remove
    # each of them from the original parameter list



    # Return the length of the list of marked sprites
    # ---> TEST AFTER THIS LINE <--- #



#### ---------------------- ####
#### ---- MAIN PROGRAM ---- ####
#### ---------------------- ####
# --- Setup --- #
w = pygame.display.set_mode([1018, 573])
c = pygame.time.Clock()

# --- Sprites --- #
background = tsk.Sprite("FairBooth.jpg", 0, 0)
dart = tsk.Sprite("Dart.png", 500, 450)
balloons = []
move_direction = []

# --- Variables --- #
balloon_timer = 2000
game_timer = 20000
num_balloons = 0
popped = 0
darts = 0
flying = False


#### ---- MAIN LOOP ---- ####
drawing = True
while drawing:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            flying = False

        elif event.type == pygame.MOUSEBUTTONUP:
            flying = True
            darts += 1

    # --- Dart follows mouse or flies forward --- #
    if not flying:
        x, y = pygame.mouse.get_pos()
        dart.center_x = x
        dart.center_y = 450

    else:
        dart.center_y -= .6 * c.get_time()

    # --- Dart resets if it gets too far --- #
    if dart.y < 0:
        flying = False

    # --- Balloons spawn every 2 seconds (up to 9) --- #

    # If time has run out (balloon_timer) and there are
    # fewer than 10 balloons on screen (num_balloons),
    # call the function to spawn a new balloon



        # Increment the number of balloons onscreen
        # and re-set the timer
        # ---> TEST AFTER THIS LINE <--- #




    # --- Move balloon --- #

    # Calculate a speed for the balloons with
    # c.get_time() and call the function to move them




    # --- Pop balloons --- #

    # Call the function that destroys balloons, then
    # decrease the number of balloons on screen and
    # increase the score (popped) by the number of
    # balloons that the function says were popped
    # ---> TEST AFTER THIS LINE <--- #





    #### ---- DRAW ---- ####

    # --- Draw scene --- #
    background.draw()
    for sprite in balloons:
        sprite.draw()
    dart.draw()

    # --- Finish --- #
    balloon_timer -= c.get_time()
    game_timer -= c.get_time()
    pygame.display.flip()
    c.tick(30)

    if game_timer <= 0:
        drawing = False


#### ---- FINAL OUTPUT ---- ####
print("You popped " + str(popped) + " balloons")
print("You used " + str(darts) + " darts")



# Turn in your Coding Exercise.
