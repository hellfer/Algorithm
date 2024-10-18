# 이동통신 사업자 요금 정보
operators = [
    {"name": "ParsTel", "call_rate": 30, "data_rate": 40},
    {"name": "ParsCell", "call_rate": 35, "data_rate": 30},
    {"name": "ParsPhone", "call_rate": 40, "data_rate": 20},
]

while True:
    # 학생의 통화 시간과 데이터 사용량 입력
    c, d = map(int, input().split())
    
    # 종료 조건
    if c == 0 and d == 0:
        break
    
    # 최소 비용 계산
    min_cost = float('inf')
    
    for operator in operators:
        cost = (operator["call_rate"] * c) + (operator["data_rate"] * d)
        min_cost = min(min_cost, cost)
    
    # 결과 출력
    print(min_cost)
