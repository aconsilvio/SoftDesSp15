import math
import matplotlib
import matplotlib.pyplot as plt


def approximation(x, order):
	#approximate e^x based on x and the number of terms in the equation
	approx = 0
	for index in range(order):
		approx += x**index / factorial(index)
	return approx

x = range(-10, 11)
apx_3_ord = [approximation(item, 3) for item in x]
apx_10_ord = [approximation(item, 10) for item in x]
apx_50_ord = [approximation(item, 50) for item in x]
ex = [math.exp(item) for item in x]

plt.plot(x,ex)