def coin_change_algo(change):
    # 예제01-거스름돈
    count = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        count = int(change/coin) + count
        change = change - int(change/coin) * coin
    return count

change = 1370
answer = coin_change_algo(change)
print(f"거스름돈 {change}일때 동전 {answer}개 교환")



def example_rule_of_big_number():
    n = 5; m = 8; k = 3
    num_list = [2, 4, 5, 4, 6]

    answer = 0
    count = 0

    for i in range(m):
        count = count + 1

        big_num = max(num_list)
        answer = big_num + answer

        if count == k:
            second_big_num = []
            for num in numlist:
                second_big_num.append(big_num - num)
            second_big_num.sort()






# example_rule_of_big_number()
