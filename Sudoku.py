# Set up ones to solve
EASY = [0,0,1,0,0,0,9,0,0
       ,0,6,9,7,2,0,1,4,0
       ,3,0,5,9,8,0,7,2,0
       ,6,0,8,4,7,2,0,0,3
       ,0,2,3,0,9,0,4,0,7
       ,4,0,0,0,0,5,8,6,0
       ,7,0,0,3,0,0,0,0,4
       ,0,3,6,8,5,4,2,0,0
       ,1,0,0,2,6,7,3,5,0
       ]

EASYT= [2,7,1,0,0,0,9,0,0
       ,8,6,9,7,2,0,1,4,0
       ,3,0,5,9,8,0,7,2,0
       ,6,0,8,4,7,2,0,0,3
       ,0,2,3,0,9,0,4,0,7
       ,4,0,0,0,0,5,8,6,0
       ,7,0,0,3,0,0,0,0,4
       ,0,3,6,8,5,4,2,0,0
       ,1,0,0,2,6,7,3,5,0
       ]

MED  = [5,6,1,3,0,0,0,0,2
       ,0,3,0,5,9,6,0,1,0
       ,0,7,0,0,0,2,3,0,0
       ,0,5,9,0,6,0,0,0,0
       ,6,8,0,0,0,5,0,3,1
       ,0,0,4,0,0,9,0,0,0
       ,0,0,3,6,1,0,0,0,7
       ,0,0,6,0,5,0,2,0,3
       ,7,0,0,0,0,0,1,0,0
       ]

HARD = [0,0,0,0,0,0,0,2,6
       ,0,0,0,7,0,9,0,0,0
       ,0,2,0,1,0,0,0,0,0
       ,0,0,6,0,9,0,2,0,4
       ,0,0,0,0,7,0,9,0,0
       ,0,0,9,0,0,0,0,5,0
       ,6,0,1,3,0,7,0,0,2
       ,4,0,0,2,6,1,8,7,0
       ,2,3,0,0,0,5,6,0,0
       ]

EXPT = [0,0,0,0,0,5,7,9,0
       ,0,0,0,8,0,0,0,0,6
       ,0,0,5,6,0,9,4,0,3
       ,4,0,0,0,0,3,9,0,0
       ,0,9,0,0,0,0,2,1,0
       ,0,8,0,0,9,4,3,0,0
       ,0,5,0,0,0,1,0,7,0
       ,3,0,8,0,0,2,1,4,0
       ,0,2,0,9,0,0,6,0,5
       ]

Vhrd = [0,0,7,0,0,0,0,5,0
       ,0,0,0,0,0,0,0,0,0
       ,0,1,0,6,0,0,0,0,4
       ,5,9,0,0,0,2,0,0,0
       ,0,3,0,4,7,0,0,0,0
       ,0,6,0,0,3,0,9,0,0
       ,8,0,0,0,0,5,0,0,2
       ,0,0,0,0,0,0,0,8,0
       ,2,0,0,0,0,1,0,4,7
       ]

diff = [0,0,0,0,0,0,0,3,2
       ,3,6,0,0,0,0,0,0,0
       ,0,0,0,0,0,0,5,0,8
       ,8,7,0,0,0,0,0,0,0
       ,0,9,0,0,0,3,0,4,0
       ,6,0,0,8,0,0,0,0,0
       ,0,0,0,0,0,2,0,0,3
       ,5,0,1,6,3,0,4,0,0
       ,0,3,9,1,4,8,7,5,6]

evil = [0,0,0,0,0,0,0,0,0
       ,0,0,0,0,0,0,5,2,3
       ,0,0,0,0,0,0,0,1,8
       ,0,0,0,0,0,0,0,0,0
       ,0,0,9,0,7,4,0,6,0
       ,0,0,4,6,1,0,0,0,7
       ,0,5,8,0,4,3,0,0,0
       ,0,4,0,0,2,0,0,3,0
       ,0,6,7,0,8,1,0,9,4]

circle =    "⓪①②③④⑤⑥⑦⑧⑨"
sub =       "₀₁₂₃₄₅₆₇₈₉"
nums =      "0123456789"

def concat(arrarr):
    out = []
    for arr in arrarr:
        out += arr
    return out

def findIn2d(arr,item):
    for i, c in enumerate(arr):
        if item in c:
            return i
    raise Exception("Item not found")

def knit(arr1,arr2):
    return [arr1[i]+arr2[i] for i,c in enumerate(arr1)]

class Sudoku:

    def __init__(self, board):
        self.board = board
        self.boardNote = [[]]*9*9
        #self.boardNotePP = [[1,2,3,4,5,6,7,8,9]]*9*9
        self.printBreak = "──────┼──────┼──────\n"
        self.Gdepth = 0

    def getRows(self,board):
        return [board[i*9:i*9+9] for i in range(0,9)]

    def getCols(self,board):
        a = self.getRows(board)
        return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

    def getSquares(self,board):
        a = self.getCols(board)
        out = []
        for x1 in range(0,3):
            for y1 in range(0,3):
                hold = []
                for x2 in range(0,3):
                    for y2 in range(0,3):
                        hold.append(a[y1*3+y2][x1*3+x2])
                out.append(hold)
        return out

    def validChunk(self,chunk):
        for i in range(1,10):
            if chunk.count(i) > 1:
                return False
        return True

    def validSet(self,sect):
        for chunk in sect:
            if not self.validChunk(chunk):
                return False
        return True

    def validChunkZ(self,chunk):
        for i in range(1,10):
            if chunk.count(i) == 0:
                return False
        return True

    def validSetZ(self,sect):
        for chunk in sect:
            if not self.validChunkZ(chunk):
                return False
        return True
    
    def valid(self,depth=0):
        if not self.validSet(self.getSquares(self.board)):
            return False
        if not self.validSet(self.getCols(self.board)):
            return False
        if not self.validSet(self.getRows(self.board)):
            return False
        if(depth > 0):
            self.guessPass(depth=depth-1)
            if not self.validSetZ(knit([concat(x) for x in self.getSquares(self.boardNote)],self.getSquares(self.board))):
                return False
            if not self.validSetZ(knit([concat(x) for x in self.getCols(self.boardNote)],self.getCols(self.board))):
                return False
            if not self.validSetZ(knit([concat(x) for x in self.getRows(self.boardNote)],self.getRows(self.board))):
                return False
            else:
                return True
        return True

    def valid2(self,depth=0):
        if not self.validSet(self.getSquares(self.board)):
            return False
        elif not self.validSet(self.getCols(self.board)):
            return False
        elif not self.validSet(self.getRows(self.board)):
            return False
        else:
            if(depth > 0):
                self.guessPass(depth=depth-1)
                if not self.validSetZ(knit([concat(x) for x in self.getSquares(self.boardNote)],self.getSquares(self.board))):
                    return False
                elif not self.validSetZ(knit([concat(x) for x in self.getCols(self.boardNote)],self.getCols(self.board))):
                    return False
                elif not self.validSetZ(knit([concat(x) for x in self.getRows(self.boardNote)],self.getRows(self.board))):
                    return False
                else:
                    return True
            else:
                return True

    def changeSquare(self,num,pos):
        a = self.board[:]
        a[pos] = num
        return Sudoku(a)

    def get(self,pos):
        return self.board[pos]

    def guess(self,num,pos,depth=0):
        return self.changeSquare(num,pos).valid(depth=depth)

    def guessPass(self,depth=0):
        for i in range(0,len(self.board)):
            if self.get(i) == 0:
                #self.boardNote[i] = [x for x in self.boardNotePP[i] if self.guess(x,i,depth=depth)]
                self.boardNote[i] = [x for x in range(1,10) if self.guess(x,i,depth=depth)]
            else:
                self.boardNote[i] = []
                #print("-",end="",flush=True)
        #print(self.boardNote)
        print(".",end="",flush=True)

    def singleNumberPass(self):
        for i,c in enumerate(self.boardNote):
            if len(c) == 1:
                self.board[i] = c[0]
                self.boardNote[i] = []

    def singleChunk(self,chunk,chunkpos):
        chunkr = concat(chunk)
        for i in range(1,10):
            if chunkr.count(i) == 1:
                self.board[chunkpos[findIn2d(chunk,i)]] = i
                self.boardNote[chunkpos[findIn2d(chunk,i)]] = []

    def singleChunkPass(self):
        for i,c in enumerate(self.getRows(self.boardNote)):
            self.singleChunk(c,[x+i*9 for x in range(len(c))])
        self.guessPass(depth=self.Gdepth)
        for i,c in enumerate(self.getCols(self.boardNote)):
            self.singleChunk(c,[x*9+i for x in range(len(c))])
        self.guessPass(depth=self.Gdepth)
        for i,c in enumerate(self.getSquares(self.boardNote)):
            self.singleChunk(c,self.getSquares(range(0,82))[i])

    def rulePass(self):
        print("\nPASS AT DEPTH:", self.Gdepth)
        #self.boardNotePP = self.boardNote[:]
        self.guessPass(depth=self.Gdepth)
        self.singleNumberPass()
        self.guessPass(depth=self.Gdepth)
        self.singleChunkPass()
    
    def solved(self):
        return self.boardNote == [[]]*9*9 and self.valid()

    def solve(self):
        before = []
        after = [0]
        done = False
        #self.guessPass()
        #self.boardNotePP = self.boardNote[:]
        #print(self.boardNotePP)
        while not done:
            if before != after:
                self.Gdepth = 0
                before = self.board[:]
                print(self)
                self.rulePass()
                after = self.board[:]
            print("Solved:",self.solved())
            if not self.solved():
                self.boardBefore = [[]]*9*9
                self.boardAfter = [[1]]*9*9
                self.Gdepth += 1
                self.rulePass()
            else:
                done = True

        print("Done!")
        print(self)
        print(self.boardNote)
        print(self.board)
        return self.solved()


    def printPars(self,sect):
        out = ""
        for i in sect:
            if i == 0:
                out += "  "
            else:
                out += nums[i]+" "
        return out

    def printRow(self,row):
        return self.printPars(row[0:3])+"│"+self.printPars(row[3:6])+"│"+self.printPars(row[6:9]) + "\n"

    def __str__(self):
        out = "\n"
        rows = self.getRows(self.board)
        out += self.printRow(rows[0])
        out += self.printRow(rows[1])
        out += self.printRow(rows[2])
        out += self.printBreak
        out += self.printRow(rows[3])
        out += self.printRow(rows[4])
        out += self.printRow(rows[5])
        out += self.printBreak
        out += self.printRow(rows[6])
        out += self.printRow(rows[7])
        out += self.printRow(rows[8])
        return out

hds = [0,0,2,3,9,0,8,0,6
      ,0,0,0,1,0,0,0,2,0
      ,6,0,0,0,0,2,0,1,7
      ,2,9,0,0,0,0,0,0,1
      ,1,0,0,0,0,6,0,4,5
      ,0,0,7,0,1,0,2,0,0
      ,9,0,0,0,0,5,1,7,0
      ,0,4,1,0,3,0,5,0,0
      ,8,0,3,6,7,0,0,0,0
      ]

escagot = [8,0,0,0,0,0,0,0,0
          ,0,0,3,6,0,0,0,0,0
          ,0,7,0,0,9,0,2,0,0
          ,0,5,0,0,0,7,0,0,0
          ,0,0,0,0,4,5,7,0,0
          ,0,0,0,1,0,0,0,3,0
          ,0,0,1,0,0,0,0,6,8
          ,0,0,8,5,0,0,0,1,0
          ,0,9,0,0,0,0,4,0,0
          ]

a = Sudoku(escagot)
print(a)
print(a.solve())
