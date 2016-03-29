# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = '#'

# The visual representation of a hallway.
HALL = '.'

# The visual representation of a brussels sprout.
SPROUT = '@'

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = 'J'
RAT_2_CHAR = 'P'


class Rat:
    """ A rat caught in a maze. """

    # Write your Rat methods here.
    def __init__(self, symbol, row, col):
        """ (Rat, str, int, int) -> NoneType

        A rat with a one character symbol, row and column position.
        Initial number of sprouts eaten set to 0.

        >>> ratty = Rat('P', 1, 4)
        >>> ratty.symbol
        'P'
        >>> ratty.row
        1
        >>> ratty.col
        4
        >>> ratty.num_sprouts_eaten
        0

        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = 0

    def __str__(self):
        """ (Rat) -> str

        Return a string representation of the rat.

        >>> ratty = Rat('P', 1, 4)
        >>> str(ratty)
        'P at (1, 4) ate 0 sprouts.'
        """

        return '{0} at ({1}, {2}) ate {3} sprouts.'.format(self.symbol,
            self.row, self.col, self.num_sprouts_eaten)
    def set_location(self, row, col):
        """ (Rat, int, int) -> NoneType 

        Set the row and column instance variables.

        >>> ratty = Rat('P', 1, 4)
        >>> ratty.set_location(1,2)
        >>> ratty.row
        1
        >>> ratty.col
        2
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """ (Rat) -> NoneType 

        Increases the number of sprouts eaten by 1.

        >>> ratty = Rat('P', 1, 4)
        >>> ratty.eat_sprout()
        >>> ratty.num_sprouts_eaten
        1
        """
        self.num_sprouts_eaten += 1


class Maze:
    """ A 2D maze. """

    # Write your Maze methods here.

    def __init__(self, maze, rat_1, rat_2):
        """(Maze, list of list of str, Rat, Rat) -> NoneType 

        A maze defined by a list of strings symbolising wall, 
        and sprouts. The maze comes with two rats. 

        >>> the_maze = [ \
                ['#', '#', '#', '#', '#', '#', '#'], \
                ['#', '.', '.', '.', '.', '.', '#'], \
                ['#', '.', '#', '#', '#', '.', '#'], \
                ['#', '.', '.', '@', '#', '.', '#'], \
                ['#', '@', '#', '.', '@', '.', '#'], \
                ['#', '#', '#', '#', '#', '#', '#']]
        >>> rat1 = Rat('P', 1, 1)
        >>> rat2 = Rat('J', 1, 4)
        >>> maze = Maze(the_maze, rat1, rat2)
        >>> print(maze.rat_1)
        P at (1, 1) ate 0 sprouts.
        >>> print(maze.rat_2)
        J at (1, 4) ate 0 sprouts.
        >>> print(maze.num_sprouts_left)
        3
        """
        self.maze = maze
        self.rat_1 = rat_1
        self.rat_2 = rat_2

        no_sprouts = 0
        for i in self.maze:
            for j in i:
                if j == SPROUT:
                    no_sprouts += 1

        self.num_sprouts_left = no_sprouts

    def __str__(self):
        """ (Maze) -> str

        Returns a string representation of the maze, showing the position
        of the two rats.

        >>> the_maze = [ \
                ['#', '#', '#', '#', '#', '#', '#'], \
                ['#', '.', '.', '.', '.', '.', '#'], \
                ['#', '.', '#', '#', '#', '.', '#'], \
                ['#', '.', '.', '@', '#', '.', '#'], \
                ['#', '@', '#', '.', '@', '.', '#'], \
                ['#', '#', '#', '#', '#', '#', '#']]
        >>> rat1 = Rat('P', 1, 1)
        >>> rat2 = Rat('J', 2, 1)
        >>> maze = Maze(the_maze, rat1, rat2)
        >>> print(maze)
        #######
        #P....#
        #J###.#
        #..@#.#
        #@#.@.#
        #######
        P at (1, 1) ate 0 sprouts.
        J at (2, 1) ate 0 sprouts.
        """

        str_maze = ''
        for i in range(len(self.maze)):
            for j in range(len(self.maze[i])):
                if self.rat_1.row == i and self.rat_1.col == j:
                    str_maze += self.rat_1.symbol
                elif self.rat_2.row == i and self.rat_2.col == j:
                    str_maze += self.rat_2.symbol
                else:
                    str_maze += self.maze[i][j]
            str_maze += '\n'    
        str_maze += str(self.rat_1) + '\n'
        str_maze += str(self.rat_2)
        return str_maze

    def is_wall(self, row, col):
        """ (Maze, int, int) -> bool

        Returns true if there is a wall at position row, col

        >>> the_maze = [ \
                ['#', '#', '#', '#', '#', '#', '#'], \
                ['#', '.', '.', '.', '.', '.', '#'], \
                ['#', '.', '#', '#', '#', '.', '#'], \
                ['#', '.', '.', '@', '#', '.', '#'], \
                ['#', '@', '#', '.', '@', '.', '#'], \
                ['#', '#', '#', '#', '#', '#', '#']]
        >>> rat1 = Rat('P', 1, 1)
        >>> rat2 = Rat('J', 1, 4)
        >>> maze = Maze(the_maze, rat1, rat2)
        >>> maze.is_wall(1,0)
        True
        >>> maze.is_wall(1,1)
        False
        """

        if self.maze[row][col] == WALL:
            return True
        else: 
            return False

    def get_character(self, row, col):
        """ (Maze, int, int) -> str

        Return the character in the maze at the given row and column. 
        If there is a rat at that location, then its character should 
        be returned rather than HALL.

        >>> the_maze = [ \
                ['#', '#', '#', '#', '#', '#', '#'], \
                ['#', '.', '.', '.', '.', '.', '#'], \
                ['#', '.', '#', '#', '#', '.', '#'], \
                ['#', '.', '.', '@', '#', '.', '#'], \
                ['#', '@', '#', '.', '@', '.', '#'], \
                ['#', '#', '#', '#', '#', '#', '#']]
        >>> rat1 = Rat('P', 1, 1)
        >>> rat2 = Rat('J', 1, 4)
        >>> maze = Maze(the_maze, rat1, rat2)
        >>> maze.get_character(0,0)
        '#'
        >>> maze.get_character(1,1)
        'P'
        >>> maze.get_character(2,1)
        '.'
        """

        if (row, col) == (self.rat_1.row, self.rat_1.col):
            return self.rat_1.symbol
        elif (row, col) == (self.rat_2.row, self.rat_2.col):
            return self.rat_2.symbol
        else:
            return self.maze[row][col]

    def move(self, rat, vert, horz):
        """ (Maze, Rat, int, int) -> bool

        Move the rat in the given direction, unless there is a wall in the way. 
        Check for a sprout and have the rat eat the sprout. Return True if there
        isn't a wall in the way.

        >>> the_maze = [ \
                ['#', '#', '#', '#', '#', '#', '#'], \
                ['#', '.', '.', '.', '.', '.', '#'], \
                ['#', '.', '#', '#', '#', '.', '#'], \
                ['#', '.', '.', '@', '#', '.', '#'], \
                ['#', '@', '#', '.', '@', '.', '#'], \
                ['#', '#', '#', '#', '#', '#', '#']]
        >>> rat1 = Rat('P', 1, 1)
        >>> rat2 = Rat('J', 1, 2)
        >>> maze = Maze(the_maze, rat1, rat2)
        >>> maze.move(rat1, 0, -1)
        False
        >>> maze.move(rat1, 1, 0)
        True
        >>> maze.move(rat1, 1, 0)
        True
        >>> maze.move(rat1, 1, 0)
        True
        >>> rat1.num_sprouts_eaten
        1
        >>> maze.num_sprouts_left
        2
        >>> maze.move(rat1, -1, 0)
        True
        >>> maze.get_character(1, 4)
        '.'

        """
        new_row  = rat.row
        new_col = rat.col

    
        new_row += vert
        new_col += horz

        #print new_row, new_col
        maze_char = self.get_character(new_row, new_col)
        if maze_char == WALL:
            return False
        elif maze_char == SPROUT:
            rat.set_location(new_row, new_col)
            rat.num_sprouts_eaten += 1
            self.num_sprouts_left -= 1
            self.maze[new_row][new_col] = HALL
            return True
        else:
            rat.set_location(new_row, new_col)
            return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()