def cur(): 

    import sys

    a = dir(sys)

    clean = []

    for i in range(0,len(a)):
        b = ""
        for j in range(0,len(a[i])):
            if j != "_":
                b += a[i][j]
        clean.append(a)

    print(clean)

cur()
