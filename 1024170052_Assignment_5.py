import numpy as np

# Question 1
arr = np.array([10, 20, 30, 40, 50])

print("Original array:", arr)
print("After adding 2:", arr + 2)
print("After multiplying by 3:", arr * 3)
print("After dividing by 2:", arr / 2)
print()

# Question 2
arr = np.array([1, 2, 3, 6, 4, 5])
print("Original array:", arr)
print("Reversed array:", arr[::-1])
print()

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])
y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

x_values, x_counts = np.unique(x, return_counts=True)
x_max_count = x_counts.max()
x_most_frequent = x_values[x_counts == x_max_count]

print("Array x:", x)
print("Most frequent value in x:", x_most_frequent)
for value in x_most_frequent:
    print("Indices of", value, "in x:", np.where(x == value)[0])
print()

y_values, y_counts = np.unique(y, return_counts=True)
y_max_count = y_counts.max()
y_most_frequent = y_values[y_counts == y_max_count]

print("Array y:", y)
print("Most frequent value in y:", y_most_frequent)
for value in y_most_frequent:
    print("Indices of", value, "in y:", np.where(y == value)[0])
print()

# Question 3
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print("2-D array:")
print(arr)
print("1st row, 2nd column:", arr[0, 1])
print("3rd row, 1st column:", arr[2, 0])
print()

# Question 4
ucs420_abhi = np.linspace(10, 100, 25)

print("Array:", ucs420_abhi)
print("Dimensions:", ucs420_abhi.ndim)
print("Shape:", ucs420_abhi.shape)
print("Total elements:", ucs420_abhi.size)
print("Data type:", ucs420_abhi.dtype)
print("Total bytes:", ucs420_abhi.nbytes)

transpose_array = ucs420_abhi.reshape(1, 25)
print("Transpose using reshape():")
print(transpose_array)

print("Transpose using T attribute:")
print(ucs420_abhi.T)
print("For a 1-D array, T does not change the shape. Reshape is used to get a row or column form.")
print()

# Question 5
ucs420_abhi = np.array([[10, 20, 30, 40],
                        [50, 60, 70, 80],
                        [90, 15, 20, 35]])

print("Original 2-D array:")
print(ucs420_abhi)
print("Mean:", np.mean(ucs420_abhi))
print("Median:", np.median(ucs420_abhi))
print("Maximum:", np.max(ucs420_abhi))
print("Minimum:", np.min(ucs420_abhi))
print("Unique elements:", np.unique(ucs420_abhi))

reshaped_ucs420_abhi = ucs420_abhi.reshape(4, 3)
print("Reshaped array:")
print(reshaped_ucs420_abhi)

resized_ucs420_abhi = np.resize(ucs420_abhi, (2, 3))
print("Resized array:")
print(resized_ucs420_abhi)
