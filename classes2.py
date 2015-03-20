""" Drawing some shapes with pygame! """

import pygame
from pygame.locals import *
import time

class Polygon(object):
    """ A Class to represent an arbitrary Polygon that can be drawn to a window """
    def __init__(self, vertices):
        """ Creates a polygon that can be drawn to a pygame window

            vertices: a list of two-element tuples with the first element of the
                      tuple specifying the x-coordinate of a vertex and the
                      second element of the tuple representing the y-coordinate
                      of a vertex.  The vertices should be in the order that they
                      should be drawn.
        """
        self.vertices = vertices

    def draw(self, screen):
        """ Draws the Polygon object to the specified screen """
        for i,v in enumerate(self.vertices):
            next_v = self.vertices[(i + 1)%len(self.vertices)]
            # draw an edge of the polygon
            pygame.draw.line(screen, pygame.Color(0,0,0), v, next_v)

class Rectangle(Polygon):
    """ Represents a rectangle that can be drawn to a pygame window """
    def __init__(self, x_upperleft, y_upperleft, width, height):
        """ Initialize the Square with the specified geometry """
        self.x_upperleft = x_upperleft
        self.y_upperleft = y_upperleft
        self.width = width
        self.height = height
        self.vertices = self.getVertices()
        super(Rectangle, self).__init__(self.vertices)
        
    def getVertices(self, x_upperleft, y_upperleft, width, height):
        


    def draw(self, screen):
        """ Renders the rectangle to the specified screen """
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft,self.y_upperleft),
                         (self.x_upperleft + self.width,self.y_upperleft))
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft + self.width, self.y_upperleft),
                         (self.x_upperleft + self.width,self.y_upperleft + self.height))
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft + self.width,self.y_upperleft + self.height),
                         (self.x_upperleft, self.y_upperleft + self.height))
        pygame.draw.line(screen,
                         pygame.Color(0,0,0),
                         (self.x_upperleft, self.y_upperleft+ self.height),
                         (self.x_upperleft, self.y_upperleft))


class Square(Rectangle):
    """ Represents a Square that can be drawn to a pygame window """
    def __init__(self, x_upperleft, y_upperleft, side_length):
        """ Initialize the Square with the specified geometry """
        super(Square, self).__init__(x_upperleft, y_upperleft, side_length, side_length)

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    running = True

    triangle = Polygon([(300,300),(400,300),(400,450)])
    square = Square(50,20,100)
    rect = Rectangle(200,100,200,10)
    while running:
        screen.fill(pygame.Color(255,255,255))
        square.draw(screen)
        rect.draw(screen)
        triangle.draw(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()