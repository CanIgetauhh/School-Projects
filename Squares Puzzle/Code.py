#How many squares in a larger square containing a grid with a length and width of x
x = int(input("What are the side lengths of the square?\n"))
squares = 0
for i in range(x + 1) : squares = squares + i**2
print("The amount of smaller squares in side that square is " + str(squares) + " squares.")
