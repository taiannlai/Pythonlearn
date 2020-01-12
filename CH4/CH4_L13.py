import math
n = eval(input("請輸入為哪一種多邊形："))
s = eval(input("請輸入正多邊形邊長："))
area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("area = ", area)