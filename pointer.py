
matrix = [['A'], 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

# Draw the expanded 4x4 grid
def draw():
    print(f" {matrix[0]} |  {matrix[1]}  |  {matrix[2]}  |  {matrix[3]} ")
    print("---+-----+-----+-----")
    print(f" {matrix[4]} |  {matrix[5]}  |  {matrix[6]}  |  {matrix[7]} ")
    print("---+-----+-----+-----")
    print(f" {matrix[8]} |  {matrix[9]}  |  {matrix[10]}  |  {matrix[11]} ")
    print("---+-----+-----+-----")
    print(f" {matrix[12]} |  {matrix[13]}  |  {matrix[14]}  |  {matrix[15]} ")

draw()

def findPointer():
    for i in matrix:
        if type(i) == list:
            return matrix.index(i)
def remPointer():
            loc = findPointer()
            matrix[loc] = matrix[loc][0]
def movert():
    loc = findPointer() + 1
    if loc > len(matrix) - 1:
        loc = loc - len(matrix)
    remPointer()
    matrix[loc] = [matrix[loc]]
def movelt():
    loc = findPointer() - 1
    remPointer()
    matrix[loc] = [matrix[loc]]

def moveup():
    loc = findPointer() - 4
    remPointer()
    matrix[loc] = [matrix[loc]]

def movedwn():
    loc = findPointer() + 4
    if loc > len(matrix) - 4:
        loc = loc - len(matrix)
    remPointer()
    matrix[loc] = [matrix[loc]]

def main():
    while True:
        usin = input("enter intructions (WASD only):")
        if all(char in 'wasdWASD' for char in usin):
            for char in usin:
                if char in 'dD':
                    movert()
                elif char in 'aA':
                    movelt()
                elif char in 'wW':
                    moveup()
                elif char in 'sS':
                    movedwn()
            draw()
main()

