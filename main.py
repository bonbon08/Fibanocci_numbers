def next_num(n1, n2):
    return n1+n2, n1
n1 = 1
n2 = 0
while True:
    n1, n2 = next_num(n1, n2)
    print(n1)
