#!/usr/bin/python

import json

dataFileHandle = open("dataFile", "r")
content = dataFileHandle.read()
data = json.loads(content)
dataFileHandle.close()

for area in data:
    print area
    for coordinate in data[area]:
        print coordinate

