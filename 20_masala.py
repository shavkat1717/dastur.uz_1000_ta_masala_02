a=int(input("Kun boshidan beri necha sekund o'tdi: => "))
import math
b=math.floor(a/3600)
if b==0:
    print(" Birinchi soat hali endi o'tib bormoqda...")
else:
    print(f"Kun boshidan beri {b} soat to'la o'tdi.")