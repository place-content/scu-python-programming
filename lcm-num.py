def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

result = 1
for i in range(2, 21): 
    result = lcm(result, i)

print("1부터 20까지의 어떤 수로도 나누어떨어지는 가장 작은 수는:", result)
