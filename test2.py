class TicTacToe:
    def __init__(self):
        self.board = [
                        ['1', '2', '3'],
                        ['4', '5', '6'],
                        ['7', '8', '9'],
                    ]
        self.current_player = chr(128512) 

    def display_board(self):
        
        print(
            f'{self.board[0][0]}|{self.board[0][1]}|{self.board[0][2]}',
            '-----',
            f'{self.board[1][0]}|{self.board[1][1]}|{self.board[1][2]}',
            '-----',
            f'{self.board[2][0]}|{self.board[2][1]}|{self.board[2][2]}',
            sep='\n'
        )

    def make_move(self, position):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == position:
                    self.board[i][j] = self.current_player  
                    return True
        return False

    def check_winner(self):

        for row in self.board:
            if row.count(row[0]) == 3:  
                return f'{row[0]} Победитель!'
        
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col]):
                return f'{self.board[0][col]} Победитель!'
        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2]) or \
           (self.board[0][2] == self.board[1][1] == self.board[2][0]):
            return f'{self.board[1][1]} Победитель!'


        return 'Ничья' 

    def switch_player(self):
        # Switch current player
        self.current_player = chr(128514) if self.current_player == chr(128512) else chr(128512)

class Game:
    def __init__(self):
        self.tic_tac_toe = TicTacToe()

    def play(self):
        print('Начало игры.')
        while True:
            self.tic_tac_toe.display_board()
            move = input(f'Игрок {self.tic_tac_toe.current_player}, введи номер позиции:\n')
            if self.tic_tac_toe.make_move(move):
                winner = self.tic_tac_toe.check_winner()
                if winner != 'Ничья':
                    self.tic_tac_toe.display_board()
                    print(winner)
                    break
                self.tic_tac_toe.switch_player()  # Switch after successful move
            elif all(tuple(filter(lambda a: True if len([True for i in a if i == 'X' or i == 'O']) == 3 else False, self.tic_tac_toe.board))): 
                print('Ничья')
                break
            else: print("Неверно попробуй еще.")

#Инициализация игры.
game_instance = Game()
game_instance.play()