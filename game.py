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

camera = gamebox.Camera(800,600)
#creating characters
player_1 = gamebox.from_color(400,300,'red',30,30)
player_2 = gamebox.from_color(450,300,'green',30,30)

#creating a game screen full of obstacles
platforms = [
    gamebox.from_color(450,350,'gray',200,40)
]

level = False
level_1 = gamebox.from_color(200,400,'yellow',60,60)
level_2 = gamebox.from_color(400,400,'blue',60,60)
level_3 = gamebox.from_color(600,400,'pink',60,60)

def tick(keys):
    global level, level_1, level_2,level_3

    if not level:
        #create a menu screen with different levels to choose
        camera.clear('white')
        camera.draw(gamebox.from_text(400,150,"Welcome to our Game! Choose Level to Start.",50,'black'))
        #level logos-- eventually could be a picture not a color gamebox
        camera.draw(level_1)
        camera.draw(level_2)
        camera.draw(level_3)
        #click on level logo to start
        if camera.mouseclick:
            if level_1.contains(camera.mouse):
                level = 1
            if level_2.contains(camera.mouse):
                level = 2
            if level_3.contains(camera.mouse):
                level = 3
    if level == 1:
        camera.clear('white')
    if level == 2:
        camera.clear('yellow')
    if level == 3:
        camera.clear('black')
    camera.display()

gamebox.timer_loop(60, tick)
