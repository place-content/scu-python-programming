num1 = int(input("1번째 숫자 : "))
num2 = int(input("2번째 숫자 : "))

if num1 > num2:
    print(f"처음 입력했던 {num1}가 {num2}보다 더 큽니다.")
elif num1 < num2:
    print(f"처음 입력했던 {num1}가 {num2}보다 더 작습니다.")
else:
    print("두 숫자는 같습니다.")
