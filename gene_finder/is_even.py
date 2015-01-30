def is_even(x):
	"""
	is x is_even
	>>> is_even(4)
	True
	>>> is_even(5)
	False
	"""

	if x%2 == 0:
		return True
	else:
		return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print is_even(6)
