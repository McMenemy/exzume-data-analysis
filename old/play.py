import pandas as pd
from pandas import DataFrame
import json

data = [{'v1': 2, 'v2': 3},
        {'v1': 3, 'v2': 4},
        {'v1': 4, 'v2': None},
        {'v1': 5, 'v2': 4},
        {'v1': None, 'v2': 5}]
print(data[0])
print(data[0]['v1'])
df = pd.DataFrame(data)

print(df)
print(df.corr())
print(df.describe())
dict = {'arr': [{'a':1}, {'b':2}]}
print('here!!!')
print(dict['arr'][0])

JSON_Datalist = '[{"id":"XXXX", "name": null, "user" : { "id": "XXXX", "username":"XYZ", "group":{"id": "XXXX"}}}]'
the_dict = json.loads(JSON_Datalist)
print(the_dict)
print(the_dict[0]['id'])
