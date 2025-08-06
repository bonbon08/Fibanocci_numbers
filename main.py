print("1 : 1")
n1 = 1
n2 = 0
for i in range(100):
    nt = n1
    n1 = n1 + n2
    n2 = nt
    print(i+2, " : ", n1)
