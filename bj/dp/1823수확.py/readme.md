# 1823 수확
https://www.acmicpc.net/problem/1823

# 시도
그리디 문제라 생각해서, 각 상황에서 작은쪽을 먼저 수확하는 방법으로 구현
~~~python
n = int(input())
l = [int(input()) for _ in range(n)]

i = 0
j = n-1
sum = 0
k = 0
while i<j:
    k += 1
    if l[i] < l[j]:
        sum += l[i]*k
        i += 1
    else:
        sum += l[j]*k
        j -= 1
sum += l[i]*(k+1)
print(sum)
~~~

반례  
4 2 2 1 2

# 풀이
dp 문제. dp\[i]\[j]를 '왼쪽에서 i번째, 오른쪽에서 j번째를 수확할 수 있는 상태에서 최대 값' 으로 정의  
- 처음에 모든 스트링을 저장하려고 했으나, 인덱스만으로도 충분함