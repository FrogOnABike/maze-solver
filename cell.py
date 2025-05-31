from classes import *

class Cell:    
    def __init__(self,window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self.__visited = False
        
    def draw(self,p1,p2):
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y
    
        if self.has_top_wall:
            lc = "black"
        else:
            lc = "white"
        top_line = Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1))
        if self.__win != None:
            self.__win.draw_line(top_line,lc)
        
    
        if self.has_bottom_wall:
            lc = "black"
        else:
            lc = "white"
        bottom_line = Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2))
        if self.__win != None:
            self.__win.draw_line(bottom_line,lc)
    
        if self.has_left_wall:
            lc = "black"
        else:
            lc = "white"
        left_line = Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2))
        if self.__win != None:
            self.__win.draw_line(left_line,lc)
    
        if self.has_right_wall:
            lc = "black"
        else:
            lc = "white"
        right_line = Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2))
        if self.__win != None:
            self.__win.draw_line(right_line,lc)
        
    def draw_move(self, to_cell, undo=False):
        if undo:
            fc = "grey"
        else:
            fc = "red"
        move_line = Line(Point((self.__x1+self.__x2)/2,(self.__y1+self.__y2)/2),Point((to_cell.__x1+to_cell.__x2)/2,(to_cell.__y1+to_cell.__y2)/2))
        if self.__win != None:
            self.__win.draw_line(move_line,fc)
        
    def __repr__(self):
        return f"X1:{self.__x1},Y1:{self.__y1},X2:{self.__x2},Y2:{self.__y2}"
    
