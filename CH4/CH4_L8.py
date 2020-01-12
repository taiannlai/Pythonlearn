airate = input("請輸入年利率：")
year = input("請輸入存款年數：")
money = 50000 * (1 + float(airate)) ** float(year)
print("本金和是 %7d" % money)