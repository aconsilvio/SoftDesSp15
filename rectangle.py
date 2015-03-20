"""RECTANGLES"""

"""Dealing with rectangles"""

## Point and print_point from Think Python
class Point(object):
    """Represents a point in 2-D space"""
    pass

def print_point(p):
    """Print a Point object in human-readable format"""
    template = "({x}, {y})"
    # See Python string formatting docs
    # https://docs.python.org/2/library/string.html#format-examples
    print template.format(x=p.x, y=p.y)

class Rectangle(object):
	"""Reprsents a rectangle in a 2d plane"""
	pass



## TODO:
# - Implement Rectangle class using two points, instead of point + width/length
# - Implement print_rectangle
# - Implement find_center function
a = Point()
a.x = 0
a.y = 0
b = Point()
b.x = 1
b.y = 1

def print_rectangle(a,b):
	r = Rectangle()
	r.width = b.x - a.x
	r.height = b.y - a.y
	r.a2x = a.x + r.width
	r.a2y = a.y
	r.b2y = a.y + r.height
	r.b2x = a.y
	template = "(({ax},{ay}),({bx},{by}), ({a2x},{a2y}),({b2x},{b2y})) "
	print template.format(ax = a.x, ay = a.y, bx = b.x, by = b.y, a2x = r.a2x, a2y = r.a2y, b2x = r.b2x, b2y = r.b2y)

print_rectangle(a,b)

def find_center(my_rect):
    """
    Return the Point at the center of my_rect Rectangle

    Note: Your doctest may be different depending on your 
    implementation of Rectangle
    >>> p1 = Point()
    >>> p1.x = 0
    >>> p1.y = 0
    >>> p2 = Point()
    >>> p2.x = 6
    >>> p2.y = 4
    >>> rect = Rectangle()
    >>> rect.lower_left = p1
    >>> rect.upper_right = p2
    >>> print find_center(rect)
    (3.0, 2.0)
    """
    pass

## Challenge problem:
def bounding_box(rects):
    """
    Given a list of Rectangles, return a Rectangle
    that contains all of them
    """
    pass