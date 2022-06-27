'''
[큰 수의 법칙(Law of Large Numbers) 문제]
- 이 문제에서 큰 수의 법칙이란, 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다.
- 단, 배열의 특정한 인덱스(번호)에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것이 이 법칙의 특징이다.
- 이때, 서로 다른 인덱스에 해당하는 수가 같은 경우에도 서로 다른 것으로 간주한다.
- 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 K가 주어질 때 큰 수의 법칙에 따른 결과를 출력하시오.

<입력조건>
- 첫째 줄에 N(2<=N<=1000), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다. (입력받음)
- 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10,000 이하의 수로 주어진다. (입력받음)
- 입력으로 주어지는 K는 항상 M보다 작거나 같다
'''

n, m, k = map(int, input().split())     # n: 배열의 크기, m: 숫자가 더해지는 총 횟수, k: 한 인덱스에서 더할 수 있는 총 횟수
data = list(map(int, input().split()))

data.sort(reverse=True)

first_num = data[0]
second_num = data[1]
sum_result = 0

sum_count = m//(k+1)
tail_count = m%(k+1)

sum_unit = first_num * k + second_num
sum_result = sum_unit * sum_count
sum_result += first_num*tail_count

print(sum_result)
