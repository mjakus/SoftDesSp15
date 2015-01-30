def print_evens(n):
	""" print even numbers less than 10"""
	from is_even import is_even
	i = 1
	while i < n:
		if is_even(i):
			print i
		i=i+1
	return



def factorial(a):
	total = 1
	while a > 0:
		total = total*a
		a = a-1
	print total
	return

print print_evens(20)
print factorial(6)