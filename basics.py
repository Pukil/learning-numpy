import numpy as np
#
# x = np.array([1, 2, 4, 2, 5, 3])
# print(x)

# multi_dimensional_x = np.array([range(i, i + 3) for i in x])
# print(multi_dimensional_x)

# array filled with 0's
# y = np.zeros(10, dtype=float)
# print(y)

# array filled with 1's
# z = np.ones((3, 5), dtype=int)
# print(z)

# array filled with given number
# number_array = np.full((5,6), 123)
# print(number_array)

# linear sequence array (start, stop, step) without the last result
# print(np.arange(2, 12, 2))

# evenly spaced values (first value, second value, number of values between)
# print(np.linspace(3, 7, 8))

# array of uniformly distributed random values between 0 and 1
# print(np.random.random((5,5)))

# array of normally distributed random values (mean, standard deviation, (x, y))
# print(np.random.normal(2, 1, (3, 3)))

# array of random integers (start number, stop number, (x, y))
# print(np.random.randint(1, 12, (3, 5)))

# identity matrix
# print(np.eye(5))

# uninitialized array of given number integers (gives what exists in mem loc)
# print(np.empty(4))

# seed
# np.random.seed(0)

# sizes
# a = np.random.randint(10, size=5) # one dimension
# b = np.random.randint(10, size=(2, 6)) # two dimensions
# c = np.random.randint(10, size=(3, 4, 5)) # three dimensions
# arrays = [a, b, c]
# print(a)
# print(b)
# print(c)
# for array in arrays:
#     print(f" dimensions: {array.ndim},"
#           f" shape: {array.shape},"
#           f" size: {array.size},"
#           f" type: {array.dtype},"
#           f" array element size (bytes): {array.itemsize},"
#           f" total size (bytes): {array.nbytes} ")

# accessing values in multidimensional array
# print(c[1,3,2])
# print(c)

# modifying values
# c[1,3,2] = 15
# print(c)

# accessing single row/col
# print(b[ :, 1]) # col
# print(b[ 1, :]) # row
# print(b)

# modifying subarrays changes the original aswell
# original_array = np.random.randint(1, 10, (4, 5))
# print(original_array)
# sub_array = original_array[:3, :3]
# print(sub_array)
# sub_array[1,2] = 999
# print(sub_array)
# print(original_array)

# to prevent these changes use .copy()
# sub_array_copy = sub_array.copy()
# sub_array_copy[0, 0] = 999
# print(sub_array_copy)
# print(sub_array)
# print(original_array)

# reshaping of arrays
# grid = np.arange(1, 10).reshape(3, 3)
# print(np.arange(1,10).size == np.ones((3, 3)).size) # size of array must match the size of reshaped array
# print(grid)

# new_array = np.array([1,2,3])
# print(new_array)
# new_array_reshaped = new_array.reshape(1,3) # row vector
# print(new_array_reshaped)
# new_array_reshaped_new_axis = new_array[:, np.newaxis] # column vector
# print(new_array_reshaped_new_axis)
# arrays = [new_array, new_array_reshaped, new_array_reshaped_new_axis]
# for a in arrays:
#     print(f" dimensions: {a.ndim},"
#           f" shape: {a.shape},"
#           f" size: {a.size},"
#           f" type: {a.dtype},"
#           f" array element size (bytes): {a.itemsize},"
#           f" total size (bytes): {a.nbytes} ")


# array concatenation and splitting
# x = np.array([1, 2, 3])
# y = np.array([3, 4, 5])
# z = np.arange(1, 10).reshape(3, 3)
# print(np.concatenate([x, y, x]))
# print(np.concatenate([z,z])) # axis = 0
# print(np.concatenate([z,z], axis=1)) # axis = 1

# vertically and horizontally stacking (dstack - 3rd axis)
# print(np.vstack([x, y, z]))
# print(np.hstack([z, y.reshape(3,1)]))

# xxx = np.concatenate([x, x*2, x*3])
# print(xxx)
# x1, x2, x3 = np.split(xxx, [3, 5]) # split points in []
# print(x1, x2, x3)

# zzz = np.arange(36).reshape(6, 6)
# upper, lower = np.vsplit(zzz, [3])
# left, right = np.hsplit(zzz, [3])
# print(upper)
# print(lower)
# print(left)
# print(right)

# reduce, accumulate
x = np.arange(1, 15)
print(np.add.reduce(x)) # sum of all numbers in array x
print(np.add.accumulate(x)) # shows every intermediate result

# computing the output of all pairs of 2 different inputs - outer()
print(np.multiply.outer(x, x))

