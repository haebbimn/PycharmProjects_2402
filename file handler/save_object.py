from person import Person

#객체 생성하자
번호15 = Person('이재령', '하얀색')
번호17 = Person('임사랑', '분홍색')

#리스트 만들자
절친 = [번호15, 번호17]
# print(절친)
# for 친구 in 절친:
#     print(친구)

#저장하자
#1. 객체 하나 저장
import pickle

with open('object.bin', 'wb') as f:
    pickle.dump(번호15, f)

#2. 객체 여러 개 저장
with open('objects.bin', 'wb') as f:
    pickle.dump(절친, f)