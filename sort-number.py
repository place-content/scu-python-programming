a = int(input("첫 번째 정수를 입력하세요: "))
b = int(input("두 번째 정수를 입력하세요: "))
c = int(input("세 번째 정수를 입력하세요: "))

if a > b:
    a, b = b, a 
if a > c:
    a, c = c, a 
if b > c:
    b, c = c, b  

print("정렬된 순서:", a, b, c)
