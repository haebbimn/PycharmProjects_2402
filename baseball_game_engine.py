import random

#정답 만들자: 0~9 숫자 세개 뽑자
def make_answer():
    list_r = random.sample(range(9 + 1), 3)
    return "".join(map(str, list_r))

def check(guess, answer):
    strike = 0
    ball = 0
    #숫자 하나 꺼내서 정답에 있고, 자리가 같으면, strike += 1
    #숫자 하나 꺼내서 정답에 있고, 자리가 다르면, ball += 1
    for i, g in enumerate(guess):
        for j, a in enumerate(answer):
            if g == a:    #숫자가 같으면
                if i == j:  #자리가 같으면
                    strike += 1
                else:       #자리가 다르면
                    ball += 1

    return strike, ball

if __name__ == '__main__':
    answer = make_answer()
    print(answer)
    strike, ball = check("832", "934")
    print(strike, ball)     #1 0
    strike, ball = check("431", "934")
    print(strike, ball)     #1 1
    strike, ball = check("934", "934")
    print(strike, ball)     #3 0

