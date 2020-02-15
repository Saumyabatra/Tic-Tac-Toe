import random
#player1=input("Please pick a marker 'X' or 'O'")
#position=int(input("Please Enter a number"))
from IPython.display import clear_output
clear_output()
l=["O","X"]
m=[1,2,3,4,5,6,7,8,9]
def display_board(board):
    clear_output()
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])


def player_input():
     #return player 1 input and player 2 input as a tuple
    marker=" "
    while  marker!="X" and marker!="O":
       marker=input("PLayer 1, choose X or O:").upper()
    player1=marker
    if player1=="X":
        #player2="O"
        return ("X","O")
    else:
        #player2="X"
        return ("O","X")
def place_marker(board,marker,position):
        board[position]=marker
def win_check(board,mark):
   
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return "Player 1"
    else:
        return "Player 2"
def space_check(board,position):
    return board[position]==" "
def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
        #Board is full if true
    return True
def player_choice(board):
    position=0
    while position not in m or not space_check(board,position):
        position=int(input("Choose a position:[O,10]"))
    return position
def replay():
    choice=input("PLay again ? Enter Yes or No")
    return choice=="Yes".lower()

print("Welcome to Tic TAC Toe")
while True:
    #play the game
    board=[" "]*10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn+" Will go first")
    play_game=input("Ready to play?y or nay?")
    if play_game=="y" or play_game=="yes":
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn=="Player 1":
            #show the board
            display_board(board)
            #choose a position
            position=player_choice(board)
            #place the marker on the position
            place_marker(board,player1_marker,position)
            #check if they won
            if win_check(board,player1_marker):
                display_board(board)
                print("Player 1 has won!")
                game_on=False
            else:
                if full_check(board):
                    display_board(board)
                    print("Tie game!")
                    game_on=False
                else:
                    turn="Player 2"
        else:
            #show the board
            display_board(board)
            #choose a position
            position=player_choice(board)
            #place the marker on the position
            place_marker(board,player2_marker,position)
            #check if they won
            if win_check(board,player2_marker):
                display_board(board)
                print("Player 2 has won!")
                game_on=False
            else:
                if full_check(board):
                    display_board(board)
                    print("Tie game!")
                    game_on=False
                else:
                    turn="Player 1"
    if not replay():
        break
            #or check if there is a tie
            
            #no tie and no win?Then next player's turn
            