a=int(input("Kun boshidan beri necha sekund o'tdi: => "))
import math
s=math.floor(a/3600)
q=a-s*3600
m=math.floor(q/60)
c=q-m*60
if m<60:
    print(f"Kun boshidan beri {s} soat, {m} minut-u, {c} sekund o'tdi.")