'''
[백준-주유소 문제]
- N개의 도시들은 일적선 도로 위에 있다. 제일 왼쪽의 도시에서 제일 오른쪽의 도시로 자동차로 이동하려고 한다.
- 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발하여야 한다.
- 도로를 이용할 때 1km마다 1리터의 기름을 사용한다.
- 두 도시 사이의 도로들은 서로 길이가 다를 수 있고, 도시 마다 주유소의 리터당 가격은 다를 수 있다.
- 각 도시에 있는 주유소의 기름 가격과, 각 도시를 연결하는 도로의 길이를 입력으로 받아 
  제일 왼쪽 도시에서 제일 오른쪽 도시로 이동하는 최소의 비용을 계산하는 프로그램을 작성하시오.

<입력조건>
- 첫째 줄에는 도시의 개수를 나타내는 정수 N(2 ≤ N ≤ 100,000)이 주어진다. 
- 둘째 줄에는 인접한 두 도시를 연결하는 도로의 길이가 제일 왼쪽 도로부터 N-1개의 자연수로 주어진다. 
- 셋째 줄에는 주유소의 리터당 가격이 제일 왼쪽 도시부터 순서대로 N개의 자연수로 주어진다. 

<출력조건>
- 표준 출력으로 제일 왼쪽 도시에서 제일 오른쪽 도시로 가는 최소 비용을 출력한다. 
'''

city = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))
low_price_index = -1
cost = 0

for i in range(city-1):
    # 현재 도시보다 뒤에 low_price 도시가 있으면 그냥 지나감   
    if low_price_index > i:
        continue

    # 다음 도시 중 현재 도시보다 기름값이 낮은 (가장 가까운)도시 찾기-> low_price_index 찾기
    for j in range(i, city-2):
        if price[i] > price[j]:
            low_price_index = j
            break
        elif price[i] == price[j]:
            low_price_index = j

    # low_price_index가 갱신이 안됐다면, 마지막 low_price 도시라는 뜻이니 끝까지 주유함.
    if i == low_price_index:
        cost += price[i] * (sum(distance[i:city-1]))
    
    # low_price_index가 갱신 되었다면, low_price_index까지만 기름 넣기
    else:
        cost += price[i] * (sum(distance[i:low_price_index]))

print(cost)
