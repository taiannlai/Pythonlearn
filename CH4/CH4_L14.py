import math

r = 6371        # 地球半徑
x1, y1 = eval(input("請輸入第一個點的經緯度：")) #24.141074, 120.613395  我家的經緯度
x2, y2 = eval(input("請輸入第二個點的經緯度："))#24.164831, 120.593562  振鋒

d = 6371 * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2))+math.cos(math.radians(x1)) * math.cos(math.radians(x2)) * math.cos(math.radians(y1-y2)))

print("distance = ", d)