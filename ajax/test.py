

import json

fdata = open('test','r')

data = fdata.read()

data = json.loads(data)

print(data['name'])
