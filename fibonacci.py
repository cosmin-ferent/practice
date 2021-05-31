fib = [0, 1]

for _ in range(int(input('Enter your range number: '))):
    new_item = fib[-1] + fib[-2]
    fib.append(new_item)

print(fib)
