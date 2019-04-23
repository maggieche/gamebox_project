# gamebox_project

'''basic idea: Super Mario Bros meets FireBoy and WaterGirl
-interacting with objects and villains
-shooting, depends on what the player touches
-losing when coming in contact with certain objects and villains
-different levels
-one screen at a time- no scrolling; the player jumps from platform to platform
-the object of the game is to get to a door either at the top or bottom of the screen, depending on where the level starts
-for one player: use left, right, up arrows
-for the other: use A, D, W
-instructions screen has a map of the levels, can select with mouse
Optional features we are including:
*enemies (pace back and forth on a specific platform)
*collectibles (specific to each of the two characters)
*two players simultaneously
*multiple levels
'''

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

# creating characters
kyle = gamebox.from_image(400, 560, 'https://a.espncdn.com/combiner/i?img=/i/headshots/mens-college-basketball/'
                                    'players/full/4065730.png')
kyle.height = 60
kihei = gamebox.from_image(200, 560,
                           'https://a.espncdn.com/i/headshots/mens-college-basketball/players/full/4395677.png')
kihei.height = 60

# creating a game screen full of obstacles

# level 1
# all platforms are 20 pixels tall & 150 pixels apart (height wise)
platforms_level1 = [
    gamebox.from_color(400, 600, 'dark green', 800, 20),  # floor
    gamebox.from_color(400, 0, 'dark green', 800, 20),  # ceiling
    gamebox.from_color(0, 300, 'dark green', 20, 600),  # left wall
    gamebox.from_color(800, 300, 'dark green', 20, 600),  # right wall

    gamebox.from_color(100, 450, 'dark green', 250, 20),
    gamebox.from_color(600, 450, 'dark green', 200, 20),
    gamebox.from_color(750, 300, 'dark green', 100, 20),
    gamebox.from_color(250, 300, 'dark green', 300, 20),
    gamebox.from_color(100, 150, 'dark green', 100, 20),
    gamebox.from_color(550, 150, 'dark green', 200, 20),

]

# function for player 1 motion (to decrease repetition)
def kylemove(keys, platformlevel):
    if pygame.K_LEFT in keys:
        kyle.x -= 10
    if pygame.K_RIGHT in keys:
        kyle.x += 10
    if pygame.K_UP in keys:
        if platformlevel == 1:
            for platform in platforms_level1:
                if kyle.bottom_touches(platform):
                    kyle.speedy = -20
        # elif platformlevel == 2:
        #     for platform in platforms_level2:
        #         if kyle.bottom_touches(platform):
        #             kyle.speedy = -20
        # else:
        #     for platform in platforms_level3:
        #         if kyle.bottom_touches(platform):
        #             kyle.speedy = -20

# function for player 2 motion
def kiheimove(keys, platformlevel):
    if pygame.K_a in keys:
        kihei.x -= 10
    if pygame.K_d in keys:
        kihei.x += 10
    if pygame.K_w in keys:
        if platformlevel == 1:
            for platform in platforms_level1:
                if kihei.bottom_touches(platform):
                    kihei.speedy = -20
        # elif platformlevel == 2:
        #     for platform in platforms_level2:
        #         if kihei.bottom_touches(platform):
        #             kihei.speedy = -20
        # else:
        #     for platform in platforms_level3:
        #         if kihei.bottom_touches(platform):
        #             kihei.speedy = -20

level = False
level_1 = gamebox.from_color(200, 400, 'yellow', 60, 60)
level_2 = gamebox.from_color(400, 400, 'blue', 60, 60)
level_3 = gamebox.from_color(600, 400, 'pink', 60, 60)


def tick(keys):
    global level, level_1, level_2, level_3

    if not level:
        # create a menu screen with different levels to choose
        camera.clear('white')
        camera.draw(gamebox.from_text(400, 150, "Welcome to our Game! Choose Level to Start.", 50, 'black'))
        # level logos-- eventually could be a picture not a color gamebox
        camera.draw(level_1)
        camera.draw(level_2)
        camera.draw(level_3)
        # click on level logo to start
        if camera.mouseclick:
            if level_1.contains(camera.mouse):
                level = 1
            if level_2.contains(camera.mouse):
                level = 2
            if level_3.contains(camera.mouse):
                level = 3

    # level 1
    if level == 1:
        camera.clear('white')

        # kyle movement
        kylemove(keys, 1)
        for platform in platforms_level1:
            kyle.move_to_stop_overlapping(platform)
        kyle.speedy += 1
        kyle.move_speed()

        # kihei movement
        kiheimove(keys, 1)
        for platform in platforms_level1:
            kihei.move_to_stop_overlapping(platform)
        kihei.speedy += 1
        kihei.move_speed()

        # drawing
        for platform in platforms_level1:
            camera.draw(platform)
        camera.draw(kyle)
        camera.draw(kihei)

    if level == 2:
        camera.clear('yellow')
    if level == 3:
        camera.clear('black')

    camera.display()


gamebox.timer_loop(60, tick)
