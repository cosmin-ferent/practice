prime = []
for n in range(100, 200):
    # if all(n % i != 0 for i in range(2, n)):
    #     prime.append(n)
    check = []
    for i in range(2, n):
        if n % i == 0:
            check.append(i)
    if len(check) == 0:
        if n not in prime:
            prime.append(n)
print(prime)
