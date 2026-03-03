def honi(text):
    honicount = 0
    need = ["H","O","N","I"]
    y = 0 
    for x in text:
        print(need[y])
        if x == need[y]:
            y=+1 
        elif x == need[y]:
            y=+1 
        elif x == need[y]:
            y=+1
        elif x == need[y]:
            honicount = honicount + 1
        else:
            y=+ 1
    print(honicount)

        

honi("HONI")


            