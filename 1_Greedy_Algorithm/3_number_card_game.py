'''
[숫자 카드 게임 문제]
- 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
- 숫자가 쓰인 카드들이 N*M 형태로 놓여 있다. 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
- 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택하고, 그 다음 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.

<입력조건>
- 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.(1<=N,M<=100)
- 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의 자연수이다.
'''

n, m = map(int, input().split())
card_list = []

for i in range(n):
    card = list(map(int, input().split()))
    card_list.append(card)

for i in range(n):
    min_num = 10000
    if min_num > min(card_list[i]):
        min_num = min(card_list[i])

print(min_num)