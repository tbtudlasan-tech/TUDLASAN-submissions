import numpy as np

# # Create a 1D empty array of a specific size
# empty_array_1d = np.empty(5) 
# print(f"1D Empty Array:\n{empty_array_1d}\n")

# # Create a 2D empty array with a specific shape (rows, columns)
# empty_array_2d = np.empty((3, 4)) 
# print(f"2D Empty Array:\n{empty_array_2d}\n")

# # Create an empty array with a specific data type
# empty_array_int = np.empty((2, 2), dtype=int)
# print(f"Empty Array with integer dtype:\n{empty_array_int}\n")

# # Create a truly empty array with zero elements
# truly_empty_array = np.empty(0)
# print(f"Truly Empty Array (0 elements):\n{truly_empty_array}")

#Converting a list to NumPy array
# my_list = [1, 2, 3, 4, 5]
# numpy_array = np.array(my_list)

print("Creating a 2D fruits array using numpy")
fruits_2d = np.array([
    ["apple", "banana", "cherry"],
    ["orange", "mango", "kiwi"]
])
print(f"{fruits_2d}")
print("------------------------------------")

# Accessing elements
print("Getting element at row 1, column 2:", fruits_2d[1, 2])  # 'kiwi'
print("------------------------------------")

# Changing an element
print("Changing element at row 0, column 1:")
print(f"Old array:\n{fruits_2d}")
fruits_2d[0, 1] = "blackcurrant"
print(f"Updated array:\n{fruits_2d}")
print("------------------------------------")

# Shape of the array
print("Getting shape of 2D array (rows, columns):", fruits_2d.shape)
print("------------------------------------")

# Flatten the array
print("Flattening the 2D array to 1D using flatten():")
flat_fruits = fruits_2d.flatten()
print(flat_fruits)
print("------------------------------------")

# Transpose of the array
print("Transposing the 2D array using transpose():")
transposed_fruits = fruits_2d.T
print(transposed_fruits)
print("------------------------------------")

# Adding a new row
print("Adding a new row ['pineapple', 'grapes', 'watermelon'] using vstack():")
new_row = np.array([["pineapple", "grapes", "watermelon"]])
fruits_2d = np.vstack([fruits_2d, new_row])
print(fruits_2d)
print("------------------------------------")

# Adding a new column
print("Adding a new column ['papaya', 'strawberry', 'mango'] using hstack():")
new_col = np.array([["papaya"], ["strawberry"], ["mango"]])
fruits_2d = np.hstack([fruits_2d, new_col])
print(fruits_2d)
print("------------------------------------")

# Deleting a row
print("Deleting the second row using delete():")
fruits_2d = np.delete(fruits_2d, 1, axis=0)  # axis=0 for rows
print(fruits_2d)
print("------------------------------------")

# Deleting a column
print("Deleting the last column using delete():")
fruits_2d = np.delete(fruits_2d, -1, axis=1)  # axis=1 for columns
print(fruits_2d)
print("------------------------------------")

# Sorting along each row
print("Sorting each row alphanumerically using sort():")
fruits_2d.sort(axis=1)
print(fruits_2d)
print("------------------------------------")

# Copying array
print("Creating a copy of the 2D array using copy():")
fruits_copy = fruits_2d.copy()
print(f"Original:\n{fruits_2d}\nCopy:\n{fruits_copy}")
print("------------------------------------")

# Using shape, size, and ndim
print(f"Number of rows and columns: {fruits_2d.shape}")
print(f"Total number of elements: {fruits_2d.size}")
print(f"Number of dimensions: {fruits_2d.ndim}")