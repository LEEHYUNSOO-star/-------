from math_operations import calculate_area, calculate_circumference # 모듈에서 함수를 임포트

radius = 5  # ex) 반지름

area = calculate_area(radius)
circumference = calculate_circumference(radius)

print(f"반지름이 {radius}인 원의 면적은 {area}이고, 둘레는 {circumference}입니다.")
