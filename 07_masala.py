a=int(input("Marhamat, istalgan ikki xonali son kiriting: = "))
import math
b=math.floor(a/10)
q=a%10
if 0<b<10:
    print(f"Ushbu {a} sonning raqamlari yig'indisi: {b+q} ga teng")
else:
    print("Iltimos, ikki xonali son kiriting!")