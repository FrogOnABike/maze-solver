import time
import random
from cell import Cell
from classes import *


class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        if seed != None:
            random.seed(seed)
        # else:
        #     self.__seed = None
        self.__create_cells()
        # By breaking walls first and then drawing entrance and exit, it works nicer with my logic for ensuring all perimeter cells outside walls are in place
        self.__break_walls_r(0,0)
        self.__break_entrance_and_exit()
        self.__reset_cells_visited()
        
        
    def __create_cells(self):
        for x in range(self.__num_cols):
            row = []
            for y in range(self.__num_rows):
                row.append(Cell(self.__win))
            self.__cells.append(row)
        if self.__win != None:
            for x,xv in enumerate(self.__cells):
                for y,yv in enumerate(self.__cells[x]):
                    self.__draw_cell(x+1,y+1)
                
    def __draw_cell(self,i,j):
        x1 = self.__x1 + (i-1)*self.__cell_size_x
        y1 = self.__y1 + (j-1)*self.__cell_size_y
        p1 = Point(x1,y1)
        x2 = self.__x1 + (i)*self.__cell_size_x
        y2 = self.__y1 + (j)*self.__cell_size_y
        p2 = Point(x2,y2)
        self.__cells[i-1][j-1].draw(p1,p2)
        self.__animate()
    
    def __animate(self):
        self.__win.redraw()
        time.sleep(0.02)
        
    def __break_entrance_and_exit(self):
        # print("Breaking entrance and exit")
        self.__cells[0][0].has_top_wall = False
        self.__cells[-1][-1].has_bottom_wall = False
        if self.__win != None:
            self.__draw_cell(1,1)
            self.__draw_cell(self.__num_cols,self.__num_rows)
            
    def __break_walls_r(self, i, j):
        print("Wall breaking!")
        print(f"Current Cell co-ords: {i},{j}")
        curr_cell = self.__cells[i][j]
        curr_cell._Cell__visited = True
        # Get a random int to determine which walls to break
        if i == 0 and j == 0: ## Start cell - Only remove right or bottom
            wall_break = [random.randint(1,2)]
        elif i == self.__num_cols -1 and j == self.__num_rows -1: ## End cell - Only remove top or left
            wall_break = [random.randint(3,4)]
        elif i == 0: ## Left edge cells - Don't try and remove left wall
            wall_break = [random.randint(1,3)]
        elif j == self.__num_rows-1: ## Bottom edge cells - Don't try and remove bottom wall
            wall_break = [random.randint(2,4)]
        elif j == 0: ## Top edge cells - Don't try and remove top wall
            wall_break = [random.randint(0,2)]
        elif i == self.__num_cols-1: ## Right edge cells - Don't try and remove right wall
            wall_break = [random.randint(3,5)]
        else: ## Internal cells - GO WILD!
            wall_break = [random.randint(1,4),random.randint(1,4)]
        
        for n in wall_break:
            match n:
                case 0:
                    print("Break left")
                    curr_cell.has_left_wall = False
                    if i !=0:
                        self.__cells[i-1][j].has_right_wall = False            
                case 1:
                    print("Break bottom")
                    curr_cell.has_bottom_wall = False
                    if j != self.__num_rows -1:
                        self.__cells[i][j+1].has_top_wall = False
                        # self.__break_walls_r(i,j+1)
                case 2:
                    print("Break right")
                    curr_cell.has_right_wall = False
                    if i != self.__num_cols -1:
                        self.__cells[i+1][j].has_left_wall = False
                        # self.__break_walls_r(i+1,j)
                case 3:
                    print("Break top")
                    curr_cell.has_top_wall = False
                    if j != 0:
                        self.__cells[i][j-1].has_bottom_wall = False
                        # self.__break_walls_r(i,j-1)
                case 4:
                    print("Break left")
                    curr_cell.has_left_wall = False
                    if i !=0:
                        self.__cells[i-1][j].has_right_wall = False
                        # self.__break_walls_r(i-1,j)
                case 5:
                    print("Break bottom")
                    curr_cell.has_bottom_wall = False
                    if j != self.__num_rows -1:
                        self.__cells[i][j+1].has_top_wall = False

            
        
        # Check if cell is on border based on i,j co-ords and set the relevant side to True so it draws
        if j == 0:
            curr_cell.has_top_wall = True
        if j == self.__num_rows -1:
            curr_cell.has_bottom_wall = True 
        if i == 0:
            curr_cell.has_left_wall = True
        if i == self.__num_cols -1:
            curr_cell.has_right_wall = True
        
        # Check if need to draw cell
        if self.__win != None:
            self.__draw_cell(i+1,j+1)      
        
        # Work out next move
        # Try to move down
        if self.isValid(i,j+1):
            self.__break_walls_r(i,j+1)
        # Try to move right
        if self.isValid(i+1,j):
            self.__break_walls_r(i+1,j)
        # Try to move up
        if self.isValid(i,j-1):
            self.__break_walls_r(i,j-1)
        # Try to move left
        if self.isValid(i-1,j):
            self.__break_walls_r(i-1,j)
        
        # if j+1 <= self.__num_rows-1:
        #     if not self.__cells[i][j+1]._Cell__visited:
        #         self.__break_walls_r(i,j+1)
        # # Try to move
        # if i+1 <= self.__num_cols-1:
        #     if not self.__cells[i+1][j]._Cell__visited:
        #         self.__break_walls_r(i+1,j)
                
    def isValid(self,i,j):
        return ((i >= 0 and i < self.__num_cols) and (j >= 0 and j < self.__num_rows)) and not self.__cells[i][j]._Cell__visited
        
        
    def __reset_cells_visited(self):
        for x,xv in enumerate(self.__cells):
            for y,yv in enumerate(self.__cells[x]):
                self.__cells[x][y]._Cell__visited = False

    def solve(self):
        return self.__solve_r(0,0)
        
    def __solve_r(self,i,j):
        print("Trying to solve!")
        print(f"Current Cell co-ords: {i},{j}")
        self.__animate()
        curr_cell = self.__cells[i][j]
        print(f"Cell details:{curr_cell}")
        
        curr_cell._Cell__visited = True
        if i == self.__num_cols-1 and j == self.__num_rows-1:
            return True
        
        # Attempt to move down
        if self.isValid(i,j+1) and curr_cell.has_bottom_wall == False and self.__cells[i][j+1].has_top_wall == False:
            # if not self.__cells[i][j+1]._Cell__visited:
                print("Moving down!")
                target_cell = self.__cells[i][j+1]
                print(f"Move to cell:{target_cell}")
                curr_cell.draw_move(target_cell)
                result = self.__solve_r(i,j+1)
                if result:
                    return True
                else:
                    curr_cell.draw_move(target_cell,True)

        # Attempt to move right
        if self.isValid(i+1,j) and curr_cell.has_right_wall == False and self.__cells[i+1][j].has_left_wall == False:
            # if not self.__cells[i+1][j]._Cell__visited:
                print("Moving right!")
                target_cell = self.__cells[i+1][j]
                print(f"Move to cell:{target_cell}")
                curr_cell.draw_move(target_cell)
                result = self.__solve_r(i+1,j)
                if result:
                    return True
                else:
                    curr_cell.draw_move(target_cell,True)

        # Attempt to move up
        if self.isValid(i,j-1) and curr_cell.has_top_wall == False and self.__cells[i][j-1].has_bottom_wall == False:
            # if not self.__cells[i][j-1]._Cell__visited:
                print("Moving up!")
                target_cell = self.__cells[i][j-1]
                print(f"Move to cell:{target_cell}")
                curr_cell.draw_move(target_cell)
                result = self.__solve_r(i,j-1)
                if result:
                    return True
                else:
                    curr_cell.draw_move(target_cell,True)
                    
        # Attempt to move left
        if self.isValid(i-1,j) and curr_cell.has_left_wall == False and self.__cells[i-1][j].has_right_wall == False:
            # if not self.__cells[i-1][j]._Cell__visited:
                print("Moving left!")
                target_cell = self.__cells[i-1][j]
                print(f"Move to cell:{target_cell}")
                curr_cell.draw_move(target_cell)
                result = self.__solve_r(i-1,j)
                if result:
                    return True
                else:
                    curr_cell.draw_move(target_cell,True)
        
        # If all the above fails, it should mean the maze has no solution!           
        else:
            print("No solution found!")
            return False