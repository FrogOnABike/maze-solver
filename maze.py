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
            self.__seed = random.seed(seed)
        else:
            self.__seed = None
        self.__create_cells()
        self.__break_entrance_and_exit()
        
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
        time.sleep(0.05)
        
    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__cells[-1][-1].has_bottom_wall = False
        if self.__win != None:
            self.__draw_cell(1,1)
            self.__draw_cell(self.__num_cols,self.__num_rows)