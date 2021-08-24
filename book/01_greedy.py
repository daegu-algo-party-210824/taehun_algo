"""당신은 음식점의 계산을 도와주는 점원이다.
카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다."""

product_price = 8000
pay = 9000
coins = [500, 100, 50, 10]
#
def min_count():
    remain = 1260
    # print(remain)
    coin_n = 0
    for coin in coins:
        coin_n = coin_n + remain // coin
        remain = remain % coin
    # n_min = [remain/coin for coin in coins]
    return coin_n

answer = min_count()
print(answer)

n = 1260
count = 0
# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]
for coin in coin_types :
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세가 n %= coin
    n %= coin
print(count)
