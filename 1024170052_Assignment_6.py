import numpy as np

# Question 1
temperature = np.array([25, 28, 31, 35, 38, 27, 33, 40])

corrected_temperature = temperature + 2
print("Original temperature readings:", temperature)
print("Temperature readings after adding 2°C:", corrected_temperature)

fahrenheit = (9 / 5) * corrected_temperature + 32
print("Temperature in Fahrenheit:", fahrenheit)

greater_than_32 = corrected_temperature[corrected_temperature > 32]
print("Readings greater than 32°C:", greater_than_32)

count_greater_than_32 = np.sum(corrected_temperature > 32)
print("Number of readings greater than 32°C:", count_greater_than_32)

print("Vectorization performs operations on the complete array at once.")
print("Boolean indexing selects values based on a condition without using a loop.")
print()

# Question 2
steps = np.array([
    [5000, 6200, 7100],
    [8000, 7500, 9000],
    [4500, 5100, 4800],
    [9000, 8500, 9500]
])

print("Steps matrix:")
print(steps)

print("Total steps:", np.sum(steps))
print("Mean steps:", np.mean(steps))
print("Maximum steps:", np.max(steps))
print("Minimum steps:", np.min(steps))

total_each_day = np.sum(steps, axis=0)
print("Total steps for each day:", total_each_day)

total_each_user = np.sum(steps, axis=1)
print("Total steps for each user:", total_each_user)

maximum_position = np.unravel_index(np.argmax(steps), steps.shape)
print("Position of maximum steps:", maximum_position)
print()

# Question 3
original = np.array([1, 2, 3, 4, 5, 6])

subset = original[1:5]
subset[0] = 999

print("Original after modifying subset:", original)
print("Subset:", subset)

copied_array = original[1:5].copy()
copied_array[0] = 500

print("Original after modifying copied array:", original)
print("Copied array:", copied_array)

matrix = np.arange(1, 13).reshape(3, 4)
print("3 x 4 matrix:")
print(matrix)

print("First row:", matrix[0, :])
print("Last row:", matrix[-1, :])
print("Second column:", matrix[:, 1])
print("Rows 1-2 and columns 2-3:")
print(matrix[0:2, 1:3])

flattened_array = matrix.flatten()
ravel_array = matrix.ravel()

print("Array using flatten():", flattened_array)
print("Array using ravel():", ravel_array)

ravel_array[0] = 100
print("Matrix after modifying ravel array:")
print(matrix)

flattened_array[1] = 200
print("Matrix after modifying flatten array:")
print(matrix)

print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Total elements:", matrix.size)
print("Data type:", matrix.dtype)
print()

# Question 4
X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

print("Shape of X:", X.shape)
print("Dimensions of X:", X.ndim)

print("Transpose of X:")
print(X.T)

print("X.T changes rows into columns and columns into rows.")
print("Each row of X.T represents one feature across all users.")

xtx = X.T @ X
print("X.T @ X:")
print(xtx)

inverse = np.linalg.inv(xtx)
print("Inverse of X.T @ X:")
print(inverse)

beta = inverse @ X.T @ y
print("OLS coefficients:")
print(beta)

print("The coefficients represent the contribution of sleep hours, activity level, and stress level to the assistance score.")

new_user = np.array([5, 40, 7])
predicted_score = new_user @ beta
print("Predicted assistance score for the new user:", predicted_score)
