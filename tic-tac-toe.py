def initializeBoard():
    columns = []
    for i in range(0,3):
        rows = []
        for j in range(0,3):
            rows.append("_")
        columns.append(rows)
    return columns

def drawBoard(board):
    for i in range(0,3):
        print board[i]

def createPlayer(name, mark):
    return {"name":name, "mark": mark}

def getPlayerName(number):
    print "Please, insert player %d name:" % number
    return raw_input()

def getPlayerMark(player, board):
    print "%s... go!" % (player['name'])
    mark = raw_input()
    while True:
        try:
            if int(mark) in range(1,10):
                if(setPlayerMark(player, mark, board)):
                    drawBoard(board)
                    break
                else:
                    print "Wrong input! Please, select a free place"
                    mark = raw_input()
            else:
                print "Wrong input! Please, select an input between 1 and 9"
                mark = raw_input()
        except ValueError:
            print "Wrong input! Please, select an input between 1 and 9"
            mark = raw_input()


def setPlayerMark(player, mark, board):
    hashtableMarks = {"1": [0,0],"2":[0,1], "3":[0,2],
                      "4": [1,0],"5":[1,1], "6":[1,2],
                      "7": [2,0],"8":[2,1], "9":[2,2]}
    coordinates = hashtableMarks[str(mark)]
    if(board[coordinates[0]][coordinates[1]] == "_"):
        board[coordinates[0]][coordinates[1]] = player['mark']
        return True
    else:
        return False

def checkBoard(player, board):
    emptyCells = 0;
    for row in board:
        if row.count(player['mark']) == 3:
            return "win"
        for element in row:
            if element == "_":
                emptyCells += 1
    if emptyCells == 0:
        return "tie"
    if  (board[0][0] == board[1][0] == board[2][0] == player['mark']) or \
        (board[0][1] == board[1][1] == board[2][1] == player['mark']) or \
        (board[0][2] == board[1][2] == board[2][2] == player['mark']) or \
        (board[0][0] == board[1][1] == board[2][2] == player['mark']) or \
        (board[0][2] == board[1][1] == board[2][0] == player['mark']):
            return "win"
    return "game on"

# The Game begins
finish = False
while(finish == False):
    board = initializeBoard()
    drawBoard(board)
    players = [createPlayer(getPlayerName(1), 'X'), createPlayer(getPlayerName(2), 'O')]
    game = "game on"
    finish = False
    while(game == "game on"):
        getPlayerMark(players[0], board)
        game = checkBoard(players[0], board)
        if(game == "win"):
            print "%s WINS" % (players[0]['name'])
            break
        elif(game == "tie"):
            print "It's a tie!"
            break
        else:
            getPlayerMark(players[1], board)
        game = checkBoard(players[1], board)
        if game == "win":
            print "%s WINS" % (players[1]['name'])
        elif game == "tie":
            print "It's a tie!"
            break
    print "Do you want to play again? (y/n)"
    playAgain = ""
    while ((playAgain != 'y') and (playAgain != 'n')):
        playAgain = raw_input()
        if (playAgain == "y"):
            finish = False
        elif (playAgain == "n"):
            finish = True
        else:
            print "Wrong input! Use y, if you want to play again or n if you don't want."
            playAgain = ""
