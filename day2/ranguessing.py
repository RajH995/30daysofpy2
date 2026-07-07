import random

def createBoard():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('X')
        board.append(row)
    return board


def generateEnemyPoint(board):
    randomX = random.randint(0, 2)
    randomY = random.randint(0, 2)
    return (randomX, randomY)

def userInput():
    userMove = input("Enter your move (row and column) separated by a space (e.g., '1 2'): ")
    if not userMove or len(userMove.split()) != 2 or not all(num.isdigit() for num in userMove.split()):
        print("No input provided. Please enter your move.")
        return userInput()
    moves = userMove.split()
    if (moves[0] not in ['0', '1', '2'] or moves[1] not in ['0', '1', '2']):
        print("Invalid input. Please enter numbers between 0 and 2.")
        return userInput()
    userMove = tuple(map(int, userMove.split()))
    return userMove
def playGame():
    board = createBoard()
    for row in board:
        print(' '.join(row))
    enemyMove = generateEnemyPoint(board)
    userMove = userInput()
    while (userMove != enemyMove):
        print("You missed!")
        board[userMove[0]][userMove[1]] = 'O'
        print("Current Board:")
        for row in board:
            print(' '.join(row))
        userMove = userInput()
    else:
        print("You hit the enemy!")
    
playGame()

    
