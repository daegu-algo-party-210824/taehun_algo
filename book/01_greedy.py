def coin_change_algo(change):
    # 거스름돈, pg 87
    count = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        count = int(change/coin) + count
        change = change - int(change/coin) * coin

    return count

# change = 1370
# answer = coin_change_algo(change)
# print(f"거스름돈 : {change}일때 동전 {answer}개 교환")

def rule_of_big_number(nums, m, k):
    # 큰수의 법칙, pg 92
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

# nums = [3, 4, 3, 4, 3]; m = 7 ; k = 2
# answer = rule_of_big_number(nums, m, k)
# print(f"큰수의 법칙 : nums={nums}, m={m}, k={k} 일때 답은{answer}")

def num_card_game(n, m, rows):
    # 숫자카드게임, pg 96
    min_list = [min(r) for r in rows]
    answer = max(min_list)

    return answer

# n = 2 ; m = 4
# rows = [
#     [7, 3, 1, 8],
#     [3, 3, 3, 4],
# ]
# answer = num_card_game(n, m, rows)
# print(f"숫자카드게임 : n={n}, m={m}, rows={rows} 일때 답은{answer}")

def make_one(n, k):
    # 1이 될때까지, pg 99
    count = 0
    while True:
        if n % k != 0:
            n = n - 1
        else:
            n = n / k
        count = count + 1

        if n == 1:
            break

    return count

def adven_guild():
    string = '23122'
    s = [int(i) for i in string]
    try:
        for i in range(len(s)):
            for ii in range(len(s)):
                group = s[i+1] + s[ii+i]
                if s[i] == group:
                    print(s[i])
    except:
        pass


def multi_plus():
    s = '5671'
    s = [int(i) for i in s]
    answer = 1
    for n in s:
        if n != 0:
            answer = answer * n
        if n == 1:
            answer = answer + 1
    print(answer)


def str_reverse():
    string = '0001100'
    string_list = [ int(i) for i in string]

    index_num = []
    count = 0
    for i in range(len(string_list)):
        if string_list[i] == 1:
            string_list[i] = 0

    print(string_list)

# n = 1089 ; k = 5
# answer = make_one(n, k)
# print(f"1이 될때까지 : n={n}, k={k} 일때 답은{answer}")

def money_not_making():
    # 만들수 없는 금액, pg 314
    from itertools import combinations
    n = 5
    coins = [3, 2, 1, 1, 9]

    combi_list = [combinations(coins, i) for i in range(len(coins)+1)]
    calcu_list = []
    plus = 0
    for combi in combi_list[1:]:
        for num in combi:
            for calcu in num:
                plus = plus + calcu

            if plus not in calcu_list :
                calcu_list.append(plus)
            plus = 0

    sorted_calcu_list = sorted(calcu_list)
    max_num = max(sorted_calcu_list)
    answer = [i for i in range(1, max_num) if i not in sorted_calcu_list]

    print(min(answer))

# money_not_making()

def choose_ball():
    # 볼링공 고르기, pg 315
    n = 5
    m = [1, 5, 4, 3, 2, 4, 5, 2]

    combi = []
    for i in range(len(m)):
        for ii in range(i, len(m)):
            if m[i] != m[ii]:
                combi.append((i+1, ii+1))
    print(len(combi))

# choose_ball()

def eating_live():
    # 무지의 먹방 라이브, pg 316
    food_times = [3, 1, 2]
    k = 5
    total_time = sum(food_times)

    i = 0
    count = 0
    while True:
        if food_times[i] != 0:
            food_times[i] = food_times[i] - 1
            count = count + 1

        i = i + 1
        if i == len(food_times):
            i = 0

        if count == k:
            break

    for num, food_time in enumerate(food_times):
        if food_time == total_time - k:
            print(num+1)

eating_live()
