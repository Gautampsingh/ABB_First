
"""
Python Object Persistence - shelve

-> shelve in python standard library is a simple yet effective tool for persistent data storage when you don't really need a relational database solution.

-> the 'Shelf' object defined in this module is dictionary like object which is persistently stored in a disk file.

-> this creates a file similar to dbm database on UNIX like systems.

-> However, objects of only stirng type is allowed as key in this special dictionary object

value however can be any picklable object
"""
"""
The shelve module defines three classes as follows

Shelf    : This is the base class for shelf implementations.
           It is initialized with dict-like object.

BsdDbsShelf : This is a subclass of Shelf class.
              The dict object passed to its constructor must support 
              first(), next(), previous(), last() and set_location() methods.

DbfilenameShelf : this is also a subclass of Shelf but accepts a filename as parameter to its constructor rather than dict object.

The Shelf object has the following methods

close()     : Synchronise and close persistent dict object
sync()      : Write back all entries in the cache of shelf was opened with writeback set to True
get()       : returns value associated with key
items()     : list of tuples - each tuple is key value pair
keys()      : list of Shelf keys
pop()       : Remove specified keyand return corresponding value
update()    : update shelf from another dict/iterable
values()    : list of shelf values
"""

import shelve

s1 = shelve.open("hello")    # creates a file
s1['name'] = "Sachin"
s1['age'] = 36
s1['city'] = 'Mumbai'
s1.close()

s2 = shelve.open("hello")
print(s2['name'])
print(s2['age'])
print(s2['city'])
# s2.close()

print("-" * 60)
print(list(s2.items()))
print(list(s2.keys()))
print(list(s2.values()))

print(s2.get('name'))

d = {'name': 'Tendulkar', 'salary': 25000, 'desig': 'MGR'}
s2.update(d)
print(list(s2.items()))
res = s2.pop('age')
print(f"res :{res}")

print(list(s2.items()))
