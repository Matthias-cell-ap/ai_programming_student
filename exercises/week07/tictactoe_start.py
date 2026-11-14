"""
Oefening: TicTacToe met Minimax & Alpha-Beta
==============================================
"""
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def possible_moves(self):
        """Geef lijst van (rij, kolom)-tupels van lege velden."""
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == ' ']

    def is_valid_move(self, x, y):
        return x > -1 and y > -1 and x < 3 and y < 3 and self.board[x][y] == ' '

    def make_move(self, x, y, player):
        if self.is_valid_move(x, y):
            self.board[x][y] = player

    def undo_move(self, x, y):
        self.board[x][y] = ' '

    def check_winner(self):
        for x in range(3):
            if self.board[x][0] != ' ' and self.board[x][0] == self.board[x][1] == self.board[x][2]:
                return self.board[x][0]
        for y in range(3):
            if self.board[0][y] != ' ' and self.board[0][y] == self.board[1][y] == self.board[2][y]:
                return self.board[0][y]
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[1][1]

    def is_draw(self):
        return len(self.possible_moves()) == 0 and not self.check_winner()

    def minimax(self, depth, is_maximizing, alpha=-float('inf'), beta=float('inf'), max_depth=None):
        if self.check_winner() == 'X': return 1
        if self.check_winner() == 'O': return -1
        if self.is_draw(): return 0
        if depth >= max_depth: return 0

        if is_maximizing:
            best = -float('inf')
            for zet in self.possible_moves():
                self.make_move(*zet, 'X')
                best = max(best, self.minimax(depth+1, False, alpha, beta))
                self.undo_move(*zet)
                alpha = max(best, alpha)
                if beta <= alpha:                                            
                    break
            return best
        else:
            best = float('inf')
            for zet in self.possible_moves():
                self.make_move(*zet, 'O')
                best = min(best, self.minimax(depth+1, True, alpha, beta))
                self.undo_move(*zet)
                beta = min(best, beta)
                if beta >= alpha:                                            
                    break
            return best

    def find_best_move(self):
        best_move = None

        best_score = -float('inf')
        for zet in self.possible_moves():
            self.make_move(*zet, 'X')
            score = self.minimax(0, False)
            self.undo_move(*zet)
            if score > best_score:
                best_score = score
                best_move = zet
        return best_move


    def print_board(self):
        horizontal_line = "+---+---+---+"
        print(horizontal_line)
        for row in self.board:
            print("| {} | {} | {} |".format(row[0], row[1], row[2]))
            print(horizontal_line)

    def play(self):
        beurt = 'O'

        while True:
            if self.is_draw():
                self.print_board()
                print("draw")

            if beurt == 'O':
                self.print_board()
                print("Waar wil je zetten (y x)")
                antwoord = input().split(' ')
                if self.is_valid_move(int(antwoord[0]), int(antwoord[1])):
                    self.make_move(int(antwoord[0]), int(antwoord[1]), 'O')
                    beurt = 'X'
                else:
                    print("yo geef iet geldig in")
            
            winnaar = self.check_winner()
            if winnaar:
                self.print_board()
            if winnaar == 'O':
                print("O wint")
                break
            if winnaar == 'X':
                print("X wint")
                break
            if self.is_draw():
                self.print_board()
                print("draw")
                break
            
            if beurt == 'X':
                zet = self.find_best_move()
                self.make_move(zet[0], zet[1], 'X')
                beurt = 'O'
            
            winnaar = self.check_winner()
            if winnaar:
                self.print_board()
            if winnaar == 'O':
                print("O wint")
                break
            if winnaar == 'X':
                print("X wint")
                break
            if self.is_draw():
                self.print_board()
                print("draw")
                break


if __name__ == "__main__":
    game = TicTacToe()
    game.play()