a=int(input("Marhamat, istalgan 999 dan katta son kiriting: = "))
import math
b=math.floor(a/1000)
if b>0:
    s=a-b*1000
    y=math.floor(s/100)
    print(y)
else:
    print("Kamida 4 xonali son kiriting!")