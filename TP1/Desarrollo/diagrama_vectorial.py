# python modules
from matplotlib import pyplot

from numpy import pi
from numpy import radians

from cmath import rect
from cmath import phase

from random import random

from time import sleep


def random_color():
	""" Generates a random RGBA color with a 3-tupled value """
	sleep(0.015)
	return (random(),random(),random(),1)

if __name__ == "__main__":

	# Complex values measured
	v_cap = rect(13.9, radians(-45))
	v_res = rect(14.2, radians(44))
	i = rect(0.0026, radians(44))
	v_source = v_cap + v_res
	
	# Create the figure
	figure = pyplot.figure()
	axes = pyplot.subplot(projection="polar")
	axes.set_ylim(0, 21)
	axes.set_xlim(radians(-50), radians(50))
	
	axes.set_xticks(list(radians(i) for i in range(-50, 50, 5)))
	
	# Drawing the arrows
	to_draw = [
		("Capacitor", v_cap),
		("Resistencia", v_res),
		("Generador", v_source)
	]
	
	arrows = []
	labels = []
	
	for label, draw in to_draw:
		arrow = pyplot.arrow(0, 0, phase(draw), abs(draw),
					color = random_color(),
					linewidth=1.5)
					
		arrows.append(arrow)
		labels.append(label)
	
	# Showing the resulting plot
	figure.legend(arrows, labels)
	pyplot.show()
