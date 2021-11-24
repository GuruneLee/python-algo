n = int(input())
l = list(map(int, input().split()))
l.sort()   

target = 1
for i in range(n):
    if target < l[i]:
        break
    target += l[i]

print(target)
    
# solution
# 1~i-1번째 까지 만들 수 있는 금액 집합 C가 있다 해보자.
# i 번째 금액을 I라고 해보자
# 그럼 1~i 번째까지 만들 수 있는 금액은 
# {C의 원소} + {C의 원소 + I} 가 될 것이다
# C의 원소가 1부터 연속된 숫자로 이어져 있다는 가정이 있다면,
# C의max+1(target) 이 {C의 원소+I}에 포함되기위해선 C의min+I가 C의max+1보다 작거나 같아야 한다
# => C의max+1 >= C의min+I
# => target >= 1+I
# => target > I
# 이 조건을 만족해야 함!!!!

# 순회를 하기 전, C는 공집합 일 것이고
# 아직 아무 숫자도 없으므로 첫번째 타겟을 1로 설정할 수 있다
