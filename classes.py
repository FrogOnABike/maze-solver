from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self,width,height):
        self.__root = Tk()
        self.__root.title("Mark's A-mazing Solver!")
        self.__running = False
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update()
        self.__root.update_idletasks()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
        
    def draw_line(self,line,fill_color):
        line.draw(self.__canvas,fill_color)
        
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
class Line:
    def __init__(self,point1,point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y
    
    def draw(self,canvas,fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)
        
class Cell:
    def __init__(self,window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        
    def draw(self,p1,p2):
        self.__x1 = p1.x
        self.__x2 = p2.x
        self.__y1 = p1.y
        self.__y2 = p2.y
        # self.has_bottom_wall = b
        # self.has_top_wall = t
        # self.has_left_wall = l
        # self.has_right_wall = r
        if self.has_top_wall:
            top_line = Line(Point(self.__x1,self.__y1),Point(self.__x2,self.__y1))
            self.__win.draw_line(top_line,"black")
        if self.has_bottom_wall:
            bottom_line = Line(Point(self.__x1,self.__y2),Point(self.__x2,self.__y2))
            self.__win.draw_line(bottom_line,"black")
        if self.has_left_wall:
            left_line = Line(Point(self.__x1,self.__y1),Point(self.__x1,self.__y2))
            self.__win.draw_line(left_line,"black")
        if self.has_right_wall:
            right_line = Line(Point(self.__x2,self.__y1),Point(self.__x2,self.__y2))
            self.__win.draw_line(right_line,"black")
        
    def draw_move(self, to_cell, undo=False):
        if undo:
            fc = "grey"
        else:
            fc = "red"
        move_line = Line(Point((self.__x1+self.__x2)/2,(self.__y1+self.__y2)/2),Point((to_cell.__x1+to_cell.__x2)/2,(to_cell.__y1+to_cell.__y2)/2))
        self.__win.draw_line(move_line,fc)
        
    def __repr__(self):
        return f"X1:{self.__x1},Y1:{self.__y1},X2:{self.__x2},Y2:{self.__y2}"
    
class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        
    def __create_cells(self):
        for x in range(self.__num_cols):
            row = []
            for y in range(self.__num_rows):
                row.append(Cell(self.__win))
            self.__cells.append(row)
        print(f"Cells list:{self.__cells}")
    
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
        