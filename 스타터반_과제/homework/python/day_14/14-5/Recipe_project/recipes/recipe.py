class Recipe:
    def __init__(self, name, ingredients, cook_time):
        self.name = name # 레시피 이름
        self.ingredients = ingredients # 재료 목록
        self.cook_time = cook_time # 조리 시간
    
    def add_ingredient(self, ingredient): # 재료를 추가하는 메서드
        if ingredient in self.ingredients:
            print(f"{ingredient}는 이미 재료 목록에 있습니다.")
        else:
            print(f"{ingredient}가 추가되었습니다.")
        
    def remove_ingredient(self, ingredient): # 재료를 제거하는 메서드
         if ingredient in self.ingredients:
            self.ingredients.remove(ingredient) 
         else:
             print(f"{ingredient}는 재료 목록에 없다~.")
             
    def display_recipe(self): # 레시피의 모든 정보를 출력하는 메서드
        print(f"레시피 이름: {self.name}")
        print(f"재료: {','.join(self.ingredients)}")
        print(f"조리 시간: {self.cook_time}분")
        
    def calculate_difficulty(self): # 레시피의 난이도를 계산
        
        num_ingredients = len(self.ingredients)
        if num_ingredients < 5 and self.cook_time < 30:
            return '초보'
        elif 5 <= num_ingredients <= 10 and 30 <= self.cook_time < 60:
            return '아빠' 
        else:
            return '엄마'