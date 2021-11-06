K=int(input(" Yil ichidagi 1 dan 365 oralig'ida kun kiriting: => "))
N=int(input(" 1-yanvar haftaning qaysi kuniga to'g'ri kelmoqda, [1;7] gacha kiriting: =>"))
import math
q=(K%7+N-1)
if 1<=K<=365 and 1<=N<=7:
    print(f"Ushbu {K}-kun haftaning {q}-kuniga to'g'i keladi!")
else:
    print("K yoki N shartlariga e'tibor bering!")