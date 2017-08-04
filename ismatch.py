"""
Problem Statement 1: Checking Stable Matching

You are to read in a sequence of matching preferences and a proposed matching and determine if it is
perfect and stable.

This is then followed
by n lines of (white-space separated) preferences for the men and n lines of preferences for the women.
For convenience we assume men’s and women’s names are of the form M i and W i, for 1 ≤ i ≤ n. The
last line of each test case consists of the proposed matching. It will be a sequence of n women’s names,
where the i-th name given is matched to the man M i.


Sample Input:
2
3
W1 W2 W3
W2 W1 W3
W1 W2 W3
M2 M1 M3
M1 M2 M3
M1 M2 M3
W1 W2 W3
3
W1 W2 W3
W2 W1 W3
W1 W2 W3
M2 M1 M3
M1 M2 M3
M1 M2 M3
W3 W2 W1


Sample Output:
Yes
No

"""




inputTest = int(input())
n = 0


while(n < inputTest):
    inputNumber = int(input())
    loop = inputNumber*2+1
    
    
    men = {}
    women = {}
    pw = []
    pair = {}
    for i in range(1,loop+1):
        if i < inputNumber+1:
            men['M'+str(i)] = input().split()
        elif i == loop:
            pw += input().split()
        else:
            women['W'+str(i-inputNumber)] = input().split()

    for j in range(len(pw)):
        pair[pw[j]] = 'M'+str(j+1)

    
    output = 0  
    count = 0
    
    for x in range(1,inputNumber+1):
        orig_m = 'M'+str(x)
        w = pw[count]
        index = men[orig_m].index(w)
        prefer = men[orig_m][:index]

        y = index
        for y in prefer:
            m = pair[y]
            if women[y].index(orig_m) < women[y].index(m):
                output = 1
                break
            
        count += 1

        



    if output == 0:
        print("Yes")
    else:
        print("No")
    

    n += 1
