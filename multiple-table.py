for dan in range(2, 10):
    print(f"{dan}단".ljust(10), end="")
print()

for i in range(1, 10):
    for dan in range(2, 10):
        expr = f"{dan}x{i}={dan*i}"
        print(expr.ljust(10), end="")  
    print() 
