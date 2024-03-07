"""02 -> Operators"""

"""Logical operators in Python, such as `and` and `or`, use a mechanism called short-circuit evaluation, which can improve performance and prevent unnecessary computations.  
1. Short-circuit evaluation with `and`:
In the `and` operator, if the first operand is `False`, the entire expression will be `False` regardless of the second operand else returns the 2nd operand. So, Python doesn't evaluate the second operand and simply returns `False`. This behavior is known as short-circuiting."""

print(False and "subrata")
print(False and "mondal")
print(True and "subrata")
print(True and "mondal")

"""2.Short-circuit evaluation with or:
In the or operator, if the first operand is True, the entire expression will be True regardless of the second operand. So, Python doesn't evaluate the second operand and simply returns True."""

print("subrata" or False)
print("mondal" or False)
print(False or "subrata")
print(False or "mondal")

"""Ternary Operator"""
# first value if (condition) else second value
age = 15
age_group = "adult" if age > 18 else "underage"
print(age_group)

# chaining of ternary operator
age_group = "adult" if age > 18 else ("teen" if age > 13 else "minor")
print(age_group)