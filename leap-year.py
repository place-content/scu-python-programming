def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1 
            else:
                return 0 
        else:
            return 1  
    else:
        return 0 

year = int(input("연도를 입력하세요: "))

if isLeapYear(year):
    print(f"{year}년은 윤년입니다.")
else:
    print(f"{year}년은 평년입니다.")