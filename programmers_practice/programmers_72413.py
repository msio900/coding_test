import datetime

def solution(a, b):
    days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    answer = days[datetime.date(2016, a, b).weekday()]
    return answer

if __name__ == '__main__':
    a, b = 5, 24
    print(solution(a, b))
