'''
[거스름돈 문제]
- 카운터에 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다.
- 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라.
'''

n = int(input("거스름돈을 입력하세요: "))
coin_list = [500, 100, 50, 10]
coin_count = 0


for coin in coin_list:
    coin_count += n//coin
    n = n % coin

print("최소 동전 개수: ", coin_count)
