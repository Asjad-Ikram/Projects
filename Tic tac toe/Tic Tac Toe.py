#Tic tac toe Game

import random

print("\nWelcome to Tic tac toe\n-------------------")
possibleNumbers=[1,2,3,4,5,6,7,8,9]
gameBoard=[[1,2,3],[4,5,6],[7,8,9]]
result=" "


def GameBoard_Display():
    #Printing rows
    for x in range(3):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(3):
            print("",gameBoard[x][y], end=" |")
    print("\n+---+---+---+")

def modifyArray(num,turn):
    num-=1
    match num:
        case 0:
            gameBoard[0][0]=turn
        case 1:
            gameBoard[0][1]=turn
        case 2:
            gameBoard[0][2]=turn
        case 3:
            gameBoard[1][0]=turn
        case 4:
            gameBoard[1][1]=turn
        case 5:
            gameBoard[1][2]=turn
        case 6:
            gameBoard[2][0]=turn
        case 7:
            gameBoard[2][1]=turn
        case 8:
            gameBoard[2][2]=turn
        

def CheckForWinner(result):   #Checks if any Player has won the game
    
    #All Player Win conditions
    #{
    #Player Wins in rows
    for i in range(3):
        if(gameBoard[i][0]=="X" and gameBoard[i][1]=="X" and gameBoard[i][2]=="X"):
            return "X"
                        

    #Player wins in columns
    for j in range(3):
        if(gameBoard[0][j]=="X" and gameBoard[1][j]=="X" and gameBoard[2][j]=="X"):
            return "X"
            
        #Player CrossWins
    if(gameBoard[0][0]=="X" and gameBoard[1][1]=="X" and gameBoard[2][2]=="X"):
        return "X"
     
    if(gameBoard[0][2]=="X" and gameBoard[1][1]=="X" and gameBoard[2][0]=="X"):
        return "X"
    #}

    #All Cpu Win conditons
    #Wins in rows
    for k in range(3):
        if(gameBoard[k][0]=="O" and gameBoard[k][1]=="O" and gameBoard[k][2]=="O"):
            return "O"
            

    #Wins in columns
    for l in range(3):
        if(gameBoard[0][l]=="O" and gameBoard[1][l]=="O" and gameBoard[2][l]=="O"):
            return "O"
            
    
    #CrossWins
    if(gameBoard[0][0]=="O" and gameBoard[1][1]=="O" and gameBoard[2][2]=="O"):
        return "O"
     
    if(gameBoard[0][2]=="O" and gameBoard[1][1]=="O" and gameBoard[2][0]=="O"):
        return "O"
    
LeaveLoop=False
turnCounter=0

while(LeaveLoop==False):
     #Player turn
    if (turnCounter%2==1) :
        GameBoard_Display()
        numberPicked=int(input("\nChoose a number [1-9]: "))
        if(numberPicked>=1 or numberPicked<=9) and (numberPicked in possibleNumbers):
            modifyArray(numberPicked,"X")
            possibleNumbers.remove(numberPicked)
        else:
            print("Invalid Input")
        
        turnCounter+=1
    
    else:
        while(True):
            cpuChoice=random.choice(possibleNumbers)
            print("\nCpuChoice:")
            if (cpuChoice in possibleNumbers):
                modifyArray(cpuChoice,"O")
                possibleNumbers.remove(cpuChoice)
                turnCounter+=1
                break
    
    Winner=CheckForWinner(result)
    if (Winner=="X"):
        print("Congrats. You have won")
        LeaveLoop=True

    elif(Winner=="O"):
        print("Sorry. You have lost")
        LeaveLoop=True


GameBoard_Display()
