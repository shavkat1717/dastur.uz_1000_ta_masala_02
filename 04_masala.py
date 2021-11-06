a=int(input("A kesma uzunligini kiriting A = "))
b=int(input("B kesma uzunligini kiriting B = "))
import math
if a>b>0:
    print("A kesma ichida B kesmani ",math.floor(a/b)," marta joylashtirish mumkin.")
else:
    print("A kesma B kesmadan katta va musbat bo'lishiga e'tibor bering!")