'''
[백준-동전0 문제]
- 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
- 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

<입력조건>
- 첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
- 둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)
<출력조건>
- 첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
'''

n, k = map(int, input().split())
coin_list = []
for i in range(n):
    coin_list.append(int(input()))

count = 0
max_index = 0

# K보다 작은 coin 중 가장 큰 coin의 인덱스 찾기
# if 동전의 최댓값이 K보다 작을 경우
if k >= coin_list[n-1]:
    max_index = n-1
# if 동전의 최댓값이 K보다 클 경우
else:
    for i in range(n):
        if k < coin_list[i]:
            max_index = i-1
            break

# K를 max_index coin부터 나눔 (몫: 필요한 coin 개수(count), 나머지: 갱신되는 K의 값)
for i in range(max_index, -1, -1):   #coin_list는 오름차순으로 정렬되어 있으므로
    if k == 0:
        break
    count += k//coin_list[i]
    k = k%coin_list[i]
print(count)

