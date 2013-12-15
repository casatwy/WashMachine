#!/usr/bin/python
# coding: utf-8

import json
import math
import string
import encodings

def findClosestPointWithPoint(data, area, point):
    result = {}

    resultPoint = []
    resultArea = ""
    minDistance = 9999

    for tArea in data:
        if tArea == area:
            continue
        for coordinate in data[tArea]:
            distance = distanceWithPoints(coordinate, point)
            if distance < minDistance:
                minDistance = distance
                resultPoint = coordinate
                resultArea = tArea

    result['point'] = resultPoint
    result['area'] = resultArea
    result['distance'] = minDistance

    return result

def distanceWithPoints(pointA, pointB):
    result = math.sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)
    return result

def isInland(area):

    inlandArea = [
            "上海市卢湾",
            "上海市闵行",
            "上海市闸北",
            "上海市松江",
            "上海市杨浦",
            "上海市黄浦",
            "上海市虹口",
            "上海市徐汇",
            "上海市长宁",
            "上海市静安",
            "上海市普陀"
            ]

    area = area.encode("utf-8")
    print "inland %s" % area

    result = False
    for tArea in inlandArea:
        if tArea == area:
            result = True
            break
    print "inland result %s" % result
    return result

def washData(data):

    keys = data.keys()

    for area in keys:
        for coordinate in data[area]:

            result = findClosestPointWithPoint(data, area, coordinate)
            validateResult = findClosestPointWithPoint(data, result["area"], result["point"])

            if isInland(area):
                coordinate[0] = result["point"][0]
                coordinate[1] = result["point"][1]
                continue

            if validateResult["point"] == coordinate:
                print "success %s" % result
                if result["distance"] != 0:
                    coordinate[0] = result["point"][0]
                    coordinate[1] = result["point"][1]
            else:
                print "fail %s" % result
    return data

dataFileHandle = open("dataFile", "r")
content = dataFileHandle.read()
data = json.loads(content)
dataFileHandle.close()

# make string into float
for area in data:
    for coordinate in data[area]:
        coordinate[0] = string.atof(coordinate[0])
        coordinate[1] = string.atof(coordinate[1])

data = washData(data)

content = json.dumps(data)
print content
dataFileHandle = open("resultFile", "w")
dataFileHandle.write(content)
dataFileHandle.close()
