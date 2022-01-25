class OddEvenTTT:
    def __init__(self):
        self.board = []
        self.size = 3
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        print("")
        print("    0   1   2 ")
        print("")
        print(("0   {b1} | {b2} | {b3} ").format(b1=self.board[0][0], b2=self.board[0][1], b3=self.board[0][2]))
        print("   -----------")
        print(("1   {b4} | {b5} | {b6} ").format(b4=self.board[1][0], b5=self.board[1][1], b6=self.board[1][2]))
        print("   -----------")
        print(("2   {b7} | {b8} | {b9} ").format(b7=self.board[2][0], b8=self.board[2][1], b9=self.board[2][2]))
        print("")


    def squareEmpty(self, row, col):
        if self.board[row][col] == 0:
            return True
        else:
            return False
    
    
    def place(self, row, col, num):
        if self.squareEmpty(row,col):
            self.board[row][col] = num
            return True
        else:
            return False
    
    
    def isFull(self):
        check = True
        for i in self.board:
            for j in i:
                if j == 0:
                    check = False
        return check
        
           
    def isWinner(self):
        check = False
        for i in self.board:
            if sum(i) == 15:
                check = True
        for i in range(3):
            if self.board[0][i]+self.board[1][i]+self.board[2][i] == 15:
                check = True
        if self.board[0][0]+self.board[1][1]+self.board[2][2] == 15:
                check = True
        if self.board[0][2]+self.board[1][1]+self.board[2][0] == 15:
                check = True
        return check


def getEntry(player, entries):
    if player % 2 == 0:
        numDescription = 'even'
        lower = 2
        upper = 8        
    else:
        numDescription = 'odd'
        lower = 1
        upper = 9
    entry = int(input('Player {}, please enter an {} number between {} and {}): '.format(player, numDescription, lower, upper)))
    return entry


def getLoc(player, element):
    index = int(input('Player ' + str(player) + ', please enter a ' + element +': '))
    return index


def gameOver(myBoard, player):
    if myBoard.isWinner():
        myBoard.drawBoard()
        print ('Player', player, "wins.")           
        return True
    elif myBoard.isFull():
        myBoard.drawBoard()
        print ("Tie.")        
        return True
    return False


def playAgain():
    playAgain = ' ' 
    while playAgain[0].upper() not in ['Y', 'N']:
        playAgain = input("Do you want to play another game? (Y/N): ")
    return playAgain[0].upper() == "Y"   


def main():
    newGame = True
    while newGame:
        TITLE = "Starting a new Odd Even Tic Tac Toe game"
        print("-" * len(TITLE))
        print (TITLE)
        print("-" * len(TITLE))
        myBoard = OddEvenTTT()
        gOver = False
        round = 0
        entries = []
        while not gOver:
            myBoard.drawBoard()
            entry = getEntry(round + 1, entries)
            row = getLoc(round + 1, 'row')
            col = getLoc(round + 1, 'column')
            if myBoard.place(row, col, entry):
                entries.append(entry)
                gOver = gameOver(myBoard, round + 1)
                round = (round + 1) % 2                
            else:
                print('Error: Can\'t make move!')
        newGame = playAgain()
    print('Thanks for playing! Goodbye.')
            
if __name__ == '__main__':
    main()

    