
"""
the pickle module also consists of dumps function that pickles python data to a byte object
"""

from pickle import  loads, dumps
dct = {'name': 'Margret', 'age': 32, 'Gender': 'Female', 'city': 'Las Vegas'}
print(f"dct :{dct}")

print("-" * 60)
dctString = dumps(dct)      # pickles to bytes
print(dctString)
print(type(dctString))


print("-" * 60)
# unpickle the byte object to obtain original dictionary object...
dctObj = loads(dctString)
print(dctObj)
