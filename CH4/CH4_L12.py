x1, y1 = eval(input("請輸入第一個點的座標："))
x2, y2 = eval(input("請輸入第二個點的座標："))
x3, y3 = eval(input("請輸入第三個點的座標："))
dist1 = (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** 0.5
dist2 = (((x1 - x3) ** 2) + ((y1 - y3) ** 2)) ** 0.5
dist3 = (((x2 - x3) ** 2) + ((y2 - y3) ** 2)) ** 0.5

p = (dist1 + dist2 +dist3) / 2
print("三角形面績：%10d" %p)