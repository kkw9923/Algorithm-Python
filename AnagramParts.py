while True:
    try:
        theInput = input().split()

    except EOFError:
        break
    except KeyboardInterrupt:
        break


    inputList = []
    
    for i in theInput:
        alpha = list(i)
        inputList.append(alpha)
    print(inputList)


