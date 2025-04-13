#Created by Sarvamm
#Working Tic-Tac-Toe game using a one dimensional array
import random
cSym = ""
uSym = ""
matrix = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  
avchoices = [0, 1, 2, 3, 4, 5, 6, 7, 8]  #Available position choices for user and computer

#drawing the game
def draw():
    print(f" {matrix[0]} | {matrix[1]} | {matrix[2]} ")
    print("---+---+---")
    print(f" {matrix[3]} | {matrix[4]} | {matrix[5]} ")
    print("---+---+---")
    print(f" {matrix[6]} | {matrix[7]} | {matrix[8]} ")

#user selects his preferred symbol
def XorO():
    global uSym, cSym
    symbol = input("What symbol do you want? (X/O)")
    if symbol in "xX":
        uSym = "X"
        cSym = "O"
    elif symbol in "oO":
        uSym = "O"
        cSym = "X"
    else:
        print("Invalid input!, Let's try that again.")
        XorO()
#Checking win status
def check():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for k in win_conditions:
        if matrix[k[0]] == matrix[k[1]] == matrix[k[2]]:
            if matrix[k[0]] == cSym:
                return "Computer Won"
            elif matrix[k[0]] == uSym:
                return "Player Won"
    
    if " " not in matrix:
        return "Tie"
    
#Try again wihout starting over
def TryAgain():
    ch = input(("Wanna try again? (Y/N)"))
    if ch in "Yy":
        game()

#Start a new game
def PlayAgain():
    global matrix, avchoices
    ch = input(("Wanna play again? (Y/N)"))
    if ch in "Yy":
        matrix = [" ", " ", " ", " ", " ", " ", " ", " ", " "]  
        avchoices = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        game()
    else:
        print("Thanks for Playing")
        matrix = [" ", " ", " ", " ", " ", " ", " ", " ", " "] 
        print("Game Ended")


def checkResult():
    op = check()
    if op == "Player Won":
        draw()
        print("You Won! Congratulations!")
        return True
    elif op == "Computer Won":
        draw()
        print("You Lose!")
        return True
    elif op == "Tie":
        draw()
        print("Game Tied.")
        return True
    else:
        return False   
#Main 
print("Tic-Tac-Toe by Sarvamm")    
XorO()
def game():
    global matrix, avchoices
    while len(avchoices) > 0:
        draw()

        #Player's Turn
        try:
            userCh = int(input("Enter position where you want to insert symbol (0-8)"))
            if userCh in avchoices: 
                matrix[userCh] = uSym
                avchoices.remove(userCh)
                if checkResult():
                    PlayAgain()
                    break

        #Computer's Turn
                comCh = random.choice(avchoices)
                matrix[comCh] = cSym
                avchoices.remove(comCh)
                if checkResult():
                    PlayAgain()
                    break
            else:
                print("Inavlid input! your available choices are:\n", avchoices)
                TryAgain()
                break 
        except ValueError:
            print("Inavlid input! your available choices are:\n", avchoices)
            TryAgain()     
game() #Starting game