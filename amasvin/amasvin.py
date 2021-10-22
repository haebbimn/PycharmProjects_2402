class Drink:
    _CUPS = ('레귤러', '점보')  # '레귤러'
    _ICES = ('0%', '50%', '100%', '150%')  # '100%'
    _SUGARS = ('0%', '50%', '100%', '150%')  # '100%'

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.cup = 0  # '레귤러'   Drink._CUPS[self.cup]
        self.ice = 2  # '100%'  Drink._ICES[self.ice]
        self.sugar = 2  # '100%'    Drink._SUGARS[self.sugar]

    def set_cup(self):
        for index, cup in enumerate(Drink._CUPS):  # 컵 종류 보여주자
            print(f'{index + 1}: {cup}')

        cup = input('컵사이즈를 선택하세요: ')  # 컵 선택하자
        if cup == '':
            self.cup = 0
        else:
            cup = int(cup)
            self.cup = cup - 1  # 컵 self에 넣자

        if self.cup == 1:       #점보면, +500원
            self.price += 500

    def set_ice(self):
        for index, ice in enumerate(Drink._ICES):  # 얼음량 종류 보여주자
            print(f'{index + 1}: {ice}')
        ice = input('얼음량을 선택하세요: ')  # 선택하자
        # if ice == '':
        #     self.ice = 2
        # else:
        #     self.ice = int(ice) - 1
        self.ice = 2 if ice == '' else int(ice) - 1  # self.ice에 설정하자

    def set_sugar(self):
        for index, sugar in enumerate(Drink._SUGARS):  # 당도 종류 보여주자
            print(f'{index + 1}: {sugar}')
        sugar = input('당도를 선택하세요: ')  # 당도 선택하자
        self.sugar = 2 if sugar == '' else int(sugar) - 1  # self.sugar에 넣자

    def order(self):
        self.set_cup()
        self.set_ice()
        self.set_sugar()

    def __str__(self):
        return f'이름: {self.name}\t가격: {self.price}원\t컵사이즈: {Drink._CUPS[self.cup]}\t얼음량: {Drink._ICES[self.ice]}\t당도: {Drink._SUGARS[self.sugar]}'


class Coffee(Drink):
    pass


class Bubbletea(Drink):
    _PEARLS = ('타피오카', '화이트', '알로에', '젤리')

    def __init__(self, name, price):
        super().__init__(name, price)        #부모초기화 호출
        self.pearl = 0       #'타피오카'

    def set_pearl(self):
        for index, pearl in enumerate(Drink._PEARLS):
            print(f'{index + 1}: {pearl}')
        pearl = input('펄 종류를 선택하세요: ')
        self.pearl = 2 if pearl == '' else int(pearl) - 1

    def order(self):
        super().order()
        self.set_pearl()

    def __str__(self):
       result = super().__str__()
        return result + f'\t펄 종류:{self.pearl}'


class Order:
    def __init__(self):
        self.menu = []
        self.init_menu()
        self.order_menu = []


    def init_menu(self):
        사랑이꺼 = Coffee('카페모카', 2500)
        하람이꺼 = Bubbletea('오레오 쉐이크', 3900)
        에스더꺼 = Bubbletea('타로 밀크티',  3300)
        self.menu.append(사랑이꺼)
        self.menu.append(하람이꺼)
        self.menu.append(에스더꺼)

    def show_menu(self):
        for index, drink in enumarate(self.menu):
            print(f'{index +1}: {drink.name}\t{drink.price}원')

    def sum_price(self):
       return '0'

    def order_drink(self):
        while True:
            self.show_menu()
            drink = input('메뉴를 선택하세요: ')
            drink = int(drink) -1
            new_drink = self.menu[drink]
            new_drink.order()
            self.order_menu.append(new_drink)
            is_add = input('더 주문하시겠습니까?(n: 종료)')
            if is_add == 'n':
                break
        print(self)

    def __str__(self):
        s = '-' * 20 + '주문내역' + '-'*20
        s += self.order_menu

#사랑이꺼 = Coffee('카페모카', 2500)
#사랑이꺼.order()
#print(사랑이꺼)
order = Order()
order.show_menu()