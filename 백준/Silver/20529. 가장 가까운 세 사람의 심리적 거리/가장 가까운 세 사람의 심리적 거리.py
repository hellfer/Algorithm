import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    mbti = list(map(str,input().split()))
    cnt = [0]*16
    order = ['INFJ', 'INFP', 'INTJ', 'INTP', 'ISFJ', 'ISFP', 'ISTJ', 'ISTP', 'ENFJ', 'ENFP', 'ENTJ', 'ENTP', 'ESFJ', 'ESFP', 'ESTJ', 'ESTP']
    type_dict = {order[i]:i for i in range(16)}

    for type in mbti:
        cnt[type_dict[type]] += 1

    ans = 1e9

    for i in range(16):
        if cnt[i] >= 3:
            ans = 0
            break
        for j in range(i+1, 16):
            if cnt[i] >= 2 and cnt[j] >= 1:
                ans = min(ans, sum(x != y for x, y in zip(order[i], order[j]))*2)
            if cnt[j] >= 2 and cnt[i] >= 1:
                ans = min(ans, sum(x != y for x, y in zip(order[i], order[j]))*2)
            for k in range(j+1, 16):
                if cnt[i] >= 1 and cnt[j] >= 1 and cnt[k] >= 1:
                    ans = min(ans, sum(x != y for x, y in zip(order[i], order[j])) + sum(x != y for x, y in zip(order[j], order[k])) + sum(x != y for x, y in zip(order[i], order[k])))
    print(ans)
