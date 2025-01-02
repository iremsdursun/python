import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k)**3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)  # En hızlı çizim
bgcolor("black")
penup()  # Çizim başlamadan önce penup, hareketsizken çizim yapmıyoruz
goto(hearta(0) * 20, heartb(0) * 20)
pendown()  # Çizmeye başla

for i in range(6000):  # 6000 adımda çizimi yapacak
    goto(hearta(i) * 20, heartb(i) * 20)
    color("red")  # Renk her adımda değişir
penup()  # Çizim bittiğinde kalemi kaldır
done()       
