v = eval(input("請輸入飛機起飛的速度："))
a = eval(input("請輸入飛機的加速度："))
distance = v **2 / (2*a)
print("飛機起飛時所需的跑道長度為：%10.2d" % distance)