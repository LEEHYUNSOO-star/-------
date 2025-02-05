from recipe import Recipe

my_recipe = Recipe("김치찌개", ["김치", "돼지고기", "마늘", "물", "양파", "대파", "고추", "두부"], 30)  # 레시피 형성

my_recipe.add_ingredient("두부") # 재료 추가

my_recipe.remove_ingredient("된장") # 재료 제거

my_recipe.display_recipe() # 레시피 출력

difficulty = my_recipe.calculate_difficulty()  #난이도 계산
print(f"난이도: {difficulty}도 가능")

