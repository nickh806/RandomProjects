import random
import time
row1 = [0,1,2]
row2 = [3,4,5]
row3 = [6,7,8]

startTime = time.time()

def playerturn():
    print("Select a unentered tile")
    playerselection = int(input())
    checkplayer(playerselection)


def checkplayer(playerselection):
    if playerselection > 8 or playerselection < 0:
        playerturn()

    if playerselection >= 0 and  playerselection <= 2:
        if row1[playerselection] != 'o' and row1[playerselection] != 'x':
            row1[playerselection] = 'x'
            printBoard()
        else:
            playerturn()

    if playerselection >= 3 and  playerselection <= 5:
        playerselection = playerselection-3
        if row2[playerselection] != 'o' and row2[playerselection] != 'x':
            row2[playerselection] = 'x'
            printBoard()
        else:
            playerturn()

    if playerselection >= 6 and  playerselection <= 8:
        playerselection = playerselection-6
        if row3[playerselection] != 'o' and row3[playerselection] != 'x':
         row3[playerselection] = 'x'
         printBoard()
        else:
            playerturn()

def aiTurn():
    aiSelection = random.randint(0, 8)
    if aiSelection > 8 or aiSelection < 0:
        aiTurn()

    if aiSelection >= 0 and  aiSelection <= 2:
        if row1[aiSelection] != 'o' and row1[aiSelection] != 'x':
            row1[aiSelection] = 'o'
            printBoard()
        else:
            aiTurn()

    if aiSelection >= 3 and  aiSelection <= 5:
        aiSelection = aiSelection-3
        if row2[aiSelection] != 'o' and row2[aiSelection] != 'x':
         row2[aiSelection] = 'o'
         printBoard()
        else:
            aiTurn()

    if aiSelection >= 6 and  aiSelection <= 8:
        aiSelection = aiSelection-6
        if row3[aiSelection] != 'o' and row3[aiSelection] != 'x':
         row3[aiSelection] = 'o'
         printBoard()
        else:
            aiTurn()


def printBoard():
    for i in range(1, 4):
        print(eval("row" + str(i)))


def checkX():
    checker1 = 0
    checker2 = 0
    checker3 = 0
    for i in range(3):
        if row1[i] == 'x':
            checker1 += 1

        if row2[i] == 'x':
            checker2 += 1

        if row3[i] == 'x':
            checker3 += 1

        if checker1 == 3 or checker2 == 3 or checker3 == 3:
            return True
        if row1[i] == 'x' and row2[i] == 'x' and row3[i] == 'x':
            return True
        if row1[0] == 'x' and row2[1] == 'x' and row3[2] == 'x' or row1[2] == 'x' and row2[1] == 'x' and row3[0] == 'x':
            return True
    return False

def checkO():
    checker1 = 0
    checker2 = 0
    checker3 = 0
    for i in range(3):
        if row1[i] == 'o':
            checker1 += 1

        if row2[i] == 'o':
            checker2 += 1

        if row3[i] == 'o':
            checker3 += 1

        if checker1 == 3 or checker2 == 3 or checker3 == 3:
            return True
        if row1[i] == 'o' and row2[i] == 'o' and row3[i] == 'o':
            return True
        if row1[0] == 'o' and row2[1] == 'o' and row3[2] == 'o' or row1[2] == 'o' and row2[1] == 'x' and row3[0] == 'o':
            return True
    return False


playerWins = False
aiWins = False

printBoard()

while True:
    print("PLAYER TURN")
    playerturn()
    playerWins = checkX()
    print("")
    if playerWins:
        print("Player wins!")
        endTime =time.time()
        totalTime = endTime - startTime;
        print("Total time playing: {:.1f} seconds".format(round(totalTime, 1)))
        break
    print("AI TURN")
    aiTurn()
    aiWins = checkO()
    print("")
    if aiWins:
        print("AI wins!")
        endTime = time.time()
        totalTime = endTime - startTime;
        print("Total time playing: {:.1f} seconds".format(round(totalTime, 1)))
        break