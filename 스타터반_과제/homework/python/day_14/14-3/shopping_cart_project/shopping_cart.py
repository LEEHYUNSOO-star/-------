class ShoppingCart:
    def __init__(self): # 쇼핑카트 초기화 __init__ 으로 객체 초기화
        self.cart = []  # 상품을 담을 리스트

    def add_item(self, name, price): # 쇼핑카트에 상품추가
        item = {"name": name, "price": price} 
        self.cart.append(item)
        print(f"상품 '{name}'이(가) 추가되었습니다.")

    def remove_item(self, name): # 쇼핑카트에서 상품 제거
        for item in self.cart:
            if item["name"] == name:
                self.cart.remove(item)
                print(f"상품 '{name}'이(가) 제거되었습니다.")
                return
        print(f"상품 '{name}'을(를) 찾을 수 없습니다.")

    def total_price(self): # 쇼핑카트에 담긴 상품 가격 계산
        total = sum(item["price"] for item in self.cart)
        return total

    def show_cart(self): # 쇼핑카트에 담긴 상품 확인받기
        if self.cart:
            print("현재 쇼핑카트에 담긴 상품들:")
            for item in self.cart:
                print(f"{item['name']} - {item['price']}원")
        else:
            print("쇼핑카트가 비어 있습니다.")
