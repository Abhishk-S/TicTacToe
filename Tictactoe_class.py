# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 00:52:30 2020

@author: abhis
"""

# Board
# Display board
# Choose a position
# Win or tie check
# If none, flip player
# Once a game is over, provide option to replay

import numpy as np

class Board:
    # initialising and displaying the board
    def __init__(self):
        self.board = np.asarray([' ']*9)
    
    def display_board(self):
        print (self.board.reshape(3,3))

        


class Game(Board):

    def __init__(self,player):
        super().__init__()
        self.player = player
        
    def choose_update_cell(self):
        # chooses a position unless the entry is valid and the cell is empty
        selection = True
        while selection:
            position = input('Enter a number between 1-9:')
            while position not in ['1','2','3','4','5','6','7','8','9']:
                position = input('Enter a number between 1-9:')
            position = int(position)
            if self.board[position-1]==' ':
                self.board[position-1] = self.player
                selection = False
            else:
                print ('That position is filled. Try again.')
    
    def change_player(self):

        if self.player == 'X': 
            self.player = 'O'
        else: 
            self.player = 'X'
            
    def AI_0(self):# computer randomly chooses a position
        var = True
        while var:
            cell_number = np.random.randint(1,10)
            if self.board[cell_number-1]==' ':
                self.board[cell_number-1] = self.player
                var = False
    
    def AI_1(self): 
        '''checks if it can win by placing its mark in
        #any of the available positions.  Ifso, it makes the winning move.
        Otherwise, it places its mark on a randomly chosen available position.'''
        keep_searching = True
        board_ = self.board.copy()#creates a copy of board for checking purposes.
        found_cell = False

        for number, cell in enumerate(board_):
            if not found_cell:
                if cell==' ':  #loops through all empty positions in board.
                    board_[number] = self.player
                    if self.AI_checkwins(board_):# checks if win is possible
                        self.board[number] = self.player

                        found_cell = True
                    board_ = self.board.copy() #reverts back to board's 
                    #original position so that it can check for the next 
                    #empty cell and the board doesnot keep getting filled.     
        
        if not found_cell:
            while keep_searching:       
                cell_number = np.random.randint(1,10)
                if self.board[cell_number-1]==' ':
                    self.board[cell_number-1] = self.player

                    keep_searching = False
                    
    def AI_2(self):
        '''checks if it can win by placing its mark in any of the available
        positions.  Ifso, it makes the winning move.  If not, it checks if 
        the opponent can win the game on the next move by placing their mark
        on one of the available positions.  If so, it blocks that position 
        with its own mark.Otherwise, it places its mark on a randomly chosen
        available position.'''
        keep_searching = True
        board_ = self.board.copy()
        found_cell = False

        for number, cell in enumerate(board_): #AI_1
            if not found_cell:
                if cell==' ': 
                    board_[number] = self.player
                    if self.AI_checkwins(board_):
                        self.board[number] = self.player
         
                        found_cell = True
                    board_ = self.board.copy()
                    
        board_ = self.board.copy()
        
        if not found_cell:   #This part blocks the opponent winning move.
            self.change_player() #Changes to opponent
            for number, cell in enumerate(board_): 
                if not found_cell:
                    if cell==' ': 
                        board_[number] = self.player
                        if self.AI_checkwins(board_): #checks for which position
                            #opponent can win
                            self.change_player() #changes back to itself
                            self.board[number] = self.player #..and blocks.
             
                            found_cell = True
                        board_ = self.board.copy()
            
            
            
        if not found_cell:
            self.change_player()
            while keep_searching:       
                cell_number = np.random.randint(1,10)
                if self.board[cell_number-1]==' ':
                    self.board[cell_number-1] = self.player
           
                    keep_searching = False
            
    def AI_checkwins(self,board_):
        
        #Horizontal wins
        for i in [0,3,6]:
            
            if board_[i]==self.player and board_[i+1]==self.player and board_[i+2]==self.player:


                return True
                
        #Vertical wins
        for i in range(3):
            if board_[i]==self.player and board_[i+3]==self.player and board_[i+6]==self.player:

                return True
        #Diagonal wins
        if board_[0]==self.player and board_[4]==self.player and board_[8]==self.player:
    


            return True
        if board_[2]==self.player and board_[4]==self.player and board_[6]==self.player:

            return True
        
        else:  
            return False



    def check_wins(self):
        #Horizontal wins
        for i in [0,3,6]:
            
            if self.board[i]==self.player and self.board[i+1]==self.player and self.board[i+2]==self.player:

                print ('\nGame over. {} wins.\n'.format(self.player))
                return False
                
        #Vertical wins
        for i in range(3):
            if self.board[i]==self.player and self.board[i+3]==self.player and self.board[i+6]==self.player:
    
                
                print ('\nGame over. {} wins.\n'.format(self.player))
                return False
        #Diagonal wins
        if self.board[0]==self.player and self.board[4]==self.player and self.board[8]==self.player:
    
            
            print ('\nGame over. {} wins.\n'.format(self.player))
            return False
        if self.board[2]==self.player and self.board[4]==self.player and self.board[6]==self.player:
    
            
            print ('\nGame over. {} wins.\n'.format(self.player))
            return False
        
        else:  
            return True

    def check_tie(self):

        fill_cells = 0
        if self.check_wins(): # You dont want to print tie when someone wins the moment all the cells fill up.
            for cell in self.board: 
                if cell!= ' ':
                    fill_cells += 1
            if fill_cells ==9: #If all the cells are filled up with no winner in sight, declare tie.
                
                print ('\nIt\'s a tie.\n')
                return False
            else: 
                return True
                
    def game_not_over(self):#checks if there's any wins or ties; if not, then allows game to proceed
        a = self.check_wins()
        b = self.check_tie()
        return (a==True and b==True)
    
    def difficulty_level(self,level):
        
        if level == 'E':
            return self.AI_0()
        elif level == 'M':
            return self.AI_1()
        else:
            return self.AI_2()
    

            
 
#main code
def play_game():
    
    print ('Welcome to Tic-Tac-Toe.')
    diff_level = input('Choose difficulty level- Easy/Medium/Hard(Press E/M/H):')
    board = Board()
    board.display_board()
    not_over = True
    player = np.random.choice(['X','O']) #random choice of X and O.
    print ('You are: {}'.format(player))
    x_pos = Game(player)
    while not_over:
 
        print ('{}\'s turn.'.format(x_pos.player))
        x_pos.choose_update_cell()
        x_pos.display_board()
        not_over = x_pos.game_not_over()
        if not_over:
            x_pos.change_player()
            x_pos.difficulty_level(diff_level)
            x_pos.display_board()
            not_over = x_pos.game_not_over()
            x_pos.change_player()
#code for replay
def replay():
    replay_ = True
    while replay_:
        replay = input('Do you want to play again?(Y/N)').upper()
        if replay == 'Y':
            play_game()
        else:
            replay_ = False
            print ('Go home, loser!')
def main():
    play_game()
    replay()


if __name__ == '__main__': main()

    
    
    
    
