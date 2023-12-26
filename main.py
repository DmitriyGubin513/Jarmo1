from game_config import *
from jarmo_items import *


clock = pg.time.Clock()
screen = pg.display.set_mode(WinSize)
screen.fill(Brown_Wood_Light)

jarmoboard = Jarmoboard(screen)

run = True
while run:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False