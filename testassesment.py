def parking(N,b,c):
    list(b)
    list(c)
    count = 0 
    toc = []
    todayspots = []
    for i in range (0, N):
        if b[i] == "C" and c[i] == "C": 
            count = count + 1
            # print(count)`
    print(count)
parking(5,"C..C.","CC.C.")
