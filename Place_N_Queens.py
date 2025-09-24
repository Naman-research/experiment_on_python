text="----------MY SPICY CHEESE BURGER----------"
width=100
print(f"\n{text:^{width}}")

n=int(input("Enter N: "))

# Board should be a list of lists
board=[["." for _ in range(n)] for _ in range(n)]

# Diagonal arrays should be of length 2*n - 1
main_diagonal=[False for _ in range(2*n-1)]
anti_diagonal=[False for _ in range(2*n-1)]
columns=[False for _ in range(n)]
solutions=[]

def postional_geography(n,row,main_diagonal,anti_diagonal,columns):
    if row==n:
        # Take a snapshot (convert rows back to strings)
        solutions.append(["".join(r) for r in board])
        return

    for i in range(n):
        if columns[i] or main_diagonal[row-i+n-1] or anti_diagonal[row+i]:
            continue

        board[row][i]='Q'
        columns[i]=main_diagonal[row-i+n-1]=anti_diagonal[row+i]=True

        postional_geography(n,row+1,main_diagonal,anti_diagonal,columns)

        board[row][i]='.'
        columns[i]=main_diagonal[row-i+n-1]=anti_diagonal[row+i]=False

postional_geography(n,0,main_diagonal,anti_diagonal,columns)

# Print solutions
for sol in solutions:
    for row in sol:
        print(row)
    print()
