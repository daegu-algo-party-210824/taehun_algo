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



def rule_of_big_number(nums, m, k):
    # 큰수의 법칙
    answer = 0
    count = -1
    big_num = 0

    for i in range(m):
        count = count + 1
        big_num = max(nums)
        if count == k:
            nums.sort()
            big_num = nums[-2]
            count = 0
        answer = big_num + answer
    return answer

nums = [3, 4, 3, 4, 3]; m = 7 ; k = 2
answer = rule_of_big_number(nums, m, k)
print(f"큰수의 법칙 nums={nums}, m={m}, k={k} 일때 답은{answer}")
