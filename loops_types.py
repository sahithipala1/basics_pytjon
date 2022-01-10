y = "banana"
for x in y:
    print(x)

# for loop : if you select "a" for number of words in a string times

a = "banana"
for x in a:
    print(a)

print(len(x))
print(len(a))

# if else
text = "The best things"
if "The" in text:
    print("yes its present")

# if else
if "best" in text:
    print("True")

# upper()
z = "zipper"
print(z.upper())

# format strings
quantity = 4
item_no = 3000
price = 50
my_order = "i want to pay {2} dollars for {0} pieces of item no is {1}."
print(my_order.format(quantity,item_no, price))


# " " in the middle of text
name = "my name is \"john\" "
print(name)

# Booleans
print(10 > 9)
print(10 == 20)
print(29 < 23)


# Boolean 2
a = 199
b = 399

if b < a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# bool 3
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# bool
def myfunc():
    return False

print(myfunc())

# module operator means reminder
x = 151
y = 2

print(x%y)

# lists

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print(len(thislist))

# for loop
fruits = ["apple", "banana", "mango", "strawberry"]
new_list = [ x for x in fruits if x != "a"]
print(new_list)

#for loop
x = [1,1,2,2,3]
for i in x:
    print(i)

print(x)

# comprehension lists

new_list = [ x for x in range(10) if x < 5]
print(new_list)

# tuples
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# tuples 2
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, *yellow, red) = fruits

print(green)
print(yellow)
print(red)



















