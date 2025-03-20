
"""
Json Module:
-> using the json module we can serialize and deserialize several standard Python types like
    bool, dict, int, float, list, string, tuple, None etc
-> good choice if we want to interoperability among different languages
"""

import json

# json string
data = {'name': 'Sachin', 'age': '35', 'runs': '98', 'oppn': 'West Indies'}
print(f"data :{data}")

print("-" * 60)
# serializing the json data
json_object = json.dumps(data)
print(json_object)
print("Serialization complete......")

print("-" * 60)
# convert it into python dictionary
player_dict = json.loads(json_object)
print(player_dict)

print(player_dict['name'])
print("Deserialization complete.....")