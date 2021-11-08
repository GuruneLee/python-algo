# 정윤이가 추천해준 그리디 문제
# 같은 문자일 때 어떤 문자를 골라야 하는지가 핵심

n = int(input())

sl = []
for _ in range(n):
    sl.append(input().rstrip())
so = [0]*n


def d(s1, s2):
    i = 0
    while True:
        if len(s1) == i and len(s2) == i:
            return s1
        if len(s1) == i:
            return s2
        if len(s2) == i:
            return s1
        if s1[i] > s2[i]:
            return s2
        if s1[i] < s2[i]:
            return s1
        i += 1


re = ""
while True:
    # 현재 고를 수 있는 것 중 가장 작은거 고르기 (같다면 d 함수 ㄱㄱ)
    m = ""
    csi = 0
    flag = False
    for i in range(n):
        if len(sl[i]) == so[i]:
            continue
        flag = True
        if m == "":
            m = sl[i][so[i]:]
            csi = i
        else:
            if m != d(m, sl[i][so[i]:]):
                m = sl[i][so[i]:]
                csi = i
    if not flag:
        break
    re += sl[csi][so[csi]]
    # 고른 s 에 대해 해당 so를 +=1 하기
    so[csi] += 1
print(re)
