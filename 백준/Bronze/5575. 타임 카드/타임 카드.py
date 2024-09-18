# 직원 근무 시간을 계산하는 함수
def calculate_work_time(start_time, end_time):
    start_h, start_m, start_s = start_time
    end_h, end_m, end_s = end_time
    
    # 출근 시간과 퇴근 시간을 초로 변환
    start_seconds = start_h * 3600 + start_m * 60 + start_s
    end_seconds = end_h * 3600 + end_m * 60 + end_s
    
    # 근무 시간 계산
    work_seconds = end_seconds - start_seconds
    
    # 근무 시간을 시, 분, 초로 변환
    work_h = work_seconds // 3600
    work_seconds %= 3600
    work_m = work_seconds // 60
    work_s = work_seconds % 60
    
    return work_h, work_m, work_s

# 입력 받기
for _ in range(3):
    start_h, start_m, start_s, end_h, end_m, end_s = map(int, input().split())
    start_time = (start_h, start_m, start_s)
    end_time = (end_h, end_m, end_s)
    
    # 근무 시간 계산
    work_time = calculate_work_time(start_time, end_time)
    
    # 결과 출력
    print(work_time[0], work_time[1], work_time[2])
