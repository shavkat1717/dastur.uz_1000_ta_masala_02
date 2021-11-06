a=int(input("Marhamat, istalgan ikki xonali son kiriting: = "))
import math
b=math.floor(a/10)
q=a%10
if 0<b<10:
    print(f"Ushbu {a} sonining raqamlari almashtirilib  {10*q+b} soni hosil qilindi")
else:
    print("Iltimos, ikki xonali son kiriting!")