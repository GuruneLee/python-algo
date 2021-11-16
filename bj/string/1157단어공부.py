# Set 을 이용해보자
# o 를 갱신하면 된다
s = input().upper()
m = 0
for c in set(s):
    count = s.count(c)
    if m == count:
        o = '?'
    if m < count:
        m = count
        o = c
print(o)

# s = input().casefold()
# d = {}
# for c in s:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] += 1

# m = max(d.values())
# mc = ""
# count = 0
# for k in d:
#     if d[k] == m:
#         count += 1
#         mc = k
#     if count > 1:
#         print('?')
#         exit(0)
# print(chr(ord(mc)-ord('a')+ord('A')))
