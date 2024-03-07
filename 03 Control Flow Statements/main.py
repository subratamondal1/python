"""03 Control Flow Statements"""

# If Statement:
print("\nIf Statement")
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Elif Statement:
print("\nElif Statement")
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
else:
    print("D")

# For Loop:
print("\nFor Statement")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop:
print("\nWhile Statement")
count = 0
while count < 5:
    print(count)
    count += 1

# Break Statement
print("\nBreak Statement")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

# Continue Statement
print("\nContinue Statement")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)