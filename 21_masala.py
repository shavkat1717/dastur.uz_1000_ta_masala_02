a=int(input("Kun boshidan beri necha sekund o'tdi: => "))
import math
b=math.floor(a/60)
q=a-b*60
if b==0:
    print(f"Kun boshidan beri {a} minut o'tdi.")
else:
    print(f"Kun boshidan beri {b} minut-u, {q} sekund o'tdi.")