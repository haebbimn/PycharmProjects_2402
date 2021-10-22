class Celebrity:

    def __init__(self, name):
        #이름
        self.name = name
        #소속사
        #그룹

    def set_name(self, name):
        self.name = name

    def set_entertainment(self, entertainment):
        self.entertainment = entertainment

    def set_group(self, group):
        self.group = group

    def info(self):
        print(f'이름: {self.name}\t소속사: {self.entertainment}')

    def __str__(self):
        return f'이름: {self.name}\t소속사: {self.entertainment}'

class Talent(Celebrity):
    def __init__(self, name):
        super().__init__(name)

    def set_drama(self, drama):
        self.drama = drama

    def __str__(self):
        return super().__str__() + f'\t드라마: {self.drama}'

class singer(Celebrity):
    def __init__(self, name):
        super().__init__(name)

    def set_song(self, song):
        self.song = song

    def __str__(self):
        return super().__str__() + f'노래: {self.song}'

JDon = singer("이승협", "옥탑방")
JDon.set_entertainment("FNC")
print(JDon)

HwengStar = singer("유회승", "진짜가 나타났다")
HwengStar.set_entertainment("FNC")
print(HwengStar)

엔플라잉 = []
엔플라잉.append(JDon)
엔플라잉.append(HwengStar)
print(엔플라잉)
for 멤버 in 엔플라잉:
    print(멤버)
# for i in range(len(엔플라잉)):
#     print(엔플라잉[i])

IU = Celebrity("이지은")
#IU.set_name("이지은")
IU.set_entertainment("EDAM")
# IU.info()
# print(IU.name, IU.entertainment)
print(IU) #클래스의 __str__() 호출됨


JDon = Celebrity("이승협(제이던)")
#JDon.set_name("이승협(제이던)")
JDon.set_entertainment("FNC")
# JDon.info()
# print(JDon.name, JDon.entertainment)
print(JDon)

이광수 = Celebrity("이광수")
이광수.set_entertainment("킹콩")
이광수.set_drama("라이브")
print(이광수)
#