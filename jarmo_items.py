import pygame as pg
from game_config import *
import sprites
import board_data

pg.init()


class Jarmoboard():
    def __init__(self, screen):
        self.pieces_types = ['a', 'A']
        self.__screen = screen
        self.__prepare_screen(screen)
        self.__table = board_data.board
        self.__archers_types = Piece_Types
        self.all_pieces = pg.sprite.Group()
        self.__create_board()
        self.__draw_all_pieces()
        pg.display.update()

    def __prepare_screen(self, screen):
        back_img = pg.image.load(IMG_Path_1 + IMG_1)
        screen.blit(back_img, (0, 0))

    def __create_board(self):

        self.loc = []
        for i in range(0, 25):
            self.loc.append(sprites.Location((i // 5, i % 5)))

        connections = {
            0: [7, 11],
            1: [8, 10],
            2: [5, 9, 11],
            3: [6, 14],
            4: [7, 13],
            5: [2, 12],
            6: [3, 7, 11, 13],
            7: [0, 4, 6, 8, 16],
            8: [1, 7, 13, 19],
            9: [2, 12],
            10: [1, 21],
            11: [0, 2, 6, 16, 18, 20],
            12: [5, 9, 15, 23],
            13: [4, 6, 8, 18, 22, 24],
            14: [3, 17],
            15: [12, 22],
            16: [7, 11, 17, 23],
            17: [14, 16, 18, 20, 24],
            18: [11, 13, 17, 21],
            19: [8, 22],
            20: [11, 17],
            21: [10, 18],
            22: [13, 15],
            23: [12, 16],
            24: [13, 17]
        }

        for i, loc in enumerate(self.loc):
            for connected_loc in connections.get(i, []):
                loc.valid_moves.append(self.loc[connected_loc])
                self.loc[connected_loc].valid_moves.append(loc)
        
        for location in self.loc:
            for adjustment in location.valid_moves:
                pg.draw.line(self.__screen, Brown,
                        [location.rect[0] + location.radius, location.rect[1] + location.radius],
                        [adjustment.rect[0] + location.radius, adjustment.rect[1] + location.radius],
                        6)
        pg.draw.rect(self.__screen, Brown_Red, (0, 150 - CS , 600, 60))
        pg.draw.rect(self.__screen, Brown_Wood, (0, 0, 600, 150 - CS))
        pg.draw.rect(self.__screen, Brown_Red, (0, 1000 - (210) + CS, 600, 60))
        pg.draw.rect(self.__screen, Brown_Wood, (0, 1000 - 150 + CS, 600, 150 - CS))
        pg.draw.rect(self.__screen, Brown_Midle, (0, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))
        pg.draw.rect(self.__screen, Brown_Midle, (540 - CS / 2, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))

        for location in self.loc:
            self.__screen.blit(location.image, location.rect)


    # Перерисовываем board:
    def update_board(self):
        self.__screen.fill(Brown_Wood_Light)

        back_img = pg.image.load(IMG_Path_1 + IMG_1)
        self.__screen.blit(back_img, (0, 0))

        for location in self.loc:
            for adjustment in location.valid_moves:
                pg.draw.line(self.__screen, Brown,
                        [location.rect[0] + location.radius, location.rect[1] + location.radius],
                        [adjustment.rect[0] + location.radius, adjustment.rect[1] + location.radius],
                        6)

        pg.draw.rect(self.__screen, Brown_Red, (0, 150 - CS , 600, 60))
        pg.draw.rect(self.__screen, Brown_Wood, (0, 0, 600, 150 - CS))
        pg.draw.rect(self.__screen, Brown_Red, (0, 1000 - (210) + CS, 600, 60))
        pg.draw.rect(self.__screen, Brown_Wood, (0, 1000 - 150 + CS, 600, 150 - CS))
        pg.draw.rect(self.__screen, Brown_Midle, (0, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))
        pg.draw.rect(self.__screen, Brown_Midle, (540 - CS / 2, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))

        for l in self.loc:
            if board_data.board[l.pos[1]][l.pos[0]] == 1:
                l.redraw_sprite(True)
            else:
                l.redraw_sprite(False)
            self.__screen.blit(l.image, l.rect)

        for piece in self.all_pieces:
            self.__screen.blit(piece.image, piece.rect)

        pg.display.flip()

    def __draw_all_pieces(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                # Проверяем есть ли в ключах словаря pieces_types название, содержащееся в field_value
                if field_value in self.pieces_types: # if field_value != 0:
                    p_archer = self.__create_piece(field_value,(j,i))
                    self.all_pieces.add(p_archer)

        for ix, piece in enumerate(self.all_pieces):
            print(f"Добавляю piece класса {piece.__class__} с координатами {piece.rect.x}, {piece.rect.y}")
            self.__screen.blit(piece.image, piece.rect)

    def __create_piece(self, symbol : str, table_coord : tuple[int, int]):
        if symbol == 'a':
            piece = sprites.BlackArcher(pos=table_coord)
        elif symbol == 'A':
            piece = sprites.WhiteArcher(pos=table_coord)
        else:
            raise f"Unknown symbol {symbol}"
        return piece
