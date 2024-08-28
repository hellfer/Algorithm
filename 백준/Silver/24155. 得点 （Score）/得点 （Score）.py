n = int(input())
scores = []

# 점수 입력받기
for _ in range(n):
    scores.append(int(input()))

# 점수와 인덱스를 함께 저장
indexed_scores = [(score, index) for index, score in enumerate(scores)]

# 점수를 기준으로 내림차순 정렬
indexed_scores.sort(key=lambda x: x[0], reverse=True)

# 순위 매핑을 위한 리스트 초기화
ranks = [0] * n
current_rank = 1

# 순위를 매핑
for i in range(n):
    if i > 0 and indexed_scores[i][0] == indexed_scores[i - 1][0]:
        ranks[indexed_scores[i][1]] = ranks[indexed_scores[i - 1][1]]
    else:
        ranks[indexed_scores[i][1]] = current_rank
    current_rank += 1

# 결과 출력
for rank in ranks:
    print(rank)
