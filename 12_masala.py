a=int(input("Marhamat, istalgan uch xonali son kiriting: = "))
import math
b=math.floor(a/100)
s=a-b*100
y=math.floor(s/10)
q=s%10
if 0<b<10:
    print(f"Ushbu {a} sonining raqamlarini teskari tartibda yozilishidan hosil bo'lgan son: {100*q+10*y+b} ga teng.")
else:
    print("Iltimos, uch xonali son kiriting!")