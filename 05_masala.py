a=int(input("A kesma uzunligini kiriting: (m) A = "))
b=int(input("B kesma uzunligini kiriting: (m) B = "))
q=a%b
import math
if a>b>0 and q==0:
    print("A kesma ichida B kesmani ",math.floor(a/b)," marta joylashtirish mumkin.")
else:
    print("A kesma ichida B kesma ",math.floor(a/b)," marta joylashdi va ",q," metr masofa ortib qoldi")