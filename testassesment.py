# def parking(N,b,c):
#     list(b)
#     list(c)
#     count = 0 
#     toc = []
#     todayspots = []
#     for i in range (0, N):
#         if b[i] == "C" and c[i] == "C": 
#             count = count + 1
#             # print(count)`
#     print(count)
# parking(5,"C..C.","CC.C.")

def engfrec(N,text):
 linecount = text.split(".", "!", "?")
 tc = 0
 sc = 0
 for "S" or "s" in text:
     sc =  sc + 1 
       
#  for line in range (0, ):
#      s = text[line].count("s")
#      S = text[line].count("S")
#      sc = S + s
#      T = text[line].count("T")
#      t = text[line].count("t")
#      tc = T + t 
    for "S" or "S=s" in text: 
    if tc > sc:
            print(" English")
    if sc > tc: 
            print("French")
    if sc ==  tc:
            print("probably French")

def LANG(sent):
 s = 0
 t = 0
 for i in sent: #checks each character
      if i.lower == s: # if i == "s" or i == "S"
        s+=1
      elif i.lower == t: # USE ELIF. PREVENT BUGS 
        t+=1
 if s>= t: 
    print("French")
 else:
     print("English")
LANG("Ten thousand things")
