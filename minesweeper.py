import os
import random

print("\n----Welcome to Minesweeper by Tri Huynh----\n")
SIZE = int(input("Enter your board size from 2-9: "))
while SIZE >= 10 or SIZE < 2:
	SIZE = SIZE = int(input("Please select from 2-9: "))

board = [[0 for i in range(0, SIZE)] for j in range(SIZE)]
displayBoard = [["-" for i in range(0, SIZE)] for j in range(SIZE)]
gameStatus = True


def checkAndUpdate(row, col):
	totalOpened = 0
	if displayBoard[row][col] == "-":
		numMines = checkMines(row,col)
		displayBoard[row][col] = numMines
		totalOpened = totalOpened+1
		if numMines == 0:
			topRow = row - 1
			while topRow <= row+1:
				if topRow >= 0 and topRow<SIZE:
					leftCol = col - 1
					while leftCol <= col + 1:
						if leftCol >= 0 and leftCol<SIZE:
							totalOpened += checkAndUpdate(topRow, leftCol)
						leftCol = leftCol + 1
				topRow = topRow + 1			
	return totalOpened

def checkMines(row, col):
	total = 0
	topRow = row - 1
	while topRow <= row+1:
		if topRow >= 0 and topRow<SIZE:
			leftCol = col - 1
			while leftCol <= col + 1:
				if leftCol >= 0 and leftCol<SIZE:
					total= total+board[topRow][leftCol]
				leftCol = leftCol + 1
		topRow = topRow + 1
	return total

def printGameBoard(o):
	os.system("cls|| clear")
	for i in range(SIZE):
		print("\n"+" "+"|-C-"*SIZE+"|")
		print("R|", end="")
		for j in range(SIZE):
			print("", displayBoard[i][j], end=" |")
	print("\n"+" "+"|-C-"*SIZE+"|")

def printResult(o):
	os.system("cls|| clear")
	for i in range(SIZE):
		print("\n"+" "+"|-C-"*SIZE+"|")
		print("R|", end="")
		for j in range(SIZE):
			print("", board[i][j], end=" |")
	print("\n"+" "+"|-C-"*SIZE+"|")



#add mines
numMines = int(input("How many mines? "))
while numMines >= SIZE*SIZE:
	numMines = int(input(f"Your board size is {SIZE}*{SIZE} equal or bigger is impossible: "))
nums = 0
while nums < numMines:
	row = random.randint(0,SIZE-1)
	col = random.randint(0,SIZE-1)
	if board[row][col] == 0:
		board[row][col] = 1
	nums += 1


def userChoose():
	global gameStatus
	r = int(input(f"Please select Row 1 - {SIZE}: "))-1
	while r >= SIZE or r == -1:
		r = int(input("Invalided Row: "))-1
	c = int(input(f"Please select Columns 1 to {SIZE}: "))-1
	while c >= SIZE or c == -1:
		c = int(input("Invalided Columns: "))-1
	if board[r][c] == 1:
		printResult(board)
		print("\nGame Over! You hit a mine.")
		gameStatus = False
	else:
		displayBoard[r][c] = checkAndUpdate(r,c)
		printGameBoard(board)

while gameStatus:
	printGameBoard(displayBoard)
	userChoose()
