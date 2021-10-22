from recipe import Recipe

class RecipeBook:
    def __init__(self):
        self.recipe_list = []
        self.init_recipe()

    def add_recipe(self):
        # 추가할 레시피 이름 입력받자
        name = input('>> 레시피 이름을 입력하세요: ')
        # 중복 체크 하자
        for recipe in self.recipe_list:
        # 중복되는 레시피가 있으면
            if name == recipe.name:
            # 중복된다고 알려주자
                print('이미 존재하는 레시피입니다!')
                return
        # 중복되는 레시피가 없으면
        # 레시피 생성하기
        new_recipe = Recipe(name)
        new_recipe.set_recipe()
        # 레시피리스트에 생성한 레시피 추가하기
        self.recipe_list.append(new_recipe)

    def show_recipe(self):
        for index, recipe in enumerate(self.recipe_list):
            print(f'{index+1}')
            print(recipe)

    # 레시피북에서 레시피 찾기
    def search_recipe(self):
        searched_recipe = []
        # 레시피 이름을 검색하자(입력받자)
        name = input('>> 원하는 레시피를 검색하세요: ')
        # (반복문 시작) 레시피 리스트를 돌면서 레시피 확인
        for recipe in self.recipe_list:
            # 레시피의 이름이 검색받은 이름과 같다면 (찾았으면)
            if name == recipe.name:
                # 그 레시피 보여주자
                print(recipe)
                searched_recipe.append(recipe)
        # 검색된 레시피가 없다면 (searched_recipe가 비어있다면)
        if len(searched_recipe) == 0:
            # 추가할지 물어보자
            answer = int(input('>> 찾는 레시피가 없습니다. 추가하시겠습니까? (1: 예, 0: 아니오) '))
            # 추가한다고 하면
            if answer == 1:
                # 레시피 추가하기
                self.add_recipe()
            else:
                return

    # 재료로 (해당되는) 레시피 찾기
    def search_ingredient(self):
        # 빈 셋(set) 생성 -> 재료를 중복 제거해서 담은 셋(set)
        all_ingredient = set()
        # 레시피북에 있는 레시피의 재료들 셋에 넣자
        for recipe in self.recipe_list:
            for ingredient in recipe.ingredient:
                all_ingredient.add(ingredient)
        # 모든 재료들 보여주자
        for index, ingredient in enumerate(all_ingredient):
            print(f'{index+1}. {ingredient}')
        # 찾을 재료를 검색하자(입력받자)
        search_num = int(input('>> 사용할 재료를 입력하세요: '))
        search_ingredient = list(all_ingredient)[search_num-1]
        # 레시피 리스트의 레시피 -> 레시피의 재료를 살펴보자
        for recipe in self.recipe_list:
            # 입력한 재료가 포함되면
            if search_ingredient in recipe.ingredient:
            # 해당 레시피 모두 보여주자
                print(recipe)

    def init_recipe(self):
        떡볶이 = Recipe('떡볶이')
        떡볶이.people = 2
        떡볶이.video = 'youtube.com'
        떡볶이.ingredient = {'물': '100', '떡':'200', '고추장':'100', '어묵':'100', '양파':'300'}
        self.recipe_list.append(떡볶이)
        카레 = Recipe('카레')
        카레.ingredient = {'카레가루': '50', '감자': '200', '당근':'100'}
        self.recipe_list.append(카레)
        파스타 = Recipe('파스타')
        파스타.contents = '맛있게 만드세요!'
        파스타.ingredient = {'면': '100', '토마토소스': '200'}
        self.recipe_list.append(파스타)

    # def __str__(self):
    #     pass