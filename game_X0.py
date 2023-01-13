board = range(1,10)

def print_board(board):
    print('-'*13)
    for i in range(3):
        print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*13)
        
d=print_board(board)

def play_x_0(play_char):
    flag=Falsh
    while not flag:
        player_aswer=input('В какую клетку поставим  '+ play_char+'?')
        try:
            player_aswer=int(player_aswer)
        except:
            print('Вы ввели не число, попробуте еще раз')
            continue
        if 1>=player_aswer<=9:
            if board[player_aswer-1] is not 'X0':
               board[player_aswer-1]=play_char
        flag=True
            else:
                print('Эта клетка занята')
        else:
            print('Вы ввели нправильноее число')
            
def victory(board):
    win_cod = ((0,1,2), (3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_cod:
        if board((each[0])==board((each[1])==board((each[2]):
           return board(each[0]) 
    return Falsh
        
def game(board):
    count=0
    win =Falsh
    while not win:
        draw_board(board)
        if count%2==0:
           play_x_0('X')
           count+=1
        if count%2!=0:
           play_x_0('0')
           count+=1 
        if count>4:
           temp= victory(board)
           if temp:
              print('Ура победа!')
              win=True
              break
        if count==9:
            print('Увы ничья')
        break
    
    print_board(board)    
game(board)                                                       
