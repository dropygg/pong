from pygame import *



img_plat = "plat.png" 
img_plat1 = "plat1.png" 
img_back = "sky.png" 
img_enemy = "ufo.png" 
img_asteroid = 'asteroid.png'

win_width = 700
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

run = True
while run:

    for e in event.get():
       if e.type == QUIT:
           run = False

    window.blit(background,(0,0))


    display.update()
