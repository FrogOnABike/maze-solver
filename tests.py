import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells_small(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )

    def test_maze_create_cells_medium(self):
        num_cols = 24
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells_large(self):
        num_cols = 48
        num_rows = 40
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
        
    def test_maze_create_cells_xlarge(self):
        num_cols = 96
        num_rows = 80
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    
    def test_break_entrance_and_exit(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1._Maze__cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._Maze__cells[num_cols-1][num_rows-1].has_bottom_wall,
            False,
        )
    
    def test_reset_visited_cells(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        for x,xv in enumerate(m1._Maze__cells):
            for y,yv in enumerate(m1._Maze__cells[x]):
                self.assertEqual(
                    m1._Maze__cells[x][y]._Cell__visited,
                    False,
                )
        
if __name__ == "__main__":
    unittest.main(verbosity=2)