#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Project Euler problem file
import time
import math

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!PROBLEMS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#*******************************PROBLEM 1*******************************
#If we list all the natural numbers below 10 that are multiples of 3 or 5, 
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

def problem_1():
	start = time.clock()
	s = sum([n for n in range(1000) if (n % 3 == 0 or n % 5 == 0)])
	print s
	print 'Took {} seconds'.format(time.clock()-start)
	
#*******************************PROBLEM 2*******************************
# Each new term in the Fibonacci sequence is generated by adding the 
# previous two terms. By starting with 1 and 2, the first 10 terms 
# will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do 
# not exceed four million, find the sum of the even-valued terms.

def problem_2():
	start = time.clock()
	s = 0
	fib = gen_fib(4000000)
	for f in fib:
		if f % 2 ==0:
			s += f
	print s
	print 'Took {} seconds'.format(time.clock()-start)

#*******************************PROBLEM 3*******************************
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def problem_3():
	start = time.clock()
	n = 600851475143
	i = 2
	while i * i < n:
		while n % i == 0:
			n = n / i
		i = i + 1

	print (n)
	print 'Took {} seconds'.format(time.clock()-start) 
	
#*******************************PROBLEM 4*******************************
#A palindromic number reads the same both ways. The largest palindrome made
#from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.

def problem_4():
	start = time.clock()
	s = 0
	for i in range(100, 999):
		for j in range(100, 999):
			if is_palindrome(i*j): 
				if i*j > s:
					s = i*j
				
	print s
	print 'Took {} seconds'.format(time.clock()-start) 
	
#*******************************PROBLEM 5*******************************
#2520 is the smallest number that can be divided by each of the numbers 
#from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of 
#the numbers from 1 to 20?

def problem_5():
	start = time.clock()
	s = range(1, 21)
	n = 19*20
	while True:
		flag = True
		for i in s:
			if n % i != 0:
				flag = False
		if flag == True:
			break
		n += 20
	print n
	print 'Took {} seconds'.format(time.clock()-start) 

#*******************************PROBLEM 6*******************************
#The sum of the squares of the first ten natural numbers is,
#
#12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten 
#natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one 
#hundred natural numbers and the square of the sum.

def problem_6():
	start = time.clock()
	print sum(i for i in range(101))**2 - sum(i**2 for i in range(101))
	print 'Took {} seconds'.format(time.clock()-start)
	
#*******************************PROBLEM 7*******************************
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can 
#see that the 6th prime is 13.
#
#What is the 10,001st prime number?

def problem_7():
	start = time.clock()
	n = 3
	cnt = 0
	while True:
		if is_prime(n):
			cnt +=1
		if cnt == 10000:
			print n
			break
		n+=2
	print 'Took {} seconds'.format(time.clock()-start)
	
#*******************************PROBLEM 8*******************************
# Find the thirteen adjacent digits in the 1000-digit number that have the
# greatest product. What is the value of this product?

def problem_8():
	start = time.clock()
	val = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
	res = [val[i:i+13] for i in range(len(val)-13)]
	mx = max(sum(
	for v in res:
		x=sum([int(j) for j in v])
		if x > y[1]:
			y[0]=v
			y[1]=x
	print y[0]
	print 'Took {} seconds'.format(time.clock()-start)

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

# Returns true if n is a palindromic number
def is_palindrome(n):
	n = str(n)
	for f in range(len(n)):
		if n[f]==n[len(n)-f-1]:
			retval =  True
		else:
			retval =  False
			break
	return retval

# Returns true if n is prime
def is_prime(n):
	for i in range(3,int(n/2)):
		if n % i == 0:
			return False
	return True

# Returns a list of primes up to n
def primes(n): # simple Sieve of Eratosthenes 
	odds = xrange(3, n+1, 2)
	sieve = set(sum([range(q*q, n+1, q+q) for q in odds],[]))
	return [2] + [p for p in odds if p not in sieve]

# Returns a fibonacci sequence up to n
def gen_fib(n):
	result = [1, 2]
	for i in range(n):
		result.extend(result[-2]+result[-1])
	return result
	
if __name__ == '__main__':
	problem_8()
