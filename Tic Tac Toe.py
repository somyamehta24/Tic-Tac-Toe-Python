import itertools
import secrets
import random
def game_board(game_map,player=0,row=0,column=0,just_display=False):
    try:
        if game[row][column]!=0:
            print("Try another block the one you slected is already filled")
            return False
        s=" "
        for i in range(len(game)):
            s+="  "+str(i)
        if not just_display:
            game[row][column]=player
        print(s)
        for count,row in enumerate(game):
            print(count,row)
        return True

    except:
        print("Did You exceed")
        return False
def win(game_map):
    #horizontal
    for row in game_map:
        if row.count(row[0])==len(row) and row[0]!=0:
            print(f"Player-{check[0]} has won right horizontally")
            return True
    #verticle 
    for col in range(len(game_map)):
        check=[]
        for row in game_map:
            check.append(row[col])
        if check.count(check[0])==len(check) and check[0]!=0:
            print(f"Player-{check[0]} has won right vertically")
            return True
    rows=len(game)
    #\diagonal
    check=[]
    for col in range(rows):
        check.append(game_map[col][col])
    if check.count(check[0])==len(check) and check[0]!=0:
        print(f"Player-{check[0]} has won left diagonally")
        return True
    #/diagonal
    check=[]
    for col,ro in enumerate(reversed(range(rows))):
        check.append(game_map[col][ro])
    if check.count(check[0])==len(check) and check[0]!=0:
        print(f"Player-{check[0]} has won right diagonally")
        return True
play=True
players=[1,2]
while play:
    game=[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    gamewon=False
    random.shuffle(players)
    player_cycle=itertools.cycle(players)
    while not gamewon:
        curr_player=next(player_cycle)
        print(f"Current Player-{curr_player}")
        played=False
        while not played:
            x=int(input("Enter x coordinate Where you want to move:"))
            y=int(input("Enter y coordinate Where you want to move:"))
            played=game_board(game,curr_player,x,y,False)
        if win(game):
            again=input("The game is over do you like to play again? (y/n)")
            gamewon=True
            if again.lower()=="y":
                print("Restarting!!")
            elif again.lower()=="n":
                play=False
            else:
                print("Not a valid answer so we quit")
                play=False
                   