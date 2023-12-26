import pygame as pg
from game_config import *


class Location(pg.sprite.Sprite):
    def __init__(self, pos, primary_color=Black, secondary_color=White, radius=(CS/4)):
        super().__init__()
        self.radius = radius
        offset_x = 98 + radius
        offset_y = 150 + radius
        self.image = pg.Surface((radius * 2 + 4, radius * 2 + 4), pg.SRCALPHA)
        pg.draw.circle(self.image, primary_color, (radius, radius), radius)
        pg.draw.circle(self.image, secondary_color, (radius + 4, radius + 4), radius)
        self.rect = self.image.get_rect(topleft=(radius * (4 * pos[0]) + offset_x,
                                                 radius * (8 * pos[1]) + offset_y))
        self.valid_moves = []
        self.pos = pos
        self.radius = radius


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