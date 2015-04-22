""" TODO: Put your header comment here """

import random
import math
from PIL import Image
import datetime
import time


def build_random_function(min_depth, max_depth):
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    #call bjuild random inside build random
    #have it go one smaller at depth
    #if statement to return 
    functions = ["sin_pi","cos_pi","avg","prod", "sqrt","abs","cubed","x","x/2","y"]

    if min_depth > 0 and max_depth > 0:
        function = functions[random.randint(0,6)]
    if min_depth <= 0 and max_depth > 0:
        function = functions[random.randint(0,9)]
    if min_depth < 0 and max_depth <= 0:
        function = functions[random.randint(6,9)]


    if function == "avg" or function == "prod":
        lista = [function, build_random_function(min_depth-1, max_depth-1), build_random_function(min_depth-1, max_depth-1)]
    elif function == "x" or function =="y" or function == "x/2":
        lista = [function]
    else:
        lista = [function, build_random_function(min_depth-1, max_depth-1)]

    #lista is a cryptic and not very informative variable name. Its tempting to name variables
    #after data structures, but see if you can come up with a better name! But it's no 
    #big deal if you can't. 
    return lista 
    


def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    #if the first element of the list is one of the base cases x, y, or x/2 return x, y, or x/2
    if f[0] == "x":
        return x
    if f[0] == "y":
        return y
    if f[0] == "x/2":
        return x/2
    #if the first element of the inital list is a function that only takes in one input, apply the specified
    #operation to the first element of the list that begins after the first element
    if f[0] == "sin_pi":
        return math.sin(math.pi * evaluate_random_function(f[1:][0], x, y))
    if f[0] == "abs":
        return  abs(evaluate_random_function(f[1:][0], x, y))
        #f[1:][0] is the equivalent of f[1]!
    if f[0] == "sqrt":
        return  math.sqrt(abs(evaluate_random_function(f[1:][0], x, y)))
    if f[0] == "cos_pi":
        return math.cos(math.pi * evaluate_random_function(f[1:][0],  x, y))
    if f[0] == "cubed":
        return evaluate_random_function(f[1:][0],  x, y) ** 3
    if f[0] == "avg":
        return .5 * (evaluate_random_function(f[1], x, y) + evaluate_random_function(f[2], x, y))
    if f[0] == "prod":
        return (evaluate_random_function(f[1], x, y) * evaluate_random_function(f[2], x, y))



def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    a = float(input_interval_start)
    b = float(input_interval_end)
    c = float(output_interval_start)
    d = float(output_interval_end)
    x = float(val)
    #for the record, as long as one number involved in the operation is a float, the other
    #numbers will be casted to a float. So you really only need to cast some numbers to floats.
    difference_val = x - a
    difference_input = b - a
    difference_output = d -c 
    y = difference_val / difference_input * difference_output + output_interval_start
    return y


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    #also generates a random integer for depth for each function
    red_function = build_random_function(random.randint(6,9),random.randint(10,14)) 
    green_function = build_random_function(random.randint(6,9),random.randint(10,14)) 
    blue_function = build_random_function(random.randint(6,9),random.randint(10,14)) 

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    #automaticlly names the files based on the date and time
    n = time.time()
    a = 'myart_'
    b = str(n)
    #pls try to avoid using one letter variable names, even if its temporary and not too hard to follow.

    title = a+b

    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    generate_art("artpics/"+title+".png")

    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
   # test_image("noise.png")
