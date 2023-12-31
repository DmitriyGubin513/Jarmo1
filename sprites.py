import pygame as pg
from game_config import *


class Location(pg.sprite.Sprite):
    def __init__(self, pos, highlighted=False, radius=(CS / 4)):
        super().__init__()
        self.radius = radius
        offset_x = 98 + radius
        offset_y = 150 + radius
        self.image = pg.Surface((radius * 2 + 4, radius * 2 + 4), pg.SRCALPHA)
        self.redraw_sprite(highlighted)
        self.rect = self.image.get_rect(topleft=(radius * (4 * pos[0]) + offset_x,
                                                 radius * (8 * pos[1]) + offset_y))
        self.valid_moves = []
        self.pos = pos
        self.radius = radius

    def redraw_sprite(self, highlighted):
        pg.draw.circle(self.image, Black, (self.radius, self.radius), self.radius)
        pg.draw.circle(self.image,
                       White if not highlighted else CircleColor,
                       (self.radius + 4, self.radius + 4),
                       self.radius)


class Piece(pg.sprite.Sprite):
    def __init__(self, color: str, field_name: str, file_posfix: str, pos: tuple[int, int]):
        super().__init__()
        picture = pg.image.load(Piece_Path + color + file_posfix).convert_alpha()
        self.image = pg.transform.scale(picture, (CS, CS))
        self.rect = self.image.get_rect(topleft=(pos[1] * CS * 1 + 98,
                                                 pos[0] * CS * 2 + 150))
        self._color = color
        self.field_name = field_name
        self.pos = pos

    def get_loc(self, board):
        return board.loc[self.pos[0] + self.pos[1] * 5]


class Archer(Piece):
    def __init__(self, color: str, field: str, pos: tuple[int, int]):
        super().__init__(color, field, '_archer.png', pos)


class BlackArcher(Archer):
    def __init__(self, pos: tuple[int, int]):
        super().__init__('b', '', pos)


class WhiteArcher(Archer):
    def __init__(self, pos: tuple[int, int]):
        super().__init__('w', '', pos)
