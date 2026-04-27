total_sum = 0

age = int(input("Hi there! Please enter your age: "))

for i in range(1, age + 1):
    total_sum += i

print(f"The sum of all numbers from 1 to {age} is: {total_sum}")
