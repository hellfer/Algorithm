from collections import Counter

TC = int(input())

for i in range(1,TC+1):
    S = input()
    counter = Counter(S)
    count_2 = sum(value == 2 for value in counter.values()) #[True, True, False, False]에서 True의 개수인 2를 반환
    #dict_values([2, 2, 1, 1]),  value에 저장한 후, value == 2의 결과를 생성하는 제너레이터(generator)
    if len(counter) == 2 and count_2 == 2:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')

