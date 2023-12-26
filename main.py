from game_config import *
from jarmo_items import *

clock = pg.time.Clock()
screen = pg.display.set_mode(WinSize)
screen.fill(Brown_Wood_Light)

font = pg.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

jarmoboard = Jarmoboard(screen)

text_turn = font.render('', True, BLACK)
text_turn_w = font.render('Ход белых', True, WHITE)
text_turn_b = font.render('Ход чёрных', True, BLACK)


class Score:
    def __init__(self, desc):
        self.desc = desc
        self.text = ""
        self.score = 0
        self.update_score(0)

    def update_score(self, add=1):
        self.score += add
        self.text = self.desc + f" {self.score}"


score_w = Score('Счёт белого:')
score_b = Score('Счёт чёрного:')


selected_piece = None

dead = []

turn_white = True  # флажок для определения того, чей ход: True - белые, False - чёрные

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
            break

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:  # Проверяем левую кнопку мыши (1 - левая, 3 - правая, 2 - средняя)
                mouse_pos = pg.mouse.get_pos()  # Получаем позицию мыши в момент клика

                # Информация в консоль:
                for piece in jarmoboard.all_pieces:
                    if piece.rect.collidepoint(mouse_pos):
                        print(f"Клик по спрайту {piece.__class__} на координатах: {piece.pos[0]}, {piece.pos[1]}")
                        print(f"Ячейка: {jarmoboard.loc[piece.pos[0] + piece.pos[1] * 5].pos}")
                        print(f"{board_data.board[piece.pos[0]][piece.pos[1]]}")
                for l in jarmoboard.loc:
                    if l.rect.collidepoint(mouse_pos):
                        print(f"Клик по ячейке: {l.pos}, дата: {board_data.board[l.pos[1]][l.pos[0]]}")

                # Перенос фигуры:
                for piece in jarmoboard.all_pieces:
                    if piece.rect.collidepoint(mouse_pos) and isinstance(piece,
                                                                         (sprites.WhiteArcher if turn_white
                                                                         else sprites.BlackArcher)):
                        selected_piece = piece
                        print(f"ВЫБРАНА ФИГУРА: {piece.pos}")
                        moves = ''
                        for adj in piece.get_loc(jarmoboard).valid_moves:
                            moves += f'{adj.pos[1], adj.pos[0]}'
                        print(f"VALID MOVES: {moves}")

                if selected_piece:
                    for l in jarmoboard.loc:
                        if l.rect.collidepoint(mouse_pos) and l in selected_piece.get_loc(jarmoboard).valid_moves:
                            if board_data.board[l.pos[1]][l.pos[0]] == 0 or \
                                    (board_data.board[l.pos[1]][l.pos[0]] == 'a' and turn_white)\
                                    or (board_data.board[l.pos[1]][l.pos[0]] == 'A' and not turn_white):

                                for piece in jarmoboard.all_pieces:
                                    if piece.pos == (l.pos[1], l.pos[0]):
                                        piece.loc = (-1, -1)
                                        piece.rect.x = -100
                                        piece.rect.y = -100
                                        dead.append(piece)
                                        if turn_white:
                                            score_w.update_score(1)
                                        else:
                                            score_b.update_score(1)
                                        print("SOMEONE DIED!")
                                # Задаём новые координаты спрайта:
                                selected_piece.rect.x = l.rect.x - l.radius
                                selected_piece.rect.y = l.rect.y - l.radius
                                board_data.board[selected_piece.pos[0]][selected_piece.pos[1]] = 0
                                selected_piece.pos = (l.pos[1], l.pos[0])
                                board_data.board[l.pos[1]][l.pos[0]] = 'A' \
                                    if isinstance(selected_piece, sprites.WhiteArcher) \
                                    else 'a'
                                selected_piece = None
                                turn_white = not turn_white
                                jarmoboard.update_board()

    # Отображение текста на экране
    if turn_white:
        text_turn = text_turn_w
    else:
        text_turn = text_turn_b

    text_score_w = font.render(score_w.text, True, WHITE)
    text_score_b = font.render(score_b.text, True, BLACK)
    screen.blit(text_score_w, (10, 30))
    screen.blit(text_score_b, (400, 30))
    screen.blit(text_turn, (220, 30))

    clock.tick(FPS)
    pg.display.flip()
