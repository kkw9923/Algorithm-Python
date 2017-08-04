"""
Problem Statement 2: Computing Gale-Shapley Matching

The input format for this problem is the same as in Problem 1 but does not have a proposed matching.
This is what your implementation of the Gale-Shapley algorithm should compute. Write the matching
(a permutation of the women’s names) on a single line for each test case.

Sample Input:
2
2
W2 W1
W1 W2
M1 M2
M1 M2
3
W1 W2 W3
W2 W1 W3
W1 W2 W3
M2 M1 M3
M1 M2 M3
M1 M2 M3

Sample Output:
W2 W1
W1 W2 W3

"""

inputTest = int(input())
n = 0



while(n < inputTest):
    inputNumber = int(input())
    loop = inputNumber*2
    
    freeList = {}
    men = {}
    women = {}
    for i in range(1,loop+1):
        if i < inputNumber+1:
            men['M'+str(i)] = input().split()
        else:
            women['W'+str(i-inputNumber)] = input().split()
    
    output = ''
    matchedList = {}
    freeM = []
    for x in range(1,inputNumber+1):
        freeM += ['M'+str(x)]



    man_index = 1
    y = 0
    while (freeM != []):
        man = 'M'+str(man_index)
        if man in matchedList.keys():
            man_index += 1
        elif men[man][y] not in matchedList.values():
            matchedList[man] = men[man][y]
            freeM.remove(man)
            #break
            y = 0
            man_index += 1
        else:
            for key in matchedList:
                if matchedList[key] == men[man][y]:
                    compare_index = key
            compare_w = men[man][y]

            if women[compare_w].index(compare_index) > women[compare_w].index(man):
                matchedList[man] = men[man][y]
                freeM.append(compare_index)
                del matchedList[compare_index]
                freeM.remove(man)
                #break
                y = 0
                man_index = 1
            else:
                y += 1
                    
                

    #for p in range(1,inputNumber+1):
        #if len(output) == 0:
    output += matchedList['M'+str(1)]
        #else:
    for p in range(2,inputNumber+1):
        output += ' ' + matchedList['M'+str(p)]


    print(output)
    n += 1

