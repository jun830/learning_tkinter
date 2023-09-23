import random

class Othello:
    def __init__(self, p1="player1",p1_att=0, p2="player2",p2_att=0,board=None):
        self.player1 = p1
        self.player2 = p2
        self.attribute = {1:p1_att, 2:p2_att}
        if board is None:
            self.board = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                          [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
                          [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
                          [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
                          [-1, 0, 0, 0, 2, 1, 0, 0, 0,-1],
                          [-1, 0, 0, 0, 1, 2, 0, 0, 0,-1],
                          [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
                          [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
                          [-1, 0, 0, 0, 0, 0, 0, 0, 0,-1],
                          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        else:
            self.board = board

    def _is_can_put(self, ID, x, y, dx, dy, depth=1):
        if self.board[x][y] == ID:
            if depth == 1:
                return False
            else:
                return True
        elif self.board[x][y] in {-1, 0}:
            return False
        else:
            return self._is_can_put(ID, x + dx, y + dy, dx, dy, depth + 1)

    def _putDFS(self, ID, x, y, dx, dy, depth=0):
        if self.board[x][y] == ID:
            if depth == 0:
                return False
            else:
                return True
        elif self.board[x][y] in {-1, 0}:
            return False
        else:
            f = self._putDFS(ID, x + dx, y + dy, dx, dy, depth + 1)
            if f: self.board[x][y] = ID
            return f

    def put_board(self, ID, x, y):
        flag = False
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            f = self._putDFS(ID, x + dx, y + dy, dx, dy)
            flag |= f
        if flag:
            self.board[x][y] = ID
            return True
        else:
            return False

    def check_can_put(self, ID, x, y):
        if self.board[x][y] != 0:
            return False
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if self._is_can_put(ID, x + dx, y + dy, dx, dy):
                return True
        return False

    def result_output(self):
        stone_count = [0] * 10
        for b_i in self.board:
            print(*b_i)
            for b_j in b_i:
                stone_count[b_j] += 1
        if stone_count[1] == stone_count[2]:
            print("DRAW")
        elif stone_count[1] > stone_count[2]:
            print("WIN", self.player1)
        else:
            print("WIN", self.player2)

    def player_turn(self, lst):
        print("置きたい場所を選んでください")
        for b_i in self.board[1:9]:
            print(*b_i)
        print(*lst)
        x, y = map(int, input().split())
        return x, y

    def com_random(self, lst):
        return random.choice(lst)

    def game(self):
        turn = 1
        pass_count = 0
        while pass_count <= 1:
            can_put_list = [(x, y) for x in range(1, 9) for y in range(1, 9)if self.check_can_put(turn, x, y)]
            if len(can_put_list) == 0:
                x, y = -1, -1

            elif self.attribute[turn] == 0:
                x, y = self.player_turn(can_put_list)

            elif self.attribute[turn] == 100:
                x, y = self.com_random(can_put_list)

            else:
                x, y = can_put_list[0]

            if x > 0:
                self.put_board(turn, x, y)
                pass_count = 0
            else:
                pass_count += 1

            turn = 2 if turn == 1 else 1

        self.result_output()


game = Othello(p1_att=100,p2_att=100)
game.game()
