def initializeGame():
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

def createPlayers():
    print "Please, insert player 1 name:"
    player1 = raw_input()
    print "Please, insert player 2 name:"
    player2 = raw_input()
    return [player1, player2]

def getPlayerMark(player, board):
    print "%s... go!" % (player)
    mark = raw_input()
    exit = False
    while True:
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

def setPlayerMark(player, mark, board):
    hashtableMarks = {"1": [0,0],"2":[0,1], "3":[0,2],
                      "4": [1,0],"5":[1,1], "6":[1,2],
                      "7": [2,0],"8":[2,1], "9":[2,2]}
    coordinates = hashtableMarks[str(mark)]
    if(board[coordinates[0]][coordinates[1]] == "_"):
        board[coordinates[0]][coordinates[1]] = player
        return True
    else:
        return False



def checkBoard(player, board):
    for row in board:
        if row.count(player) == 3:
            return True
    if board[0][0] == board[1][0] == board[2][0] == player:
        return True

    if board[0][1] == board[1][1] == board[2][1] == player:
        return True

    if board[0][2] == board[1][2] == board[2][2] == player:
        return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

board = initializeGame()
drawBoard(board)
players = createPlayers()
finishGame = False
while(finishGame == False):
    getPlayerMark(players[0], board)
    if(checkBoard(players[0], board)):
        print "PLAYER 1 WIN"
        break
    else:
        getPlayerMark(players[1], board)
    finishGame = checkBoard(players[1], board)
    if finishGame:
        print "PLAYER 2 WIN"
