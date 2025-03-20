
"""
the dump() and load() functions of pickle module respectively perform pickling and unpickling of python data
The dump() function writes the pickled object to a file and load() funtion unpickles data from file back to python object
"""

import pickle

# wb - write and binary mode
f = open("pickled.txt", "wb")
dct = {'name': 'Ruben', 'age': 45, 'Gender': 'Male', 'City': 'Los Angels'}
pickle.dump(dct, f)
f.close()

fl = open("pickled.txt", "rb")
res = pickle.load(fl)
print(res)
fl.close()


