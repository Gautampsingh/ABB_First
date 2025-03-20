"""
Marshal is the oldest module, Not recommended to use mainly used by the interpreter
"""
import marshal

data = {'name': 'sachin', 'age': 35, 'runs': 120, 'oppn': 'Aus'}
print(f"data :{data}")

# dumps() return byte object stored in variable 'byte', this function is used to write the supported type value on the open writable binary file.

bytes = marshal.dumps(data)
print("After serialization :", bytes)

print("-" * 60)
# loads - convert the byte object into values
new_data = marshal.loads(bytes)
print("After desirialization :", new_data)
