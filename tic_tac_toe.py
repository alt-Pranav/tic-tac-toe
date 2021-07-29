# COMPLETE!

# Written By Pranav Bhagwat
# Date: 28-07-2021

# class that contains all functions needed to play tic-tac-toe between 2 humans 
class play_ttt:

    # ALL CLASS ATTRIBUTES

    # stores the 3x3 grid state
    moves = [["","",""],["","",""],["","",""]]

    # used to display grid locations only once at the start of the game
    count = 0

    # dict that maps grid location to its matrix indices
    locations = {}

    # stores number of moves played
    move_count = 0

    # stores all used locations to prevent overwriting
    used_loc = []

    # stores the symbol chosen by player 1 and 2
    p1,p2="",""

    # ALL CLASS BEHAVIOURS

    # players choose their respective symbols
    def choosePlayers(self):
        self.p1 = input("Enter Player 1 input: X or O = ")
        self.p2 = input("Enter Player 2 input: X or O = ")

    # maps grid locations to its matrix indices
    def map_locations(self):
        k=0
        for i in range(0,3):
            for j in range(0,3):
                self.locations[k] = [i,j]
                k +=1
    

    def add_turn(self):
        
        # loops till valid location is entered
        while(True):
            # takes where to input X or O
            p = (int)(input("Enter current player grid location = "))

            # checks if location is empty
            if(p not in self.used_loc):
                # if player 2 played last then player 1 symbol is added to location
                if self.move_count % 2 == 0 :
                    self.moves[self.locations[p][0]][self.locations[p][1]] = self.p1

                # if player 1 played last then player 2 symbol is added to location
                else:
                    self.moves[self.locations[p][0]][self.locations[p][1]] = self.p2
    
                # updates the moves performed
                self.move_count +=1
                break
            else:
                print("Please choose an unused location")
        
        # shows new state of the grid
        print("New State: ")
        self.showGrid()

        #adds new location to list
        self.used_loc.append(p)


    # checks if either player has won the game, where c stores the player's symbol
    def checkWinner(self):

        won = False
        for i in range(0,3):
            
            # checks if each row is non-empty, then checks for winning condition
            # c stores non-"" count for each row
            c = 0
            for j in range(0,3):
                if "" != self.moves[i][j]:
                    c +=1

            if c == 3:
                if self.p2 == self.moves[i][j-1] and self.p2 == self.moves[i][j-2] and self.p2 == self.moves[i][j-3]:
                    print("Player 2 won!")
                    won = True
                elif self.p1 == self.moves[i][j-1] and self.p1 == self.moves[i][j-2] and self.p1 == self.moves[i][j-3]:
                    print("Player 1 won!")
                    won = True

            # checks if each column is non-empty, then checks for winning condition
            # c stores non-"" count for each column
            c = 0
            for j in range(0,3):
                if "" != self.moves[j][i]:
                    c +=1
            
            if c == 3:
                if self.p2 == self.moves[j-1][i] and self.p2 == self.moves[j-2][i] and self.p2 == self.moves[j-3][i]:
                    print("Player 2 won!")
                    won = True
                elif self.p1 == self.moves[j-1][i] and self.p1 == self.moves[j-2][i] and self.p1 == self.moves[j-3][i]:
                    print("Player 1 won!")
                    won = True

        # checks for diagonal win
        # c stores non-"" for each diagonal element
        c = 0
        # left diagonal
        for a in range(0,3):
            for b in range(0,3):
                if a == b:
                    if "" != self.moves[a][b]:
                        c +=1
        
        if c==3:
            if self.p2 == self.moves[0][0] and self.p2 == self.moves[1][1] and self.p2 == self.moves[2][2]:
                print("Player 2 won!")
                won = True
            elif self.p1 == self.moves[0][0] and self.p1 == self.moves[1][1] and self.p1 == self.moves[2][2]:
                print("Player 1 won!")
                won = True

        c = 0
        # right diagonal
        for a in range(0,3):
            for b in range(2,-1,-1):
                if (a+b) == 2:              
                    if "" != self.moves[a][b]:
                        c +=1
        
        if c==3:
            if self.p2 == self.moves[0][2] and self.p2 == self.moves[1][1] and self.p2 == self.moves[2][0]:
                print("Player 2 won!")
                won = True
            elif self.p1 == self.moves[0][2] and self.p1 == self.moves[1][1] and self.p1 == self.moves[2][0]:
                print("Player 1 won!")
                won = True

        if won:
            print("Thank you for playing! :)")

            # terminates the game 
            exit()
                    
        
    # starts the game
    def play(self):
        print("Game has started")

        # players choose their respective symbols
        self.choosePlayers()

        # adds turns till all locations are filled
        while(self.move_count < 9):
            self.add_turn()
            self.checkWinner()

        # if no winner then the following will execute
        print("Thank you for playing! :)")

        # terminates the game 
        exit()


    # shows initial grid and grid after each move
    def showGrid(self):
        # shows grid locations at the start and doesn't execute again
        if self.count == 0:
            print("Grid locations are as follows: ")
            k=0
            for i in range(0,3):
                for j in range(0,3):
                    print(k, end =" ")
                    k +=1
                print()
            self.count = 1

        # shows grid after each move
        else:
            for i in range(0,3):
                for j in range(0,3):
                    print(self.moves[i][j], end=" ")
                print()

        print()

# object to access tic-tac-toe methods
player = play_ttt()

# maps grid locations to its matrix indices
player.map_locations()

# shows initial grid and grid after each move
player.showGrid()

# starts the game
player.play()


