from tkinter import Tk, BOTH, Canvas

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
        
