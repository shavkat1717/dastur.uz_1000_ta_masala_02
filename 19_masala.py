a=int(input("Kun boshidan beri necha sekund o'tdi: => "))
import math
b=math.floor(a/60)
if b==0:
    print(" Ilk daqiqa o'tib bormoqda...")
else:
    print(f"Kun boshida beri {b} minut to'la o'tdi.")