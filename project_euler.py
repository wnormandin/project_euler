#!/usr/bin/python

import math
import time

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PROBLEMS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#******************************PROBLEM 9********************************
# A Pythagorean triplet is a set of three natural numbers, a < b < c, 
# for which, a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def problem_9():
	start = time.clock()
	for a in range(250):
		for b in range(500):
			if test_triplet(a, b):
				print a * b * (math.sqrt(a**2 + b **2))
				print 'Took {} seconds.'.format(time.clock()-start)
				break
				
#******************************PROBLEM 10*******************************
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def problem_10():
	pass
	
#******************************PROBLEM 11*******************************
# What is the greatest product of four adjacent numbers in the same

def problem_11():
	start = time.clock()
	fpath = './problem11.txt'
	grid = []
	with open(fpath) as f:
		for line in f:
			grid.append(line.strip('\n').split(' '))
	print grid_calc(grid)
	print 'Took {} seconds.'.format(time.clock()-start)
	
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!FUNCTIONS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Problem 11 matrix calculations
def grid_calc(grid):
	sums = []
	for y in xrange(16):
		for x in xrange(16):
			print 'y : {}\t| x : {}'.format(y,x)
			sums.extend([reduce(lambda a, b: int(a)*int(b), row) for row in [grid[n][x:x+3] for n in xrange(y,y+3)]])
			print 'y : {}\t| x : {}'.format(y,x)
			sums.extend([reduce(lambda a, b: int(a)*int(b), col) for col in [grid[y][n] for n in xrange(x,x+3) for y in xrange(y,y+3)]])
			print 'y : {}\t| x : {}'.format(y,x)
			sums.extend([reduce(lambda a, b: int(a)*int(b), diag) for diag in [grid[y+n][x+n] for n in xrange(3)]])
			print 'y : {}\t| x : {}'.format(y,x)
			sums.extend([reduce(lambda a, b: int(a)*int(b), rdiag) for rdiag in [grid[y-n][x+3-n] for n in xrange(3,0,-1)]])
	
	return max(sums)

def test_triplet(a, b):
	csq = a**2 + b**2
	c = math.sqrt(csq)
	if a + b + c == 1000:
		return True
	else:
		return False

if __name__ == '__main__':
	problem_11()
