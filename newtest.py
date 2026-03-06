""" def honi(text):
    honicount = 0
    need = ["H","O","N","I"]
    y = 0 
    honi_part_counter = 0 
    honi_count = 0
    for n in text:
        if n == need[y]:
            y=+ 1
            honi_part_counter + 1 == honi_part_counter
            if y > 3:
                y = 0 
    (honi_part_counter // 4) == honi_count
    print(honi_count)
honi("HONI")


def magnus(word):
    count = 0
    state = 0
    for char in word:
     if state == 0 and char.upper() =="H":
         state = 1
    elif state == 1 and char.upper() =="O":
    state = 2
     elif state == 2 and char.upper() =="N":
          state = 3
    elif state == 3 and char.upper() =="I":
          state = 1
          count += 1
    print(count) """
dataper = 0
datat = 0
monthsc = 0 
monts = [] 
x = 0
def datacount(dataper,monthsc,monts):
    for i in range (0,monthsc):
        datat = datat + int(dataper)
        datat = datat - int(monts[x])
        x + 1
    print(datat)
datacount(10,3,"4,6,3")