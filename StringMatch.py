aList = []
storeList = []
count = 0
index = 0
try:
    while True:
        try:
            anInput = input()
            aString = anInput.split()
            storeList.append(aString)
            compareDict = {}
            s = storeList[index][0]
            t = storeList[index][1]

                
            for i in range(len(s)):
                if s[i] not in compareDict and s[i] not in compareDict.values() and t[i] not in compareDict.values():
                    compareDict[s[i]] = t[i]
                elif (s[i] in compareDict and compareDict[s[i]] != t[i]) or (s[i] not in compareDict and t[i] in compareDict.values()):
                    count += 2
                    index += 1
                    aList.append("False")
                    break
                    
            else:        
                count += 2
                index += 1
                aList.append("True")

        except KeyboardInterrupt:
            raise
            
            
except KeyboardInterrupt:
    for j in range(len(aList)):
        print(str(aList[j]))
    
    
  

