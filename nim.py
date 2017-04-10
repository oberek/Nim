from abc import ABCMeta, abstractmethod

class Board(object):
    board = {3,5,7}

    def get_sum(self):
        return sum(self.board)

    def display_board(self):
        pass

    def take_pieces(self, change_this):
        row = change_this[0]
        num_of_pieces = change_this[1]
        if row > 0 and row < len(self.board):
            if 0 < num_of_pieces <= self.board[row]:
                self.board[change_this[0]] -= change_this[1]
                return True
        return False

class Player:
    won = False
    __metaclass__ = ABCMeta

    @abstractmethod
    def take_turn(self): pass


class Human(Player):
    def take_turn(self):
        row_num =

class AI(Player):
    pass

class Engine:

    def get_player_type(self, num):
        user_input = input("enter 1 for human or 2 for ai")
        if user_input is "1":
            return Human()
        else:
            return AI()

    def run(self):
        board = Board()
        player1 = self.get_player_type("One")
        player2 = self.get_player_type("Two")
        while board.get_sum() > 0:
            board.display_board()
            print("Player 1")
            player1.take_turn()
            if board.get_sum() > 0:
                board.display_board()
                print("Player 2")
                player2.take_turn()

        if player1.won:
            print("Player 1 Won!")
        else:
            print("Player 2 Won!")

