import numpy as np

x = np.array([1, 2, 4, 2, 5, 3])
print(x)

multi_dimensional_x = np.array([range(i, i + 3) for i in x])
print(multi_dimensional_x)

# array filled with 0's
y = np.zeros(10, dtype=float)
print(y)

# array filled with 1's
z = np.ones((3, 5), dtype=int)
print(z)

# array filled with given number
number_array = np.full((5,6), 123)
print(number_array)

# linear sequence array (start, stop, step) without the last result
print(np.arange(2, 12, 2))

# evenly spaced values (first value, second value, number of values between)
print(np.linspace(3, 7, 8))

# array of uniformly distributed random values between 0 and 1
print(np.random.random((5,5)))

# array of normally distributed random values (mean, standard deviation, (x, y))
print(np.random.normal(2, 1, (3, 3)))

# array of random integers (start number, stop number, (x, y))
print(np.random.randint(1, 12, (3, 5)))

# identity matrix
print(np.eye(5))

# uninitialized array of given number integers (gives what exists in mem loc)
print(np.empty(4))

