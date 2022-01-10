fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break

# for -2
for x in range(6):
    print(x)

# third
z = [1, 2, 1, 3]

for y in z:
    if y == 3:
        print(y)

# nested loops

adj = ["red", "big", "tasty", "apple"]
fruits = ["apple", "banana", "cherry"]

for p in adj:
    for m in fruits:
        if p == m:
            print(p, m)

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
num = 10

# iterate over the list
for val in numbers:
    num = num-val
    print(val)

print("The sum is", num)

#
# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])





































