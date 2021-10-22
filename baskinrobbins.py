class Icecream:
    def __init__(self, name):
        self.name = name

    def set_explanation(self, explanation):
        self.explanation = explanation

    def __str__(self):
        return f'이름: {self.name}'
    
아이스홈런볼 = Icecream('아이스홈런볼')
아이스홈런볼.set_explanation('초콜릿 아이스크림과 바닐라 아이스크림 속에 초코코팅 홈런볼과 피넛이 쏙쏙!')

오레오쿠앤크= Icecream('오레오 쿠키 앤 크림')
오레오쿠앤크.set_explanation('부드러운 바닐라향 아이스크림에, 달콤하고 진한 오레오 쿠키가 듬뿍!')

아몬드봉봉 = Icecream('아몬드 봉봉')
아몬드봉봉.set_explanation('입안 가득 즐거운 초콜릿, 아몬드로 더욱 달콤하게!')

엄외 = Icecream('엄마는 외계인')
엄외.set_explanation('엄마는 외계인밀크 초콜릿, 다크 초콜릿, 화이트 무스 세 가지 아이스크림에 달콤 바삭한 초코볼이 더해진 아이스크림')

class Order:
    _CATEGORIES = ('싱귤레귤러', '더블레귤러','파인트')
    _PRICES = (3200, 6200, 8200)

    def __init__(self):
        self.set_cateries()
        self.menu = []
        self.init_menu()
        self.order_menu = []

    def __str__(self):
        pass
        def set_cateries(self):
            for index, category in enumerate(Order._CATEGORIES):
                print(index+1, category)
            category_num = input('종류를 골라주세요')
            self.category = int(category_num)

        def init_menu(self):
           self.menu.append(Icecream('오레오 쿠키 앤 크림'))
           self.menu.append(Icecream('엄마는 외계인'))
           self.menu.append(Icecream('아몬드 봉봉'))

        def show_menu(self):
            for index, icecream in enumerate (self.menu):
                print(f'{index + 1}. {icecream}')

        def order(self):
            self.show_menu()
            for _ in range(self.category):
                icecream = input('아이스크림을 골라주세요: ')
                icecream = int(icecream)
                self.order_menu.append(self.menu[icecream -1])
                print('-'*10 + '주문 내역입니다.' + '-'*10)
                print(Order._CATEGORIES[self.category -1])
                print(Order._PRICES[self.category -1] + '원')
                for icecream in self.order_menu:
                    print(icecream)
order = Order()
order.order()

