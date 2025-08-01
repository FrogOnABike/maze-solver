from classes import *
from maze import Maze
import sys

def main():
    sys.setrecursionlimit(1750)
    win = Window(1024, 768)
    start_point1=Point(10,10)
    end_point1=Point(20,20)
    start_point2=Point(20,10)
    end_point2=Point(30,20)
    start_point3=Point(10,20)
    end_point3=Point(20,30)
    start_point4=Point(20,20)
    end_point4=Point(30,30)
    # Current maze dimensions seem about max it can render with the upped recursion limit!
    test_maze = Maze(5,5,39,40,20,20,win)
    test_maze.solve()
    # test_cell1 = Cell(win)
    # test_cell2 = Cell(win)
    # test_cell3 = Cell(win)
    # test_cell4 = Cell(win)
    # test_cell1.draw(start_point1,end_point1,True,True,True,False)
    # test_cell2.draw(start_point2,end_point2,True,False,False,True)
    # test_cell3.draw(start_point3,end_point3,True,True,True,False)
    # test_cell4.draw(start_point4,end_point4,False,True,False,True)
    
    # test_cell1.draw_move(test_cell2)
    # test_cell2.draw_move(test_cell4,True)
    # test_cell4.draw_move(test_cell3)
    
    # test_line=Line(start_point1,end_point1)
    # test_line2=Line(start_point2,end_point2)
    # win.draw_line(test_line,"red")
    # win.draw_line(test_line2,"black")
    win.wait_for_close()

if __name__ == "__main__":
    main()