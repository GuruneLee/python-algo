# https://justicehui.github.io/medium-algorithm/2019/01/01/monotoneStack/
'''
<모노톤 스택>
정렬되지 않은 배열이 주어졌을때, 
stack 스택의 원소들을 O(n)의 시간복잡도로 (중복을 허용하지 않고) 오름차순 혹은 내림차순 상태로 유지하는 방법
ex. 조건에 만족하는 자신보다 큰 가장 가까운 원소의 인덱스 찾기
'''

# ex. leet - 1475. Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices):
        # prices[i] >= prices[j] 인 i보다 큰 가장 가까운 j 찾기
        ms = []
        n = len(prices)
        re = [prices[i] for i in range(n)]
        for j in range(n):
            while ms and ms[-1][1] >= prices[j]:
                idx, _ = ms.pop()
                re[idx] = prices[idx]-prices[j]
            ms.append((j, prices[j]))
        return re