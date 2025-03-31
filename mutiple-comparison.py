num = int(input("정수를 입력해주세요 : "))

for i in range(2, 6):
    print(f"{num}은 {i}로 나누어 떨어지는 숫자가{' 아닙니다.' if num % i else '입니다.'}")
