import pygame as pg
from game_config import *

class Piece(pg.sprite.Sprite):
    def __init__(self, CS:int, color: str, field_name: str, file_posfix: str):
        super().__init__()
        picture = pg.image.load(Piece_Path + color + file_posfix).convert_alpha()
        self.image = pg.transform.scale(picture, (CS*2,CS*2)) ##откоректировать сайз когда прога начнёт работать так, что бы кружки были клетками...вроде бы
        self.rect = self.image.get_rect()
        self._color = color
        self.field_name = field_name

class Archer(Piece):
    def __init__(self, CS:int, color: str, field: str):
        super().__init__(CS, color, field, '_archer.png')

#class BlackArcher(Archer):
#    super()

#class WhiteArcher(Archer):
#    super()