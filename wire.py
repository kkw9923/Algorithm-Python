"""
Problem Statement: Intersecting Wires

This problem is taken from a recent code.google.com/codejam contest. Although not required at the
time the problem specifications were given, we have modified a few of the constraints so you will (most
likely) need to implement an efficient divide-and-conquer algorithm to pass the CS320 harder data set.
An intranet company wants to connect two buildings with many wires, each connecting a port on the
first building to a port on the second building. Wires are straight segments connecting a vertical position
on the left building to a vertical position on the right building. No two wires share the same endpoint
on a building. However, from our side viewpoint, some of the wires intersect midway. We also noticed
that due to different tensions of the wires exactly two wires meet at any given intersection point.

Sample Input:
2
3
1 10
5 5
7 7
2
1 1
2 2

Sample Output (number of inversions):
Case #1: 2
Case #2: 0

For the main problem, output one line containing “Case #x: y”, where x is the case number and y is
the number of intersection points you see from the side vantage point.

"""


import sys

def sortAndCount(abList):
    if len(abList) == 1:
        return abList, 0
    
    else:
        median = len(abList)//2
        abList_rA, rA = sortAndCount(abList[:median])
        abList_rB, rB = sortAndCount(abList[median:])
        abList_rAB, rAB = mergeAndCount(abList_rA, abList_rB)
        return abList_rAB, rA+rB+rAB


def mergeAndCount(aList, bList):
    count = 0
    outList = []
    
    while aList and bList:
        if aList[0] <= bList[0]:
            outList.append(aList.pop(0))
        else:
            count += len(aList)
            outList.append(bList.pop(0))
                     
    outList += aList
    outList += bList
    return outList, count






n = 0
loop = int(sys.stdin.readline())
valueList = []

while(n < loop):

    inputNum = int(sys.stdin.readline())

    wires = []
    wireIndex0 = []
    
    for i in range(inputNum):
        wire = sys.stdin.readline().split()
        intWire = [[int(wire[0]), int(wire[1])]]       
        wires += intWire

    s_wires = sortAndCount(wires)[0]


    for j in range(inputNum):
        wireIndex0 += [s_wires[j][1]]


    n += 1
    output = sortAndCount(wireIndex0)
    print("Case #"+str(n)+": "+str(output[1]))








    
