K=int(input(" 1 dan 365 oralig'ida son kiriting: => "))
hafta=["Yakshanba","Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba"]
import math
h=math.floor(K/7)
q=K-h*7
if 4>q and q<7:
    print(q+3)
else:
    print(q-4)