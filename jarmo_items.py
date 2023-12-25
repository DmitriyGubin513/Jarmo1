import pygame as pg
from game_config import *
from archers import *
import board_data

pg.init()

class Jarmoboard():
    def __init__(self, screen, CellQty: int = CellQty, CS: int = CS):
        self.__prepare_screen(screen)
        self.__table = board_data.board
        self.__archers_types = Piece_Types
        self.__all_pieces = pg.sprite.Group()
        self.__draw_board(screen, CellQty, CS)
        self.__draw_all_pieces()
        pg.display.update()

    def __prepare_screen(self, screen):
        back_img = pg.image.load(IMG_Path_1 + IMG_1)
        screen.blit(back_img, (0, 0))

    def __draw_board(self, screen, CellQty, CS):
        pg.draw.rect(screen, Brown, (217, 325 + CS / 4, 168, 328), 5)
        pg.draw.line(screen, Brown, [CS / 2 + 98, CS / 2 + 150], [2 * CS + CS / 2 + 98, 1 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [CS / 2 + 98, CS / 2 + 150], [1 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [CS + CS / 2 + 98, CS / 2 + 150], [3 * CS + CS / 2 + 98, 1 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [CS + CS / 2 + 98, CS / 2 + 150], [CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [2 * CS + CS / 2 + 98, CS / 2 + 150], [CS / 2 + 98, 1 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [2 * CS + CS / 2 + 98, CS / 2 + 150], [4 * CS + CS / 2 + 98, 1 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [3 * CS + CS / 2 + 98, CS / 2 + 150], [CS + CS / 2 + 98, CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [3 * CS + CS / 2 + 98, CS / 2 + 150], [4 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [4 * CS + CS / 2 + 98, CS / 2 + 150], [2 * CS + CS / 2 + 98, CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [4 * CS + CS / 2 + 98, CS / 2 + 150], [3 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [CS / 2 + 98, CS * 2 + CS / 2 + 150], [2 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [CS + CS / 2 + 98, CS * 2 + CS / 2 + 150], [3 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [2 * CS + CS / 2 + 98, CS * 2 + CS / 2 + 150], [CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [3 * CS + CS / 2 + 98, CS * 2 + CS / 2 + 150], [4 * CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [4 * CS + CS / 2 + 98, CS * 2 + CS / 2 + 150], [2 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [3 * CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [2 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [2 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [3 * CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [3 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [2 * CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [3 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [4 * CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 5)
        pg.draw.line(screen, Brown, [4 * CS + CS / 2 + 98, 2 * CS * 2 + CS / 2 + 150], [2 * CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], [2 * CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], [3 * CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [2 * CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], [CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [2 * CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], [4 * CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [3 * CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], [CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 6)
        pg.draw.line(screen, Brown, [4 * CS + CS / 2 + 98, 3 * CS * 2 + CS / 2 + 150], [2 * CS + CS / 2 + 98, 4 * CS * 2 + CS / 2 + 150], 6)

        pg.draw.rect(screen, Brown_Red, (0, 150 - CS , 600, 60))
        pg.draw.rect(screen, Brown_Wood, (0, 0, 600, 150 - CS))
        pg.draw.rect(screen, Brown_Red, (0, 1000 - (210) + CS , 600, 60))
        pg.draw.rect(screen, Brown_Wood, (0, 1000 - 150 + CS, 600, 150 - CS))

        pg.draw.rect(screen, Brown_Midle, (0, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))
        pg.draw.rect(screen, Brown_Midle, (540 - CS / 2, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))

        for y in range(CellQty):                                                                                        ##Само игровое поле:
            for x in range(CellQty):
                pg.draw.circle(screen, Black, (x * CS + CS / 2 + 98, y * CS * 2 + CS / 2 + 150), CS / 4)
                pg.draw.circle(screen, White, (x * CS + CS / 2 + 102, y * CS * 2 + CS / 2 + 150), CS / 4)
                pg.draw.circle(screen, CircleColor, (x * CS + CS / 2 + 100, y * CS * 2 + CS / 2 + 150), CS / 4)

    def __draw_all_pieces(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                if field_value != 0:
                    p_archer = self.__create_piece(field_value,(j,i))
                    self.__all_pieces.add(p_archer)

    def __create_piece(self, piece_symbol:str, table_coord:tuple):
        piece_tuple = self.pieces_types[peaces_symbol]
        return Archer(self.__size)