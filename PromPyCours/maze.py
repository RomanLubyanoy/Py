# -*- coding:utf-8 -*-
def print_maze(maze,x,y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print s
    print ' '


class MazeRunner(object):
    
    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        #print_maze(self.__maze, self.__x, self.__y)
        return True
    
    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self
    
    def turn_right(self):
        right_rotation = {
            (1,0): (0,1),
            (0,-1): (1,0),
            (-1,0): (0,-1),
            (0,1): (-1,0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self
    
    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]


def maze_controller(mr):

#    while mr.found() == False:
    for steps in range(60):
        if mr.go():
            mr.go()
            mr.turn_left()
            if mr.go():
                mr.go()
            else:
                mr.turn_right()
                mr.go()

        else:
            mr.turn_right()
        if mr.found():
            print steps
            break

maze_example2 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}

maze_example3 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}

maze_example4 = {
    'm': [
        [0,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [1,1,0,1,0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}

maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
#maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
#maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f'])
#print print_maze(maze_example2['m'], maze_example2['s'], maze_example2['f'])
#print print_maze(maze_example3['m'], maze_example3['s'], maze_example3['f'])
#print print_maze(maze_example4['m'], maze_example4['s'], maze_example4['f'])
print '=========='
maze_controller(maze_runner)
print '=========='
print maze_runner.found()
