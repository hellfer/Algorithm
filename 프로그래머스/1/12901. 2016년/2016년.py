import datetime

def solution(a, b):
    x = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    y = datetime.datetime(2016, a, b).weekday()
    result = x[y]
    return result
