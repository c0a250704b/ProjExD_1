import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習１
    flip_bg_img = pg.transform.flip(bg_img,True,False) #練習８
    kk_img = pg.image.load("fig/3.png") #練習３
    kk_img = pg.transform.flip(kk_img,True,False) #練習３
    kk_rct = kk_img.get_rect() #練習１０
    kk_rct.center = 300,200 #練習１０
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        white = 0 #演習２
        hight = 0 #演習２
        kk_rct.move_ip((-1, 0)) #演習１
        key_lst = pg.key.get_pressed() #練習１０
        if key_lst[pg.K_UP]:
            hight -= 1 #演習２
        if key_lst[pg.K_DOWN]:
            hight += 1 #演習２
        if key_lst[pg.K_LEFT]:
            white -= 1 #演習２
        if key_lst[pg.K_RIGHT]:
            white += 2 #演習２
        kk_rct.move_ip((white,hight)) #演習２
        x = tmr % 3200 #練習５と９
        screen.blit(bg_img, [-x, 0]) #練習２と５
        screen.blit(flip_bg_img, [-x+1600, 0]) #練習７と８
        screen.blit(bg_img, [-x+3200, 0]) #練習９
        screen.blit(kk_img, kk_rct) #練習４と１０
        pg.display.update()
        tmr += 1       #練習５
        clock.tick(200)#練習６

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()