import random


arr = [(num) for num in range(1, 101)]
choose = ['X', 'O']

def display(board):
    for i in range(10):
        strt = str(arr[i])
        if len(strt) == 1:
            print(board[i], end="  | ")
        else: 
            print(board[i], end=" | ")

    for i in range(10, 100):
        strt = str(arr[i])
        
        if i%10 != 0:
            
            if len(strt) == 1:
                print(board[i], end = "  | ")
            elif(len(strt) ==3):
                print(board[i], end = "| ")
            else:
                print(board[i], end=" | ")
        else:
            print()
            print("---| ---| ---| ---| ---| ---| ---| ---| ---| ---|")
            if len(strt) ==1:
                print(board[i], end = "  | ")
            else:
                print(board[i],  end=" | ")




def position_check(arr, pos):
    if arr[pos] not in choose:
        return True
    else:
        return False


def put_place(arr, sign, pos):
    
    if pos < 10:
        arr[pos] = sign
    else:
        arr[pos] = sign




def choose_mark():
    first = ''
    while first not in ['X', 'O']:
        first = input("Please, choose your mark: X or O ").upper()
    return first

def first_choose():
    """Randomly returns the player's mark that goes first."""
    return choose[random.choice((0, 1))]


def human_turn(board):
    mybot = player_sign(player)
    next = -1
    while(0>next or next>=100 or arr[next] == mybot or arr[next] == player):
        try:
            next = int(input('Input 1-100 '))-1
            if(arr[next] == mybot or arr[next]==player):
                print("Allready occupied")
                if(0>next or next>=100):
                    print('Wrong number')
            
        except KeyboardInterrupt:
            print('Incorrect ')
            exit()
        except:
            print('Wrong charracter')
    return next


def bot_turn(board):
    x = random.randint(0,99)
    while(board[x] =='O' or board[x] =='X'):
        x = random.randint(0,99)
    return x


def loser_find(arr, sign):
    for i in range (0, 96):
            if arr[i] == sign:
                if(i +4) % 10 >= 4:
                    if arr[i+1] == arr[i+2] == arr[i+4] == arr[i+3] == arr[i] == sign:
                        return True
    for i in range (0, 60):
            if arr[i] == sign:
                if(i +40) < 100:
                    if arr[i+10] == arr[i+20] == arr[i+40] == arr[i+30] == arr[i] == sign:
                        return True
    for i in range (57):
            if arr[i] == sign:
                if(i +4) % 10 > 4:
                    if arr[i+11] == arr[i+22] == arr[i+44] == arr[i+33] == arr[i] == sign:
                        return True
    for i in range (61):
            if arr[i] == sign:
                if(i +6) %10 <6:
                    if arr[i+9] == arr[i+18] == arr[i+36] == arr[i+27] == arr[i] == sign:
                        return True
    return False


def gameover(arr):
    return loser_find(arr, 'X') or loser_find(arr, 'O')


def area_full(arr):
    #check for array having only X and O
    return len(set(arr)) == 2

def check_loser(arr, sign):
    if(loser_find(arr, sign)):
        print(f'The player with the sign "{sign}" loses')
        return True
    if area_full(arr):
        print(f'It is draw')
        return True
    return False


def player_sign(player):
    if player == 'X':
        bot = 'O'
    else:
        bot = 'X'
    return bot



print('Welcome to our Tic-Tac-Toe game buddy')
player = choose_mark()
bot = player_sign(player)
bott = bot_turn(arr)
first_walk = first_choose()
if first_walk == player:
    print(f'Player with mark "{first_walk}" goes first.')
else:
    print("Computer goes first")
    put_place(arr, bot, bott)
    
while gameover(arr) == False:
    display(arr)
    print()
    print(f'Your turn')
    player_position = human_turn(arr)
    
    put_place(arr, player, player_position)
    bott = bot_turn(arr)
    put_place(arr, bot, bott)
    if loser_find(arr, player) or loser_find(arr, bot):
        display(arr)
        check_loser(arr, player)
        check_loser(arr, bot)
    else:
        continue
        
   
 


