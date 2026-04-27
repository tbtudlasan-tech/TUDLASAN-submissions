# Creating a list
print("Creating a fruits list")
fruits = ["apple", "banana", "cherry"]
print(f"{fruits}")
print("------------------------------------")

# Print the second item of the list
print("Getting the second item of fruits list:", end = " ")
print(f"{fruits[1]}")   # Python lists are Zero-based Index; first item is index 0,
                        # second item is index 1, third is index 2, etc.
print("------------------------------------")

# Change the second item
print("Changing the second item of fruits list:")
print(f"Old list:\t{fruits}")
fruits[1] = "blackcurrant"
print(f"Updated list:\t{fruits}")
print("------------------------------------")

# len() determines how many items a list has
print("Getting length of fruits list using len():", end = " ")
length = len(fruits)
print(length)
print("------------------------------------")

# count() counts the number of elements with the specified value.
print("Counting number of blackcurrant using count():", end = " ")
x = fruits.count("blackcurrant")
print(x)
print("------------------------------------")

# index() gets the position at the first occurrence of the specified value.
print("Getting the first index of cherry using index():", end = " ")
y = fruits.index("cherry")
print(y)
print("------------------------------------")

# insert() inserts an item at the specified index
print("Adding watermelon at index 2 of fruits list using insert():")
print(f"Old list:\t{fruits}")
fruits.insert(2, "watermelon")
print(f"Updated list:\t{fruits}")
print("------------------------------------")

# append() adds an item to the end of the list
print("Adding orange at the end of fruits list using append():")
print(f"Old list:\t{fruits}")
fruits.append("orange")
print(f"Updated list:\t{fruits}")
print("------------------------------------")

# remove() removes the specified item
print("Removing blackcurrant at the end of fruits list using remove():")
print(f"Old list:\t{fruits}")
fruits.remove("blackcurrant")
print(f"Updated list:\t{fruits}")
print("------------------------------------")
# If there are more than one item with the specified value,
# remove() removes the first occurence
# newFruit = ["apple", "banana", "orange", "mango", "banana"]
# newFruit.remove("banana")
'''output: ['apple', 'orange', 'mango', 'banana']'''

# pop() removes the specified index
print("Removing the index 1 list using pop():")
print(f"Old list:\t{fruits}")
fruits.pop(1)
print(f"Updated list:\t{fruits}")
print("------------------------------------")
# If you do not specify the index,
# pop() removes the last item
# newFruit = ["apple", "banana", "orange", "mango"]
# newFruit.pop()
'''output: ['apple', 'banana', 'orange']'''

# clear() empties the list
# The list still remains, but it has no content.
print("Clearing the list using clear():")
print(f"Old list:\t{fruits}")
fruits.clear()
print(f"Updated list:\t{fruits}")
print("------------------------------------")


fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]
print(f"\nFor the next few methods, we will be using this list: {fruits}")

# sort() sorts the list alphanumerically, ascending, by default
print("Sorting the list alphanumerically ascending using sort():")
print(f"Old list:\t{fruits}")
fruits.sort()
print(f"Updated list:\t{fruits}")
print("------------------------------------")

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]

# To sort desending, use the keyword argument reverse = True
print("Sorting the list alphanumerically descending using sort(reverse = True):")
print(f"Old list:\t{fruits}")
fruits.sort(reverse = True)
print(f"Updated list:\t{fruits}")
print("------------------------------------")

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]

# reverse() reverses the current sorting order of the elements
print("Reversing the list using reverse():")
print(f"Old list:\t{fruits}")
fruits.reverse()
print(f"Updated list:\t{fruits}")
print("------------------------------------")

fruits = ["orange", "mango", "kiwi", "pineapple", "banana"]

# copy() copies a list
print("Creating a new list newFruits that is a copy of fruits list using copy():")
newFruits = fruits.copy()
print(f"fruits list:\t{fruits}")
print(f"newFruits list:\t{newFruits}")
print("------------------------------------")

# sorted() is the combination of sort() and copy()
# sorted() returns a sorted list
print("Creating a new list newerFruits that is a sorted copy of fruits list using sorted():")
newerFruits = sorted(fruits)
print(f"fruits list:\t{fruits}")
print(f"newerFruits:\t{newerFruits}")
print("------------------------------------")

a = [1, 5, 3, 9]
print(f"\nFor the next few methods, we will be using this list: {a}")
# max() gets the item with the highest value
# min() gets the item with the lowest value
# sum() gets the sum of all items
i = max(a)
j = min(a)
k = sum(a)
print(f"Getting max of list using max(): {i}")
print(f"Getting min of list using min(): {j}")
print(f"Getting sum of list using sum(): {k}")