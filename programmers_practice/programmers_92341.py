# fees
# fees[0] = 기본 시간(분)
# fees[1] = 기본 요금(원)
# fees[2] = 단위 시간(분)
# fees[3] = 단위 요금(원)
# records
# 시각 차량번호 내역

def solution(fees, records):
    # print(fees, records)
    default_time = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]
    list = []
    for i in range(len(records)):
        if records[i][11:] == 'IN':
            list.append([records[i][0:5], records[i][5:10], records[i][11:]])
            for j in range(i+1, len(records)):
                if records[i][5:10] == records[j][5:10] and records[j][11:] == 'OUT':
                    list.append([records[j][0:5], records[j][5:10], records[j][11:]])
                    break
    # print(list)
    for i in range(len(list)):
        if list[i][1] == 
        print(list[i])


    answer = []
    return answer

if __name__ == "__main__":
    fees, records = [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print('1st Test Case', solution(fees, records))
    fees, records = [120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
    print('1st Test Case', solution(fees, records))