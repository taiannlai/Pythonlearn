fstream1 = open("E:\Git\Pythonlearn\CH4\out1.txt", mode = "w")
print("Testing for output", file=fstream1)
fstream1.close()
fstream2 = open("E:\Git\Pythonlearn\CH4\out2.txt", mode = "a")
print("Testing for output", file=fstream2)
fstream2.close()