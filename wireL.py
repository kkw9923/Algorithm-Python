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

Sample Output (longest wires):
Case #1: 1
Case #2: 1 2

We have two problems. The first problem checks if you can read the input and compute a list of wires
that are the longest in length. With x being the case number, output a single line containing “Case
#x: ” followed by a single white-space separated list in increasing order of wires (starting at index 1).

"""

def compare(v1, v2):
    if(int(v1) > int(v2)):
        value = int(v1)-int(v2)
    else:
        value = int(v2) - int(v1)

    return value


n = 0
loop = int(input())

while(n < loop):

    inputNum = int(input())
    largeValue = 0
    lvList = []
    lvDict = {}
    for i in range(1, inputNum+1):
        wire = input().split()
        lvDict[i] = wire
        value = compare(wire[0], wire[1])

        if(len(lvList) > 0):
            if(value > largeValue):
                largeValue = value
                lvList = [i]
            elif(value == largeValue):
                lvList += [i]
        else:
            largeValue = value
            lvList = [i]

        #print(lvList, 'lvList')
    #print(lvDict, 'lvDict')

    output = str(lvList[0])
    for j in range(1, len(lvList)):
        output += " "+ str(lvList[j])

    n += 1
    print("Case #"+ str(n)+ ": "+ str(output))
