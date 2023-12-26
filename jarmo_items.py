import pygame as pg
from game_config import *
import sprites
import board_data

pg.init()


class Jarmoboard():
    def __init__(self, screen):
        self.pieces_types = {
            'A': ('w', ''),
            'a': ('b', '')
        }
        #self.pieces_types["a"]
        self.__screen = screen
        self.__prepare_screen(screen)
        self.__table = board_data.board
        self.__archers_types = Piece_Types
        self.__all_pieces = pg.sprite.Group()
        self.__create_board()
        self.__draw_all_pieces()
        pg.display.update()

    def __prepare_screen(self, screen):
        back_img = pg.image.load(IMG_Path_1 + IMG_1)
        screen.blit(back_img, (0, 0))

    def __create_board(self):
        pg.draw.rect(self.__screen, Brown, (217, 325 + CS / 4, 168, 328), 5)

        self.loc = []
        for i in range(0, 25):
            self.loc.append(sprites.Location((i // 5, i % 5)))

        self.loc[0].valid_moves.extend([self.loc[7], self.loc[11]])
        self.loc[1].valid_moves.extend([self.loc[8], self.loc[10]])
        self.loc[2].valid_moves.extend([self.loc[5], self.loc[9], self.loc[11]])
        self.loc[3].valid_moves.extend([self.loc[6], self.loc[14]])
        self.loc[4].valid_moves.extend([self.loc[7], self.loc[13]])
        self.loc[5].valid_moves.extend([self.loc[2], self.loc[12]])
        self.loc[6].valid_moves.extend([self.loc[3], self.loc[7], self.loc[11], self.loc[13]])
        self.loc[7].valid_moves.extend([self.loc[0], self.loc[4], self.loc[6], self.loc[8], self.loc[16]])
        self.loc[8].valid_moves.extend([self.loc[1], self.loc[7],  self.loc[13], self.loc[19]])
        self.loc[9].valid_moves.extend([self.loc[2], self.loc[12]])
        self.loc[10].valid_moves.extend([self.loc[1], self.loc[21]])
        self.loc[11].valid_moves.extend([self.loc[0], self.loc[2], self.loc[6], self.loc[16], self.loc[18], self.loc[20]])
        self.loc[12].valid_moves.extend([self.loc[5], self.loc[9], self.loc[15], self.loc[23]])
        self.loc[13].valid_moves.extend([self.loc[4], self.loc[6], self.loc[8], self.loc[18], self.loc[22], self.loc[24]])
        self.loc[14].valid_moves.extend([self.loc[3], self.loc[17]])
        self.loc[15].valid_moves.extend([self.loc[12], self.loc[22]])
        self.loc[16].valid_moves.extend([self.loc[7], self.loc[11], self.loc[17], self.loc[23]])
        self.loc[17].valid_moves.extend([self.loc[14], self.loc[16], self.loc[18], self.loc[20], self.loc[24]])
        self.loc[18].valid_moves.extend([self.loc[11], self.loc[13], self.loc[17], self.loc[21]])
        self.loc[19].valid_moves.extend([self.loc[8], self.loc[22]])
        self.loc[20].valid_moves.extend([self.loc[11], self.loc[17]])
        self.loc[21].valid_moves.extend([self.loc[10], self.loc[18]])
        self.loc[22].valid_moves.extend([self.loc[13], self.loc[15], self.loc[20]])
        self.loc[23].valid_moves.extend([self.loc[12], self.loc[16]])
        self.loc[24].valid_moves.extend([self.loc[13], self.loc[17]])

        for l in self.loc:
            for adj in l.valid_moves:
                pg.draw.line(self.__screen, Brown,
                             [l.rect[0] + l.radius, l.rect[1] + l.radius],
                             [adj.rect[0] + l.radius, adj.rect[1] + l.radius],
                             6)

        pg.draw.rect(self.__screen, Brown_Red, (0, 150 - CS , 600, 60))
        pg.draw.rect(self.__screen, Brown_Wood, (0, 0, 600, 150 - CS))
        pg.draw.rect(self.__screen, Brown_Red, (0, 1000 - (210) + CS, 600, 60))
        pg.draw.rect(self.__screen, Brown_Wood, (0, 1000 - 150 + CS, 600, 150 - CS))
        pg.draw.rect(self.__screen, Brown_Midle, (0, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))
        pg.draw.rect(self.__screen, Brown_Midle, (540 - CS / 2, 210 - CS, CS / 2 + 60, 1000 - 2 * (210-CS)))

        for l in self.loc:
            self.__screen.blit(l.image, l.rect)

    def __draw_all_pieces(self):
        for j, row in enumerate(self.__table):
            for i, field_value in enumerate(row):
                # Проверяем есть ли в ключах словаря pieces_types название, содержащееся в field_value
                if field_value in self.pieces_types.keys(): # if field_value != 0:
                    p_archer = self.__create_piece(field_value,(j,i))
                    self.__all_pieces.add(p_archer)

        for ix, piece in enumerate(self.__all_pieces):
            print(f"Добавляю piece класса {piece.__class__} с координатами {piece.rect.x}, {piece.rect.y}")
            self.__screen.blit(piece.image, piece.rect)


    def __create_piece(self, symbol : str, table_coord : tuple):
        # Преобразование координат для борды
        if symbol == 'a':
            x = table_coord[1] * (CS + CS / 2 + 98)
            y = table_coord[0] * (CS * 2 + CS / 2 + 150)
        elif symbol == 'A':
            x = table_coord[1] * (CS + CS / 2 + 102)
            y = table_coord[0] * (CS * 2 + CS / 2 + 150)
        else:
            raise f"Unknown symbol {symbol}"

        # unzip: *('w', '') === 'w', '' тождественно равны
        piece = sprites.Archer(CS, *self.pieces_types[symbol])
        # делаем штуки с писом
        piece.rect.x = x
        piece.rect.y = y
        return piece
