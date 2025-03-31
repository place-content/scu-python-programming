numbers: list[int] = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for num in numbers:
    if num % 2 == 0:
        print(f"{num}은 짝수입니다.")
    else:
        print(f"{num}은 홀수입니다.")
