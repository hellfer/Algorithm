from datetime import datetime, timezone

# 현재 UTC 시각을 얻음
current_utc_time = datetime.now(timezone.utc)

# 연도, 월, 일을 출력
print(current_utc_time.year)
print(str(current_utc_time.month).zfill(2))
print(str(current_utc_time.day).zfill(2))
