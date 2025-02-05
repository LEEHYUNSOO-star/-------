from shopping_cart import ShoppingCart

cart = ShoppingCart()   # 쇼핑카트 객체 생성

# 상품 추가
cart.add_item("고기", 200000) # 상품 추가
cart.add_item("야채", 30000)
cart.add_item("술", 1000000)


cart.show_cart() # 쇼핑카트 내용 출력


total = cart.total_price()
print(f"총 금액은 {total}원입니다.") # 총 금액 계산


cart.remove_item("술") # 상품 제거


cart.show_cart() # 상품 제거 후 쇼핑카트 내용 출력


total = cart.total_price() # 총 금액 다시 계산
print(f"총 금액은 {total}원입니다.")
