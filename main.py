"""
N-Queens Solution Generator
Ian S. Woodley

This is an expanded version of the classic '8-Queens' problem to
generate a solution for any passed integer. But really, don't try it
with numbers higher than 17. For your CPU's sake.

Note: Some passed integers will have no possible solution. Try in the range
4 <-> 17.

https://en.wikipedia.org/wiki/Eight_queens_puzzle
"""

# Function takes an integer value (n) and returns a 2D list
# containing a valid solution to the n-Queens problem (if possible).
def getSolution(n):
    grid = [ ['_' for _ in range(n)] for _ in range(n) ]
    used = set()

    def sharesRow(x, y):
        for dx, dy in used:
            if y == dy and x != dx:
                return True
        return False
            
    def sharesColumn(x, y):
        for dx, dy in used:
            if x == dx and y != dy:
                return True
        return False

    def sharesDiagonal(x, y):
        for dx, dy in used:
            if abs(x - dx) == abs(y - dy):
                return True
        return False

    def placeQueens(x=0):
        for y in range(n):
            if any( [ sharesRow(x, y), sharesColumn(x, y),
                      sharesDiagonal(x, y) ] ):
                continue
            used.add( (x, y) )
            if x < n - 1 and not placeQueens(x + 1):
                used.remove( (x, y) )
            else:
                return True
        return False

    # Execution
    if not placeQueens():
        return list("Solution not possible.")
    for x, y in used:
        grid[y][x] = 'Q'
    return grid
            
if __name__ == "__main__":
    while True:
        uip = input("Pass a positive integer.")
        if not uip.isdigit():
            print("Invalid input.")
            continue
        
        solution = getSolution(int(uip))
        print(*solution, sep='\n')
        input("\nPress ENTER to exit.")
        break
