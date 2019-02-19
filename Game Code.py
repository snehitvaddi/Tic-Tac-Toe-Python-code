import os
os.system("cls")

class Board():
    def __init__(self):
        self.cells=["","","","","","","","","",""]

    def display(self):

         print(" {} | {} | {} ".format(self.cells[1],self.cells[2],self.cells[3]))
         print(" {} | {} | {} ".format(self.cells[4],self.cells[5],self.cells[6]))
         print(" {} | {} | {} ".format(self.cells[7],self.cells[8],self.cells[9]))

    def update_cell(self,cell_no,player):
        if self.cells[cell_no]=="":
          self.cells[cell_no]=player
        else:
            print("You lost a chance..Inappropriate seletion")

    def  is_winner(self,player) :
        if(self.cells[1]==player and self.cells[2]==player and self.cells[3]==player) :
            return True
        elif (self.cells[4]==player and self.cells[5]==player and self.cells[6]==player) :
             return True
        elif (self.cells[7]==player and self.cells[8]==player and self.cells[9]==player):
              return True
        elif (self.cells[1]==player and self.cells[5]==player and self.cells[9]==player) :
             return True
        elif (self.cells[3]==player and self.cells[5]==player and self.cells[7]==player) :
             return True
        elif (self.cells[1]==player and self.cells[4]==player and self.cells[7]==player) :
             return True
        elif (self.cells[2]==player and self.cells[5]==player and self.cells[8]==player) :
             return True      
        elif (self.cells[3]==player and self.cells[6]==player and self.cells[9]==player) :
             return True

        else :
            False
    def  reset(self):
       self.cells=["","","","","","","","","",""]
       
board = Board()

def Print_header():
    print("Welcome to Tic Tac Toe")
    
def refresh_screen():
    #Clear the screen
    os.system("cls")

    #Print the Header
    Print_header()

    #show the board
    board.display()

    
while True:  
    refresh_screen()

    #Get X input
    x_choice = int(input("X Please choose 1-9"))

    #Update Board
    board.update_cell(x_choice,"x")
    
    #Refreshing Screen
    refresh_screen()

    # Check for X is winner
    if(board.is_winner("x")):
        print("x wins !!")
        break
      #Get O input
    o_choice = int(input("O Please choose 1-9"))

    #Update Board
    board.update_cell(o_choice,"o")

    #check if O is wiiner
    if(board.is_winner("o")):
         print("\n O wins !!\n")
         break
