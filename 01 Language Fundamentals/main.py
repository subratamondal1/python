"""01 -> Language Fundamentals"""

"""
Note: In, python everything is an object, and each object is an instantiation of a class
Note: Each identifier (variable) has it's own memory address reference
"""

# this is a comment, starts with #

'This is a single line comment in Python'

"This is a single line comment in Python"

'''This is a multi-line 
comment in Python'''

"""This is a multi-line 
comment in Python"""

"""
Note: Comments are translated into machine code but they doesn't get executed
"""

print("Output in Python")
print("Hello World") # Hello World

# Fundamental Data Types
"""Integer: int()"""
print("\nInteger Datatype")

number = 5
print(type(number), "Memory Address", id(number)) # <class 'int'>
number = int(5)
print(type(number), "Memory Address", id(number)) # <class 'int'>

"""Float"""
print("\nFloat Datatype")
number = 5.0
print(type(number), "Memory Address", id(number)) # <class 'float'>
number = float(5.0)
print(type(number), "Memory Address", id(number)) # <class 'float'>

"""String"""
print("\nString Datatype")
name = "subrata"
print(type(name), "Memory Address", id(name)) # <class 'str'>
name = str(object="subrata")
print(type(name), "Memory Address", id(name)) # <class 'str'>

"""Boolean"""
print("\nBoolean Datatype")
is_ok = True
print(type(is_ok), "Memory Address", id(is_ok)) # <class 'bool'>
is_ok = bool(True)
print(type(is_ok), "Memory Address", id(is_ok)) # <class 'bool'>

"""Complex"""
print("\nComplex Datatype")
complex_number = 2 + 5j
print(type(complex_number), "Memory Address", id(complex_number)) # <class 'complex'>
complex_number = complex(real=2, imag=5)
print(complex_number) # (2+5j)
print(type(complex_number), "Memory Address", id(complex_number)) # <class 'complex'>

"""Binary number System: Base or Radix is 2 (0 & 1)"""
print("\nBinary number System: Base or Radix is 2 (0 & 1)")
binary_number = bin(100)
print(binary_number) # 0b1010
print(type(binary_number), "Memory Address", id(binary_number)) # <class 'str'>

"""Octal number System: Base or Radix is 8 (0-7)"""
print("\nOctal number System: Base or Radix is 8 (0-7)")
octal_number = oct(100)
print(octal_number) # 0o12
print(type(octal_number), "Memory Address", id(octal_number)) # <class 'str'>

"""Hexa Decimal number System: Base or Radix is 16 (0-9 & A-F)"""
print("\nHexa Decimal number System: Base or Radix is 16 (0-9 & A-F)")
hexa_decimal_number = hex(100)
print(hexa_decimal_number) # 0x64
print(type(hexa_decimal_number), "Memory Address", id(hexa_decimal_number)) # <class 'str'>

"""
Immutable Datatypes: Once created, it can't be updated at the same memory address, if 
updated then a new object is created with same name at different memory address.
Fundamental datatypes are all Immutable: 
 - int, 
 - float, 
 - str, 
 - bool, 
 - complex and also 
 - tuple & frozenset
"""
print("\nImmutable: String")
name = "Subrata"
print(id(name), "Memory Address", id(name))
# name[1] = "m" # TypeError: 'str' object does not support item assignment
name = "Mondal"
print(id(name), "Memory Address", id(name))


"""Lists are sequence, contains group of elements of any datatype
- Ordered hence Indexable hence Sliceable
- Contains duplicate elements
- Mutable
"""

print("\nLists are mutable, hence on update, Memory Address remains same")
store = [2,3,4,5, "abc", 1.0]
print(store) # [2, 3, 4, 5, 'abc', 1.0]
print(type(store), "Memory Adress", id(store))
store[2] = "No"
print(store) # [2, 3, 'No', 5, 'abc', 1.0]
print(type(store), "Memory Adress", id(store))

"""Tuple (Read-Only List) are sequence, contains group of elements of any datatype
- Ordered hence Indexable hence Sliceable
- Contains duplicate elements
- Immutable
"""

print("\nTuples are immutable, hence on update, Memory Address changes")
store = (2,3,4,5, "abc", 1.0)
print(store) # (2, 3, 4, 5, 'abc', 1.0)
print(type(store), "Memory Adress", id(store))
# store[2] = "No" # TypeError: 'tuple' object does not support item assignment
store = (2, 3, 'No', 5, 'abc', 1.0)
print(store) # (2, 3, 'No', 5, 'abc', 1.0)
print(type(store), "Memory Adress", id(store))

"""Sets are sequence, contains group of elements of any datatype
- Un-Ordered hence Not-Indexable hence Not-Sliceable
- Doesn't contain duplicate elements
- mutable
"""

print("\nSets are mutable, hence on update, Memory Address remains same")
store = {2,3,4,5, "abc", 1.0}
print(store) # [2, 3, 4, 5, 'abc', 1.0]
print(type(store), "Memory Adress", id(store))
store.add("No")
print(store) # {1.0, 2, 3, 4, 5, 'abc', 'No'}
print(type(store), "Memory Adress", id(store))

"""Frozensets are sets but Immutable"""
print("\nFrozensets are immutable, hence can't update, on same Memory Address")
store = frozenset({2,3,4,5,"abc",1.0})
print(store) # frozenset({1.0, 2, 3, 'abc', 4, 5})
print(type(store), "Memory Adress", id(store))
store = frozenset({"ok", 65, 44})
print(store) # frozenset({65, 44, 'ok'})
print(type(store), "Memory Adress", id(store))


"""Dictionaries are key-value pairs data container
- Un-Ordered hence Not-Indexable hence Not-Sliceable
- Doesn't contain duplicate keys
- mutable
"""
print("\nDictionaries are mutable, hence on update, Memory Address remains same")
store = {1:"subrata", 2:"apple", 3:"silicon"}
print(store) # {1: 'subrata', 2: 'apple', 3: 'silicon'}
print(type(store), "Memory Adress", id(store))
store[3] = "valley"
print(store) # {1: 'subrata', 2: 'apple', 3: 'valley'}
print(type(store), "Memory Adress", id(store))

# Mutability & Immutability
print("\nOrdered Immutable String's Memory Address Remains Same on Modification")
immutable_string = "Subrata"
print(immutable_string, id(immutable_string))
immutable_string = "Mondal"
print(immutable_string, id(immutable_string))

print("\nOrdered Mutable List's Memory Address Changes on Modification")
mutable_list = [12, 13, 14, "subrata"]
print(mutable_list, id(mutable_list))
mutable_list.append("mondal")
print(mutable_list, id(mutable_list))

print("\nOrdered Immutable Tuple's Memory Address Changes on Modification")
immutable_tuple = (12, 13, 14, "subrata")
print(immutable_tuple, id(immutable_tuple))
immutable_tuple=(12, 13, 14, "subrata", "mondal")
print(immutable_tuple, id(immutable_tuple))

print("\nUnordered Mutable Set's Memory Address Remains same on Modification")
mutable_set = {12, 13, 14, "subrata"}
print(mutable_set, id(mutable_set))
mutable_set.add("mondal")
print(mutable_set, id(mutable_set))

print("\nUnordered Mutable Dict's Memory Address Remains same on Modification")
mutable_dict = {"id": 1232, "name": "subrata"}
print(mutable_dict, id(mutable_dict))
mutable_dict.update({"title":"mondal"})
print(mutable_dict, id(mutable_dict))