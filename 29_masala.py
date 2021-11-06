A=int(input("To'g'ri to'rtburchakning enini kiriting: A = "))
B=int(input("To'g'ri to'rtburchakning enini kiriting: B = "))
C=int(input("Kvadratning tomonini kiriting: C = "))
import math
x=math.floor(A/C)
y=math.floor(B/C)
n=x*y
Sq=A*B-n*C**2
print(f" Mazkur to'g'ri to'rtburchakning ichiga {n} ta kvadratni joylashtirish mumkin, Qoldiq yuza {Sq} ga teng!")