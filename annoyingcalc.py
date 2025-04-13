import random
matrix = ['%', '/', '*', 'C', '7←', '8', '9', '-', '4', '5', '6', '+', '1', '2', '3', '=','0','00','000']
sym = "←"
result = "" 
userinput = ""
def display_controls():
    print("=== Calculator Controls ===")
    print("Navigation:")
    print("W - Move Up")
    print("A - Move Left")
    print("S - Move Down")
    print("D - Move Right")
    print("E - Select Current Symbol")
    print("C - Clear Input")
    print("Q - Quit")
    print("H - to show controls")
    print("============================")
display_controls()
def draw():
    global userinput, result
    l = len(userinput)
    r = len(str(result))
    
    print(" " + "-"*l + "-"*(16-l))
    print("|", userinput + " "*(15-l) + "|")
    print(" " + "-"*l + "-"*(16-l))
    print(" "*(15-r) + "= " + str(result))
    print("-----------------") 
    print(" ",
        matrix[0] + ((2 - len(matrix[0])) * " "), "|",
        matrix[1] + ((2 - len(matrix[1])) * " "), "|",
        matrix[2] + ((2 - len(matrix[2])) * " "), "|",
        matrix[3] + ((2 - len(matrix[3])) * " ")
    )
    print("-----+----+----+---")
    print(" ",matrix[4]+ ((2 - len(matrix[4])) * " "), "|", matrix[5]+ ((2 - len(matrix[5])) * " "), "|",
           matrix[6]+ ((2 - len(matrix[6])) * " "), "|", matrix[7])
    print("-----+----+----+---")
    print(" ",matrix[8]+ ((2 - len(matrix[8])) * " "), "|", matrix[9]+ ((2 - len(matrix[9])) * " "), "|",
           matrix[10]+ ((2 - len(matrix[10])) * " "), "|", matrix[11])
    print("-----+----+----+---")
    print(" ",matrix[12]+ ((2 - len(matrix[12])) * " "), "|", matrix[13]+ ((2 - len(matrix[13])) * " "),
           "|", matrix[14]+ ((2 - len(matrix[14])) * " "), "|", matrix[15])
    print("-----+----+----+---")
    print(" ",matrix[16]+ ((2 - len(matrix[16])) * " "), "|", matrix[17]+ ((2 - len(matrix[17])) * " "), "|",
           matrix[18])
    

draw()

def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error (division by zero)"
    except Exception:
        return "Error (invalid input)"

def findPointer():
    for i in matrix:
        if i[-1] == sym:
            return matrix.index(i)
def remPointer():
            loc = findPointer()
            matrix[loc] = matrix[loc].rstrip(sym)
def movert():
    loc = findPointer() + 1
    if loc > len(matrix) - 1:
        loc = loc - len(matrix)
    remPointer()
    matrix[loc] = matrix[loc] +sym
def movelt():
    loc = findPointer() - 1
    remPointer()
    matrix[loc] = matrix[loc] + sym

def moveup():
    loc = findPointer() - 4
    remPointer()
    matrix[loc] = matrix[loc]+ sym

def movedwn():
    loc = findPointer() + 4
    if loc > len(matrix) - 4:
        loc = loc - len(matrix)
    remPointer()
    matrix[loc] = matrix[loc] + sym

def main():
    global userinput, result

    while True:
        usin = input("enter intructions (WASD only):")
        if all(char in 'wasdWASDeEqQhH' for char in usin):
            for char in usin:
                if char in 'qQ':
                    return
                elif char in 'hH':
                    display_controls()
                elif char in 'dD':
                    movert()
                elif char in 'aA':
                    movelt()
                elif char in 'wW':
                    moveup()
                elif char in 'sS':
                    movedwn()
                elif char in 'eE':
                    if matrix[findPointer()][0] == "=":
                        result = calculate(userinput)
                        userinput = str(result)
                    elif matrix[findPointer()][0] == "C":
                        userinput = ""
                        result = ""
                    else:
                        userinput = str(userinput) + matrix[findPointer()].rstrip(sym)
            draw()
            if result in ["Error (division by zero)", "Error (invalid input)"] or type(result) == bool:
                userinput = ""
                result = ""
        else:
            print("Invalid input!")
            main()
main()
