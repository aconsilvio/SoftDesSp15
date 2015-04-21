""" Practice problems for objects """

from math import sqrt

class PointND(object):
    def __init__(self, coordinates):
        """ Initialize an n-dimensional point from a list of coordinates.
            coordinates: a list of numbers specifying the coordinates of
                         the point """
        self.coordinates = coordinates

    def distance(self, other):
        """ Compute the Euclidean distance between self and other
            other: an n-dimensional pointed represented as a PointND object
            returns: the Euclidean distance between the two points.
            (assume that the two points have the same number of coordinates)

            >>> p1 = PointND([0,3])
            >>> p2 = PointND([4,0])
            >>> p1.distance(p2)
            5.0
            """
        accumulator = 0.0
        for i in range(len(self.coordinates)):
            accumulator += (self.coordinates[i] - other.coordinates[i])**2
        return sqrt(accumulator)

    def __str__(self):
        """ Converts a point to a string

        >>> p1 = PointND([4.0, 5.0, 2.0, 1.0])
        >>> print p1
        (4.0, 5.0, 2.0, 1.0)
        """
        return_val = "("
        for (i,coord) in enumerate(self.coordinates):
            return_val += str(coord)
            if i + 1 != len(self.coordinates):
                return_val += ", "
        return_val += ")"
        return return_val

class Point3D(PointND):
    def __init__(self,x,y,z):
        """ Initialize a Point3D object at position (x,y,z)
            x: a number representing the x-coordinate of the point
            y: a number representing the y-coordinate of the point
            z: a number representing the z-coordinate of the point

        >>> p = Point3D(5.0, 7.0, -2.0)
        >>> print p
        (5.0, 7.0, -2.0)
        """
        super(Point3D, self).__init__([x,y,z])

if __name__ == '__main__':
    import doctest
    doctest.testmod()