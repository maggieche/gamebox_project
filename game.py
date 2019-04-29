# Cathryn Palmer cep7pa
# Maggie Che mc8ew

'''
- UVA March Madness 2019 meets Fireboy and Watergirl
- levels
- collectibles
- timer
- enemies
- objective: both players must reach the hoop at the top, while collecting as many basketballs as possible
- player 1 (left) uses A, W, and D to move
- player 2 (right) uses the left, up, and right arrows to move
'''

import pygame
import gamebox

camera = gamebox.Camera(800, 600)

# starting background
starting_screen = gamebox.from_image(400, 300, 'https://s3media.247sports.com/Uploads/Assets/96/822/8822096.jpg')
starting_screen.height = 600

# level backgrounds
background = gamebox.from_image(400, 300, 'https://auburnuniforms.com/wp-content/uploads/2019/03/2019-NCAA'
                                          '-Tournament-Court-round-2-840x469.png')
background.height = 750

# finishing hoop
hoop_url = 'https://cdn11.bigcommerce.com/s-847qwk2ikf/images/stencil/1280x1280/products/135/645/' \
       'Black_High_Res_Master768__80118.1476101510.png'
hoop_1 = gamebox.from_image(200, 50, hoop_url)
hoop_1.scale_by(0.1)
hoop_2 = gamebox.from_image(25, 50, hoop_url)
hoop_2.scale_by(0.1)
hoop_3 = gamebox.from_image(400, 50, hoop_url)
hoop_3.scale_by(0.1)

# keeping score based on collecting items
score = 0

# creating characters
kyle = gamebox.from_image(400, 560, 'https://a.espncdn.com/combiner/i?img=/i/headshots/mens-college-basketball/'
                                    'players/full/4065730.png')
kyle.height = 50
kihei = gamebox.from_image(200, 560,
                           'https://a.espncdn.com/i/headshots/mens-college-basketball/players/full/4395677.png')
kihei.height = 50

# creating coins to collect, where "coins" refers to basketballs
coinurl = 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Basketball_Clipart.svg/1035px-Basketball_' \
          'Clipart.svg.png'

coins_level1 = [
    gamebox.from_image(350, 470, coinurl),
    gamebox.from_image(400, 470, coinurl),
    gamebox.from_image(450, 470, coinurl),
    gamebox.from_image(600, 370, coinurl),
    gamebox.from_image(650, 370, coinurl),
    gamebox.from_image(700, 370, coinurl),
    gamebox.from_image(100, 270, coinurl),
    gamebox.from_image(700, 270, coinurl),
    gamebox.from_image(500, 270, coinurl),
    gamebox.from_image(50, 170, coinurl),
    gamebox.from_image(150, 370, coinurl),
    gamebox.from_image(100, 370, coinurl),
    gamebox.from_image(200, 370, coinurl),
    gamebox.from_image(700, 70, coinurl),
    gamebox.from_image(700, 45, coinurl),
]
for coin in coins_level1:
    coin.scale_by(0.02)

coins_level2 = [
    gamebox.from_image(350, 370, coinurl),
    gamebox.from_image(400, 370, coinurl),
    gamebox.from_image(450, 370, coinurl),
    gamebox.from_image(350, 170, coinurl),
    gamebox.from_image(400, 170, coinurl),
    gamebox.from_image(450, 170, coinurl)
]
for coin in coins_level2:
    coin.scale_by(0.02)

coins_level3 = [
    gamebox.from_image(350, 370, coinurl),
    gamebox.from_image(400, 370, coinurl),
    gamebox.from_image(450, 370, coinurl),
    gamebox.from_image(100, 470, coinurl),
    gamebox.from_image(700, 470, coinurl),
    gamebox.from_image(350, 270, coinurl),
    gamebox.from_image(400, 270, coinurl),
    gamebox.from_image(450, 270, coinurl),
    gamebox.from_image(450, 70, coinurl),
    gamebox.from_image(350, 70, coinurl)
]
for coin in coins_level3:
    coin.scale_by(0.02)

# creating villains
purdue = 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Purdue_Boilermakers_logo.svg/' \
         '1280px-Purdue_Boilermakers_logo.svg.png'
villains_1 = [
    gamebox.from_image(250, 150, purdue),
    gamebox.from_image(400, 250, purdue),
    gamebox.from_image(650, 350, purdue),
    gamebox.from_image(50, 450, purdue)
]
for villain in villains_1:
    villain.scale_by(0.05)

auburn = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Auburn_Tigers_logo.svg/' \
         '1200px-Auburn_Tigers_logo.svg.png'
villains_2 = [
    gamebox.from_image(250, 150, auburn),
    gamebox.from_image(400, 250, auburn),
    gamebox.from_image(650, 350, auburn),
    gamebox.from_image(50, 450, auburn)
]
for villain in villains_2:
    villain.scale_by(0.05)

texas_tech = 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Texas_Tech_Athletics_logo.svg' \
             '/1200px-Texas_Tech_Athletics_logo.svg.png'
villains_3 = [
    gamebox.from_image(250, 150, texas_tech),
    gamebox.from_image(400, 250, texas_tech),
    gamebox.from_image(650, 350, texas_tech),
    gamebox.from_image(50, 450, texas_tech)
]
for villain in villains_3:
    villain.scale_by(0.05)

# shot clock
time = 30

# all platforms are 10 pixels tall & 100 pixels apart (height wise)
# level 1
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

# level 2
platforms_level2 = [
    gamebox.from_color(400, 630, 'dark green', 800, 60),  # floor
    gamebox.from_color(400, -30, 'dark green', 800, 60),  # ceiling
    gamebox.from_color(-30, 300, 'dark green', 60, 600),  # left wall
    gamebox.from_color(830, 300, 'dark green', 60, 600),  # right wall
    gamebox.from_color(50, 500, 'dark green', 100, 10),
    gamebox.from_color(750, 500, 'dark green', 100, 10),
    gamebox.from_color(400, 400, 'dark green', 300, 10),
    gamebox.from_color(50, 300, 'dark green', 100, 10),
    gamebox.from_color(750, 300, 'dark green', 100, 10),
    gamebox.from_color(400, 200, 'dark green', 300, 10),
    gamebox.from_color(50, 100, 'dark green', 100, 10),  # winning floor
    gamebox.from_color(750, 100, 'dark green', 100, 10)
]

# level 3
platforms_level3 = [
    gamebox.from_color(400, 630, 'dark green', 800, 60),  # floor
    gamebox.from_color(400, -30, 'dark green', 800, 60),  # ceiling
    gamebox.from_color(-30, 300, 'dark green', 60, 600),  # left wall
    gamebox.from_color(830, 300, 'dark green', 60, 600),  # right wall

    gamebox.from_color(400, 400, 'dark green', 250, 10),
    gamebox.from_color(100, 500, 'dark green', 100, 10),
    gamebox.from_color(700, 500, 'dark green', 100, 10),
    gamebox.from_color(400, 300, 'dark green', 150, 10),
    gamebox.from_color(50, 200, 'dark green', 100, 10),
    gamebox.from_color(750, 200, 'dark green', 100, 10),
    gamebox.from_color(400, 100, 'dark green', 200, 10)  # winning floor
]


'''This function controls player 1's movements'''
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
        elif platformlevel == 2:
            for platform in platforms_level2:
                if kyle.bottom_touches(platform):
                    kyle.speedy = -15
        else:
            for platform in platforms_level3:
                if kyle.bottom_touches(platform):
                    kyle.speedy = -15


'''This function controls player 2's movements'''
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
        elif platformlevel == 2:
            for platform in platforms_level2:
                if kihei.bottom_touches(platform):
                    kihei.speedy = -15
        else:
            for platform in platforms_level3:
                if kihei.bottom_touches(platform):
                    kihei.speedy = -15


level = False


'''This function controls the game play and draws the screen each time it's iterated, which is controlled in a separate
loop'''
def tick(keys):
    global level, score, time

    if not level:
        # create a menu screen with different levels to choose
        camera.clear('white')
        camera.draw(starting_screen)
        camera.draw(gamebox.from_text(400, 310, "REDEMPTION TOUR", 50, 'orange'))
        camera.draw(gamebox.from_text(400, 350, "Cathryn Palmer cep7pa & Maggie Che mc8ew", 30, 'orange'))
        camera.draw(gamebox.from_text(400, 390, "How to play:", 50, 'orange'))
        camera.draw(gamebox.from_text(400, 440, "The goal of the game is to reach the basketball net together", 30,
                                      'orange'))
        camera.draw(gamebox.from_text(400, 480, "before the shot clock runs out, collecting as many basketballs as "
                                                "possible.", 30, 'orange'))
        camera.draw(gamebox.from_text(400, 520, "Beware the opposing team members.", 30, 'orange'))
        camera.draw(gamebox.from_text(400, 570, "Press Space to start.", 30, 'orange'))

        if pygame.K_SPACE in keys:
            level = 1

    # level 1
    if level == 1:
        camera.clear('white')
        camera.draw(background)
        camera.draw(hoop_1)

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

        # collecting
        for coin in coins_level1:
            if kyle.touches(coin) or kihei.touches(coin):
                score += 10
                coins_level1.remove(coin)
        # display score
        camera.draw(gamebox.from_text(730, 50, 'Score: '+str(score)+'', 40, 'black'))

        # finish level
        if kyle.touches(hoop_1) and kihei.touches(hoop_1):
            level = 1.5

        # drawing
        for platform in platforms_level1:
            camera.draw(platform)
        for coin in coins_level1:
            camera.draw(coin)
        for villain in villains_1:
            camera.draw(villain)

        camera.draw(kyle)
        camera.draw(kihei)

        # timer
        time -= 0.0167
        camera.draw(gamebox.from_text(100, 50, 'Shot Clock: '+str(int(time))+'', 40, 'black'))
        if int(time) == 0:
            gamebox.pause()
            camera.draw(gamebox.from_text(400, 300, 'You lost to Purdue!', 60, 'red', True))
            camera.draw(gamebox.from_text(400, 350, 'Final Score was: ' + str(score) + '', 60, 'red'))

        # villain movement
        for villain in villains_1:
            villain.speedx = 2.5
            villain.move_speed()
            if villain.left_touches(platforms_level1[3]):
                villain.x = 0
            if kyle.touches(villain) or kihei.touches(villain):
                gamebox.pause()
                camera.draw(gamebox.from_text(400, 300, 'You lost to Purdue!', 60, 'red', True))
                camera.draw(gamebox.from_text(400, 350, 'Final Score was: '+str(score)+'', 60, 'red'))

    if level == 1.5:
        eliteeight = gamebox.from_image(400, 300, 'http://drive.google.com/uc?export=view&id=1wqwgGquyF-IYOSjDWMYQAXJU2PM1ymQD')
        eliteeight.height = 600
        camera.clear('white')
        camera.draw(eliteeight)
        camera.draw(gamebox.from_text(400, 100, 'You\'re moving on to the Final Four!', 40, 'white'))
        camera.draw(gamebox.from_text(400, 150, 'Total Score is: '+str(score)+'', 40, 'white'))
        camera.draw(gamebox.from_text(400, 200, 'Press Space to Continue to Level 2', 40, 'white'))
        if pygame.K_SPACE in keys:
            level = 2
            kyle.x = 400
            kyle.y = 560
            kihei.x = 200
            kihei.y = 560
            time = 30

    # level 2
    if level == 2:
        camera.clear('white')
        camera.draw(background)
        camera.draw(hoop_2)

        # kyle movement
        kylemove(keys, 2)
        for platform in platforms_level2:
            kyle.move_to_stop_overlapping(platform)
        kyle.speedy += 0.75
        kyle.move_speed()

        # kihei movement
        kiheimove(keys, 2)
        for platform in platforms_level2:
            kihei.move_to_stop_overlapping(platform)
        kihei.speedy += 0.75
        kihei.move_speed()

        # collecting
        for coin in coins_level2:
            if kyle.touches(coin) or kihei.touches(coin):
                score += 10
                coins_level2.remove(coin)

        # display score
        camera.draw(gamebox.from_text(730, 50, 'Score: ' + str(score) + '', 40, 'black'))

        # finish level
        if kyle.touches(hoop_2) and kihei.touches(hoop_2):
            level = 2.5

        # drawing
        for platform in platforms_level2:
            camera.draw(platform)
        for coin in coins_level2:
            camera.draw(coin)
        for villain in villains_2:
            camera.draw(villain)
        camera.draw(kyle)
        camera.draw(kihei)

        # timer
        time -= 0.0167
        camera.draw(gamebox.from_text(100, 50, 'Shot Clock: ' + str(int(time)) + '', 40, 'black'))
        if int(time) == 0:
            gamebox.pause()
            camera.draw(gamebox.from_text(400, 300, 'You lost to Auburn!', 60, 'red', True))
            camera.draw(gamebox.from_text(400, 350, 'Final Score was: ' + str(score) + '', 60, 'red'))

        # villain movement
        for villain in villains_2:
            villain.speedx = 2.5
            villain.move_speed()
            if villain.left_touches(platforms_level2[3]):
                villain.x = 0
            if kyle.touches(villain) or kihei.touches(villain):
                gamebox.pause()
                camera.draw(gamebox.from_text(400, 300, 'You lost to Auburn!', 60, 'red', True))
                camera.draw(gamebox.from_text(400, 350, 'Final Score was: ' + str(score) + '', 60, 'red'))

    if level == 2.5:
        finalfour = gamebox.from_image(400, 300, 'http://drive.google.com/uc?export=view&id=1RUW-QrwfU_BSH20z_Q76eOeiDNBPLhz7')
        finalfour.height = 600
        camera.clear('white')
        camera.draw(finalfour)
        camera.draw(gamebox.from_text(400, 100, 'You\'re moving on to the National Championship!', 40, 'white'))
        camera.draw(gamebox.from_text(400, 150, 'Total Score is: ' + str(score) + '', 40, 'white'))
        camera.draw(gamebox.from_text(400, 200, 'Press Space to Continue to Level 3', 40, 'white'))
        if pygame.K_SPACE in keys:
            level = 3
            kyle.x = 400
            kyle.y = 560
            kihei.x = 200
            kihei.y = 560
            time = 30

    # level 3
    if level == 3:
        camera.clear('white')
        camera.draw(background)
        camera.draw(hoop_3)

        # kyle movement
        kylemove(keys, 3)
        for platform in platforms_level3:
            kyle.move_to_stop_overlapping(platform)
        kyle.speedy += 0.75
        kyle.move_speed()

        # kihei movement
        kiheimove(keys, 3)
        for platform in platforms_level3:
            kihei.move_to_stop_overlapping(platform)
        kihei.speedy += 0.75
        kihei.move_speed()

        # collecting
        for coin in coins_level3:
            if kyle.touches(coin) or kihei.touches(coin):
                score += 10
                coins_level3.remove(coin)
        # display score
        camera.draw(gamebox.from_text(730, 50, 'Score: ' + str(score) + '', 40, 'black'))

        # finish level
        if kyle.touches(hoop_3) and kihei.touches(hoop_3):
            level = 3.5

        # drawing
        for platform in platforms_level3:
            camera.draw(platform)
        for coin in coins_level3:
            camera.draw(coin)
        for villain in villains_3:
            camera.draw(villain)

        camera.draw(kyle)
        camera.draw(kihei)

        # timer
        time -= 0.0167
        camera.draw(gamebox.from_text(100, 50, 'Shot Clock: ' + str(int(time)) + '', 40, 'black'))
        if int(time) == 0:
            gamebox.pause()
            camera.draw(gamebox.from_text(400, 300, 'You lost to Texas Tech!', 60, 'red', True))
            camera.draw(gamebox.from_text(400, 350, 'Final Score was: ' + str(score) + '', 60, 'red'))

        # villain movement
        for villain in villains_3:
            villain.speedx = 2.5
            villain.move_speed()
            if villain.left_touches(platforms_level3[3]):
                villain.x = 0
            if kyle.touches(villain) or kihei.touches(villain):
                gamebox.pause()
                camera.draw(gamebox.from_text(400, 300, 'You lost to Texas Tech!', 60, 'red', True))
                camera.draw(gamebox.from_text(400, 350, 'Final Score was: ' + str(score) + '', 60, 'red'))

    # winning
    if level == 3.5:
        champions = gamebox.from_image(400, 300, 'http://drive.google.com/uc?export=view&id=1Lz-o4Bcwdf885s7Sq24kSj7O68tkBdEL')
        champions.height = 600
        camera.clear('white')
        camera.draw(champions)
        camera.draw(gamebox.from_text(400, 175, 'You\'re the National Champions!', 60, 'white'))
        camera.draw(gamebox.from_text(400, 225, 'Total Score is: ' + str(score) + '', 60, 'white'))

    camera.display()


gamebox.timer_loop(60, tick)
