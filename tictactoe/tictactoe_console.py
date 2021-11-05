from tictactoe_gameengine import TictactoeGameEngine

def __init__(self):
    self.game_engine = TictactoeGameEngine()

    #show board
def play(self):
    self.game_engine.show_boerd()

    #무한반복
    while True:
        #   input row, col
        row = int(input('행: '))
        col =int(input('열: '))
        #   set row, col
        self.game_engine.set(row, col)
        #   show board
        self.game_engine.show_board()
        #   set winner
        winner = self.game_engine.set_winner()
        #승자가 있거나 무승부면 게임오버, 결과 출력
        if winner == 'X' or winner == 'O':
            print(f'{winner}이김~ 축하')
            break
        elif winner == 'd':
            print('무승부~')
            # change turn
        self.game_engine.change_turn()

if __name__ =='__main__':
    ttt_console = TictactoeConsole()
    ttt_console.play()





