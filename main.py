import tkinter
import tkinter as tk
from kivy.app import App
from kivy.uix.label import Label


class Tic_Tac_Toe:
    def __init__(self):
        self.player1 = chr(int('1F608', 16))
        self.player2 = chr(int('1F607', 16))
        self.turn = chr(int('1F608', 16))

        self.tk = tkinter.Tk()
        self.tk.configure(bg='#A66100')
        self.tk.title("Tic_Tac_Toe")
        self.tk.geometry("%dx%d" % (505, 800))
        #self.tk['bg'] = "#A66F00"

        self.board = [['X' for _ in range(3)] for i in range(3)]

        self.frame1 = tkinter.Frame(self.tk, bg="#FFAA00", bd=5, width=20, height=50)
        self.frame1.pack(side=tkinter.TOP, fill=tkinter.BOTH)
        

        self.frame2 = tkinter.Frame(self.tk, bg="#FFAA00", bd=5, width=300, height=50)
        self.frame2.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
        tkinter.Button(self.frame2, text=chr(int('1F503', 16)), font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.replace_bord() ).pack(side=tkinter.RIGHT)

        self.print_turn_player = tk.Label(self.tk, text=f'ХОД: {self.turn}', font=("Arial", 40), fg="#000000", bg="#FFAA00", width=2, height=2)
        self.print_turn_player.pack(side=tkinter.TOP, pady=10, padx=10, fill=tkinter.BOTH)#

        self.viner = tk.Label(self.tk, text=self.check_winner(), font=("Arial", 40), fg="#000000", bg="#FFAA00", width=2, height=2)
        self.viner.pack(side=tkinter.BOTTOM, pady=10, padx=10,fill=tkinter.BOTH)#

        self.list_buttons = [
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(0,(0, 0,))).grid(row=0, column=0),
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(1,(0, 1,))).grid(row=0, column=1),
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(2,(0, 2,))).grid(row=0, column=2),
                
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(3,(1, 0,))).grid(row=1, column=0),
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(4,(1, 1,))).grid(row=1, column=1),
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(5,(1, 2,))).grid(row=1, column=2),

                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(6,(2, 0,))).grid(row=2, column=0),
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(7,(2, 1,))).grid(row=2, column=1),
                tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(8,(2, 2,))).grid(row=2, column=2)
                ]


        self.tk.mainloop()

    
    def make_moove(self, number_button, row_col):
        
        self.list_buttons[number_button] = tkinter.Button(self.frame1, text=self.turn, font=("Arial", 40), width=5, height=2, fg="#000000", bg="#FFAA00").grid(row=row_col[0], column=row_col[1])
        self.board[row_col[0]][row_col[1]] = self.turn
        self.viner.config(text=self.check_winner())
        if self.turn == chr(int('1F608', 16)): 
            self.turn = chr(int('1F607', 16))
            self.print_turn_player.config(text=f'ХОД: {self.turn}')
        else: 
            self.turn = chr(int('1F608', 16))
            self.print_turn_player.config(text=f'ХОД: {self.turn}')

    def check_winner(self):

        for row in self.board:
            if row.count(self.player1) == 3:
                return f'\n{self.player1} Победитель!'
            elif row.count(self.player2) == 3:  
                return f'\n{self.player2} Победитель!'
        
        for col in range(3):
            if (self.board[0][col] == self.board[1][col] == self.board[2][col] == self.player1):
                return f'\n{self.player1} Победитель!'
            elif (self.board[0][col] == self.board[1][col] == self.board[2][col] == self.player2):
                return f'\n{self.player2} Победитель!'
        
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player1)  or (self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player1):
            return f'\n{self.player1} Победитель!'
        elif (self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player2) or (self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player2):
            return f'\n{self.player2} Победитель!'

        return f'Пока не понятно {chr(int('1F605', 16))}'

    def replace_bord(self):

        self.board = [['X' for _ in range(3)] for i in range(3)]

        self.list_buttons_work = [
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(0,(0, 0,))).grid(row=0, column=0),
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(1,(0, 1,))).grid(row=0, column=1),
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(2,(0, 2,))).grid(row=0, column=2),
                
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(3,(1, 0,))).grid(row=1, column=0),
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(4,(1, 1,))).grid(row=1, column=1),
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(5,(1, 2,))).grid(row=1, column=2),

            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(6,(2, 0,))).grid(row=2, column=0),
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(7,(2, 1,))).grid(row=2, column=1),
            tkinter.Button(self.frame1, text="", font=("Arial", 40), width=5, height=2, fg="#000000", bg="#A66F00", command=lambda: self.make_moove(8,(2, 2,))).grid(row=2, column=2)
            ]
        for c, i in enumerate(self.list_buttons_work):
            self.list_buttons[c] = i



if __name__ == '__main__':
    Tic_Tac_Toe()  # Запуск приложения
