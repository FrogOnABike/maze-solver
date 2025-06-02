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
        self.__break_walls_r(1,1)
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
        # print("Wall breaking!")
        curr_cell = self.__cells[i-1][j-1]
        curr_cell._Cell__visited = True
        # Get a random int between 1 and 6 to determine which walls to break
        wall_break = random.randint(1,6)
        match wall_break:
            case 1:
                curr_cell.has_top_wall = False
                curr_cell.has_right_wall = False
            case 2:
                curr_cell.has_right_wall = False
                curr_cell.has_bottom_wall = False
            case 3:
                curr_cell.has_bottom_wall = False
                curr_cell.has_left_wall = False
            case 4:
                curr_cell.has_left_wall = False
                curr_cell.has_top_wall = False
            case 5:
                curr_cell.has_top_wall = False
                curr_cell.has_bottom_wall =False
            case 6:
                curr_cell.has_left_wall = False
                curr_cell.has_right_wall = False
            
        
        # Check if cell is on border based on i,j co-ords and set the relevant side to True so it draws
        if j == 1:
            curr_cell.has_top_wall = True
        if j == self.__num_rows:
            curr_cell.has_bottom_wall = True 
        if i == 1:
            curr_cell.has_left_wall = True
        if i == self.__num_cols:
            curr_cell.has_right_wall = True

        if self.__win != None:
            self.__draw_cell(i,j)      
        
        if j+1 <= self.__num_rows:
            if not self.__cells[i-1][j]._Cell__visited:
                self.__break_walls_r(i,j+1)
        if i+1 <= self.__num_cols:
            if not self.__cells[i][j-1]._Cell__visited:
                self.__break_walls_r(i+1,j)
        
    def __reset_cells_visited(self):
        for x,xv in enumerate(self.__cells):
            for y,yv in enumerate(self.__cells[x]):
                self.__cells[x][y]._Cell__visited = False

    
        
            
        
    