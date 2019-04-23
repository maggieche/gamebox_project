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

'''
04/22/19
- differentiate levels with different enemies/powers/collectibles 
- thoughts on platforms / idk how long we could make each round without scrolling / maybe just make everything uber small?
- being able to choose your avatar or which basketball team member you want to be (if we keep basketball)
- thoughts on overall final four/march madness theme
  - make the final "door" a hoop
  - after x amount of levels, you win the championship 
  - each level is a different team we beat
  - maybe wouldn't have the ability to choose the level at the beginning
'''

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

background = gamebox.from_image(400, 300, 'https://auburnuniforms.com/wp-content/uploads/2019/03/2019-NCAA'
                                          '-Tournament-Court-round-2-840x469.png')
background.height = 750

# creating characters
kyle = gamebox.from_image(400, 560, 'https://a.espncdn.com/combiner/i?img=/i/headshots/mens-college-basketball/'
                                    'players/full/4065730.png')
kyle.height = 30
kihei = gamebox.from_image(200, 560,
                           'https://a.espncdn.com/i/headshots/mens-college-basketball/players/full/4395677.png')
kihei.height = 30

# creating a game screen full of obstacles

# level 1
# all platforms are 10 pixels tall & 150 pixels apart (height wise)
platforms_level1 = [
    gamebox.from_color(400, 630, 'dark green', 800, 60),  # floor
    gamebox.from_color(400, -30, 'dark green', 800, 60),  # ceiling
    gamebox.from_color(-30, 300, 'dark green', 60, 600),  # left wall
    gamebox.from_color(830, 300, 'dark green', 60, 600),  # right wall

    gamebox.from_color(400, 500, 'dark green', 250, 10),
    gamebox.from_color(650, 400, 'dark green', 200, 10),
    gamebox.from_color(150, 400, 'dark green', 200, 10),
    gamebox.from_color(100, 300, 'dark green', 100, 10),
    gamebox.from_color(300, 300, 'dark green', 100, 10),
    gamebox.from_color(500, 300, 'dark green', 100, 10),
    gamebox.from_color(700, 300, 'dark green', 100, 10),
    gamebox.from_color(450, 200, 'dark green', 250, 10),
    gamebox.from_color(50, 200, 'dark green', 100, 10),
    gamebox.from_color(200, 100, 'dark green', 200, 10),  # winning floor
    gamebox.from_color(700, 100, 'dark green', 50, 10)

]

# function for player 1 motion (to decrease repetition)
def kylemove(keys, platformlevel):
    if pygame.K_LEFT in keys:
        kyle.x -= 7.5
    if pygame.K_RIGHT in keys:
        kyle.x += 7.5
    if pygame.K_UP in keys:
        if platformlevel == 1:
            for platform in platforms_level1:
                if kyle.bottom_touches(platform):
                    kyle.speedy = -15
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
        kihei.x -= 7.5
    if pygame.K_d in keys:
        kihei.x += 7.5
    if pygame.K_w in keys:
        if platformlevel == 1:
            for platform in platforms_level1:
                if kihei.bottom_touches(platform):
                    kihei.speedy = -15
        # elif platformlevel == 2:
        #     for platform in platforms_level2:
        #         if kihei.bottom_touches(platform):
        #             kihei.speedy = -20
        # else:
        #     for platform in platforms_level3:
        #         if kihei.bottom_touches(platform):
        #             kihei.speedy = -20

level = False
# level_1 = gamebox.from_color(200, 400, 'yellow', 60, 60)
# level_2 = gamebox.from_color(400, 400, 'blue', 60, 60)
# level_3 = gamebox.from_color(600, 400, 'pink', 60, 60)


def tick(keys):
    global level, level_1, level_2, level_3

    if not level:
        # create a menu screen with different levels to choose
        camera.clear('white')
        camera.draw(gamebox.from_text(400, 150, "Welcome to our Game! Press 'Space' to Start.", 50, 'black'))
        if pygame.K_SPACE in keys:
            level = 1
        # # level logos-- eventually could be a picture not a color gamebox
        # camera.draw(level_1)
        # camera.draw(level_2)
        # camera.draw(level_3)
        # # click on level logo to start
        # if camera.mouseclick:
        #     if level_1.contains(camera.mouse):
        #         level = 1
        #     if level_2.contains(camera.mouse):
        #         level = 2
        #     if level_3.contains(camera.mouse):
        #         level = 3

    # level 1
    if level == 1:
        camera.clear('white')
        camera.draw(background)

        # kyle movement
        kylemove(keys, 1)
        for platform in platforms_level1:
            kyle.move_to_stop_overlapping(platform)
        kyle.speedy += 0.75
        kyle.move_speed()

        # kihei movement
        kiheimove(keys, 1)
        for platform in platforms_level1:
            kihei.move_to_stop_overlapping(platform)
        kihei.speedy += 0.75
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
