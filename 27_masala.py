K=int(input(" 1 dan 365 oralig'ida son kiriting: => "))
hafta=["Yakshanba","Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba"]
import math
h=math.floor(K/7)
q=K-h*7
if q>1:
    print(q-1)
else:
    print(q+6)