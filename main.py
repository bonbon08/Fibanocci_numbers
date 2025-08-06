print("1 : 1")
n1 = 1
n2 = 0
for i in range(100):
    n1, n2 = n1+n2, n1
    print(i+2, " : ", n1)
