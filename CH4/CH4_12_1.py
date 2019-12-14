score = 90
name = "賴泰安"
count = 1
#以下是鼓勵使用
print("{0} 你的第 {1} 次物理考試成績是 {2}".format(name, count, score))
#以下是不鼓勵使用
print("{2} 你的第 {1} 次物理考試成績是 {0}".format(score, count, name))