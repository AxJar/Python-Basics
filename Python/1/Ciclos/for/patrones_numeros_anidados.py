for i in range(1, 6 + 1):
    for j in range(6, 0, -1):
        print(j if j <= i else " ", end = " ")
    print()

print()

for i in range(6+1):
    for j in range(i):
        print(" ", end = " ")
    for k in range(1,7,-i):
        print(k,end=" ")
    print()

print()

for i in range(6+1):
    for j in range(1, 6+1, 1):
        print(j if j <= i else " ", end = " ")
    print()

print()

for i in range(6 + 1):
    for j in range(1,7,-i):
        print(j , end = " ")
    print()
