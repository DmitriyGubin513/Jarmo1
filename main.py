import board_data
import sprites
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


is_running = True
winner = ''

debug = True


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


def check_win_condition():
    global winner
    # условие победы за счёт убийства всех лучников противника:
    dead_white, dead_black = 0, 0
    for zombie in dead:
        print(zombie.__class__)
        if isinstance(zombie, sprites.WhiteArcher):
            dead_white += 1
        if isinstance(zombie, sprites.BlackArcher):
            dead_black += 1

    if dead_white == 5:
        winner = 'b'
        return True
    if dead_black == 5:
        winner = 'w'
        return True

    # за счет достижения противоположной стороны:
    win_condition_w, win_condition_b = True, True
    for black_row in board_data.board[0]:
        if black_row != 'A':
            win_condition_w = False
            break

    for white_row in board_data.board[-1]:
        if white_row != 'a':
            win_condition_b = False
            break

    if not win_condition_w and not win_condition_b:
        return False

    win_count_b, win_count_w = 0, 0
    ix = 0
    # Подсчёт очков
    for row in board_data.board:
        for cell in row:
            if cell == 'A':
                if ix < 2:
                    win_count_w += 2
                else:
                    win_count_w += 1
            if cell == 'a':
                if ix > 2:
                    win_count_b += 2
                else:
                    win_count_b += 1
        ix += 1

    score_w.update_score(win_count_w)
    score_b.update_score(win_count_b)

    if score_w.score > score_b.score:
        winner = 'w'
    if score_b.score > score_w.score:
        winner = 'b'
    return True


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
                if debug:
                    for piece in jarmoboard.all_pieces:
                        if piece.rect.collidepoint(mouse_pos):
                            print(f"Клик по спрайту {piece.__class__} на координатах: {piece.pos[0]}, {piece.pos[1]}")
                            print(f"Ячейка: {jarmoboard.loc[piece.pos[0] + piece.pos[1] * 5].pos}")
                            print(f"{board_data.board[piece.pos[0]][piece.pos[1]]}")
                    for l in jarmoboard.loc:
                        if l.rect.collidepoint(mouse_pos):
                            print(f"Клик по ячейке: {l.pos}, дата: {board_data.board[l.pos[1]][l.pos[0]]}")

                if is_running:
                    # Выбор фигуры:
                    for piece in jarmoboard.all_pieces:
                        if piece.rect.collidepoint(mouse_pos) and isinstance(piece,
                                                                             (sprites.WhiteArcher if turn_white
                                                                             else sprites.BlackArcher)):
                            selected_piece = piece
                            print(f"ВЫБРАНА ФИГУРА: {piece.pos}")
                            for i in range(0, 25):
                                if board_data.board[i // 5][i % 5] == 1:
                                    board_data.board[i // 5][i % 5] = 0
                            for adj in piece.get_loc(jarmoboard).valid_moves:
                                if board_data.board[adj.pos[1]][adj.pos[0]] == 0:
                                    board_data.board[adj.pos[1]][
                                        adj.pos[0]] = 1  # помечаем локацию как доступную для перехода
                            jarmoboard.update_board()

                    # Перенос выбранной фигуры:
                    if selected_piece:
                        for l in jarmoboard.loc:
                            if l.rect.collidepoint(mouse_pos) and l in selected_piece.get_loc(jarmoboard).valid_moves:
                                if board_data.board[l.pos[1]][l.pos[0]] == 1 or \
                                        (board_data.board[l.pos[1]][l.pos[0]] == 'a' and turn_white) \
                                        or (board_data.board[l.pos[1]][l.pos[0]] == 'A' and not turn_white):

                                    for piece in jarmoboard.all_pieces:
                                        if piece.pos == (l.pos[1], l.pos[0]) \
                                                and isinstance(piece, (
                                        sprites.BlackArcher if turn_white else sprites.WhiteArcher)):
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
                                    # очищаем ячейки, которые были помечены как доступные к переходу:
                                    for i in range(0, 25):
                                        if board_data.board[i % 5][i // 5] == 1:
                                            board_data.board[i % 5][i // 5] = 0
                                    to_res = None
                                    if selected_piece.pos[0] == 0 and turn_white:
                                        if dead:
                                            for pp in dead:
                                                if isinstance(pp, sprites.WhiteArcher):
                                                    to_res = pp
                                    if selected_piece.pos[0] == 4 and not turn_white:
                                        if dead:
                                            for pp in dead:
                                                if isinstance(pp, sprites.BlackArcher):
                                                    to_res = pp
                                    if to_res:
                                        ix = 0
                                        for res_loc in board_data.board[-1 if turn_white else 0]:
                                            if res_loc == 0:
                                                to_res.pos = (4 if turn_white else 0, ix)
                                                res_location = to_res.get_loc(jarmoboard)
                                                to_res.rect.x = res_location.rect.x - res_location.radius
                                                to_res.rect.y = res_location.rect.y - res_location.radius
                                                board_data.board[to_res.pos[1]][to_res.pos[0]] = 'A' \
                                                    if isinstance(to_res, sprites.WhiteArcher) \
                                                    else 'a'
                                                print(f"RESURRECTING {'White' if turn_white else 'Black'} at "
                                                      f"{to_res.pos[1]}, {to_res.pos[0]}")
                                                dead.remove(to_res)
                                                break
                                            ix += 1
                                    if check_win_condition():
                                        print("WIN_CONDITION FIRED")
                                        text_winner = font.render(f"Чёрные победили\nсо счётом {score_b.score}!"
                                                                  if winner == 'b'
                                                                  else (f"Белые победили\nсо счётом {score_w.score}!"
                                                                        if winner == 'w' else "НИЧЬЯ!"),
                                                                  True, (200, 50, 50))
                                        screen.blit(text_winner, (110, 300))
                                        is_running = False
                                    selected_piece = None
                                    turn_white = not turn_white
                                    if is_running:
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
