from player import HumanPlayer,RandomcommputerPlayer,geniuscomputer
import time
import math

class Tictac:
    def __init__(self):
        self.board=self.make_board()
        self.current_winner=None


    @staticmethod
    def make_board():
        return[' ' for _ in range(9)]
    

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' +  '|'.join(row) + '|')

    @staticmethod
    def print_board_nums():
        number_board=[[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print(' | ' +' | '.join(row)+' | ')

    def available_moves(self):
        return[i for i, x in enumerate(self.board) if x==" "]
      
    
    def empty_squares(self):
        return' ' in self.board
    
    def num_empty_squares(self):
        return self.board.count(' ')
    
    def make_move(self , square, letter):
       if self.board[square]==' ':
           self.board[square] = letter 
           if self.winner(square,letter):
               self.current_winner=letter

           return True
       return False
    
    def winner(self,square ,letter):
        row_ind=math.floor(square/3)
        row =self.board[row_ind*3 : (row_ind +1)*3]
        if all ([spot==letter for spot in row]):
            return True
        col_ind = square % 3
        column =[self.board[col_ind+i*3] for i in range(3)]
        if all ([spot==letter for spot in column]):
            return True
        
        if square % 2 ==0:
            diagonal1 =[self.board[i] for i in [0,4,8]]
            if all ([spot==letter for spot in diagonal1]):
                return True
            diagonal2 =[self.board[i] for i in [2,4,6]]
            if all ([spot==letter for spot in diagonal2]):
                return True
        return False
    
def play (game, X_player ,O_player,Print_game=True):
    if Print_game:
        game.print_board_nums()

    letter = 'X'

    while game.empty_squares():
        if letter == "O":
            square= O_player.get_move(game)
        else:
            square=X_player.get_move(game)

        if game.make_move(square,letter):
            if Print_game:
                print(letter + f"makes amove to square{square}")
                game.print_board()
                print('')

            if game.current_winner:
                if Print_game:
                    print(letter + "wins")
                return letter

            if letter=="X":
                letter="O"
            else:
                letter="X"

        time.sleep(0.8)
    if Print_game:
        print("it a tie")


if __name__=="__main__":
    X_player = HumanPlayer('X')
    O_player = geniuscomputer('O')
    t = Tictac()
    play(t, X_player, O_player, Print_game=True)
