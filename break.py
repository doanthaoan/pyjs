print("Using a check variable: ")
a1 = []
for n in range(2, 10):
    check = True
    for x in range(2, n):
        if n % x == 0:
            check = False
    if check:
        a1.append(n)
        print(n)
print("----------")        
print("Using break and ELSE for loop: ")
a2 = []
for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        a2.append(n)
        print(n)

print("----------")
print("Compare 2 result:", a1 == a2)
print(a1)