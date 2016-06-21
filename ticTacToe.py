import random #import random module 
	
grid = [[0, 1, 2], #create tic tac toe 2D list
		[3, 4, 5],
		[6, 7, 8]] 
			
def init_board(grid): #turn the grid into a board 
	''' prints a numbered tic tac toe board  '''
	for row in grid: 
		print("-------------")  

		line = "| " # Represents one row 
		for item in row: 
			line += str(item) + ' | ' #break up each cell
		print(line) 
	print("-------------")

def int_input(prompt): #to make sure the user does not try to enter an invalid cell number #will use in next function 
	'''Accepts a prompt for the user as a string. Returns answer as an integer. Allows user to try again. '''
	answer = raw_input(prompt)
	try:
		return int(answer)
	except ValueError:
		return int_input("Not a cell try again: ") 

def is_input_open(space,grid):
	'''Checks to see if the cell the user wishes to occupy is open and then enter the character if it is open'''
	
	open = [] #make open space list 
	
	for row in grid: #for each row in the grid, and for each item 
		for item in row:
			if item != p1Char or item != p2Char or item != p3Char: #add to open list if the cell is not occupied
				open.append(item)
	
	intNotConverted = True 
	
	while intNotConverted: #until 
		try: #try and except block, see if their input is even a number / a possible space on the grid
			space = int(space)
		except ValueError:
			space = int_input("Sorry, that is not a cell, Try again: ")
		else:
			intNotConverted = False	
	
	if int(space) in open: #if the cell they entered is contained in the open space list, return the space
		return space
	else:
		while space not in open: #if space is not open
			space = int_input("Sorry, that cell is not available: Try again:  ") #allows user to input another number 
	
	return space

def place_symbol(symbol, space): 
	'''Places the player's symbol on the grid'''

	rowCoord = int(space) // (len(grid)) #find the row coordinate
	itemCoord = int(space) % (len(grid)) #find the item coordinate
	
	
	grid[rowCoord][itemCoord] = symbol #replace the grid number with symbol
	return init_board(grid) #return the new grid!
	
def check_winner(grid): 
	'''will check the grid to see if any player has three in a row (diagonals, rows, and columns)'''
	
	winner = "no winner" #set automatically to no winner 
	
	if grid[0][0] == grid[1][1] == grid[2][2]: #check all diagonals 
		if grid[0][0] == p1Char:
			winner = "Player 1" #change for each player if they win
		if grid[0][0] == p2Char:
			winner = "Player 2"
		if grid[0][0] == p3Char:
			winner = "Player 3"
	if grid[2][0] == grid[1][1] == grid[0][2]:
		if grid[2][0] == p1Char:
			winner = "Player 1"
		if grid[2][0] == p2Char:
			winner = "Player 2"
		if grid[2][0] == p3Char:
			winner = "Player 3"
			
	row = 0  #checks the rows 
	while row < len(grid):	
		if grid[row][0] == grid[row][1] == grid[row][2]:
			if grid[row][0] == p1Char:
				winner = "Player 1"
			if grid[row][0] == p2Char:
				winner = "Player 2"
			if grid[row][0] == p3Char:
				winner = "Player 3"
		row +=1 	
	column = 0	
	
	while column < len(grid): #checks the columns
		if grid[0][column] == grid[1][column] == grid[2][column]:
			if grid[0][column] == p1Char:
				winner = "Player 1"
			if grid[0][column] == p2Char:
				winner = "Player 2"
			if grid[0][column] == p3Char:
				winner = "Player 3"
		column += 1
			
	
	return winner  #return the value of winner

def take_turn(player):
	'''takes in which player's turn it is, and places their symbol accordingly'''
	
	if player == 0:
		space = raw_input("\033[94m" + "Player 1, " + "\033[0m" + "choose a box: ") #makes colorful :)
		place_symbol(p1Char, is_input_open(space,grid)) #placing symbol once program confirms whether the space is open
	
	if player == 1:
		space = raw_input("\033[92m" + "Player 2, " + "\033[0m" + "choose a box: ") 
		place_symbol(p2Char, is_input_open(space,grid))

	if player == 2:
		space = raw_input( "\033[31m" + "Player 3, " + "\033[0m" + "choose a box: ") 
		place_symbol(p3Char, is_input_open(space,grid))
		
	
	
########### Main Program ##########

print ("Welcome to the \"Tic-Tac-Toe\" game")

wantThird = raw_input("Would you like a third player? ('Y' for yes, other character for no) :  ") #third player option

p1Char = raw_input("Player 1, please enter your character: ") 
while p1Char == "": #don't want blank symbols!
	p1Char = raw_input("You didn't enter a character! Try again: ") 	

p2Char = raw_input("Player 2, please enter your character: ") 
while p2Char == "" or p2Char == p1Char: #make sure the players don't use the same character
	p2Char = raw_input("Not valid. Try again: ") 
	
if wantThird == "Y":
	p3Char = raw_input("Player 3, please enter your character: ") 
	while p3Char == "" or p3Char == p1Char or p3Char == p2Char:
		p3Char = raw_input("Not valid. Try again: ") 
	p3Char = "\033[31m"+p3Char+"\033[0m"
else:
	p3Char = False #only set p3Char to a character if user responded Y to 3 player question

p1Char = "\033[94m"+p1Char+"\033[0m"	#make the characters colorful :D 
p2Char =  "\033[92m"+p2Char+"\033[0m"
	
init_board(grid)  #print 

gameWon = "no winner" #set game won to no winner at first

if wantThird == "Y": #3 options 
	list = [0,1,2]  #make a list of 3 possible ints
	random.shuffle(list,random.random) #shuffle order of the list randomly 
	print ("Random Order: Player {} will be starting first, Player {} will be second, and Player {} will be last.").format(list[0] +1 ,list[1] + 1,list[2] + 1)
else:
	list = [0,1] #make a list of 2 possible ints
	random.shuffle(list,random.random)
	print ("Random Order: Player {} will be starting first and Player {} will be second." ).format(list[0] +1 ,list[1] + 1)


players = 0 #start at 0, (the beginning of the list of ints)
moves = 0 #(set moves to 0)

while gameWon == "no winner" and moves < 9: #will loop until a winner was found, 

	if wantThird == "Y": #for 3 players
		take_turn(list[players % 3]) #will cycle through the order of the player list #will start at 0%3 (0), then go to 1%3 (1), then go to (2) and back to 0 (will cycle)
	else:
		take_turn(list[players % 2]) #for 2 players
	moves += 1	 #increment moves and player
	players += 1 
	gameWon = check_winner(grid) #always check to see if a winner was found after each player goes

if gameWon != "no winner":
	print ("Congrats, {} won.".format(check_winner(grid))) #print which player was the winner
	
if moves == 9 and gameWon == "no winner": #if all moves used up, and no winner 
	print ("Oops. Looks like it was a tie.") #print it was a tie
	

