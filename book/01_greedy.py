def coin_change_algo(change):
    # 거스름돈
    count = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        count = int(change/coin) + count
        change = change - int(change/coin) * coin
    return count

change = 1370
answer = coin_change_algo(change)
print(f"거스름돈 {change}일때 동전 {answer}개 교환")



def rule_of_big_number(m, k):
    # 큰수의 법칙
    n = 5;
    num_list = [2, 4, 5, 4, 6]

    answer = 0
    count = -1
    big_num = 0

    for i in range(m):
        count = count + 1
        big_num = max(num_list)
        if count == k:
            num_list.sort()
            big_num = num_list[-2]
            count = 0

        answer = big_num + answer
    return answer

m = 8 ; k = 3
answer = rule_of_big_number(m, k)
print(f"큰수의 법칙 m={m}, k={k}일때 답은{answer}")
