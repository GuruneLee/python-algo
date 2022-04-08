def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def union_all(parent, l):
    root = l[0]
    for i in range(1, len(l)):
        union(parent, root, l[i])


n, m = map(int, input().split())

parent = [i for i in range(n+1)]

tmp = list(map(int, input().split()))
t_num = tmp[0]
true = list(tmp[1:])

as_party = [[] for _ in range(m)]
as_people = [[] for _ in range(n+1)]
for i in range(m):
    tmp = list(map(int, input().split()))
    p_num = tmp[0]
    for j in range(1, p_num+1):
        as_people[tmp[j]].append(i)
        as_party[i].append(tmp[j])
for i in range(m):
    union_all(parent, as_party[i])

true_group = set()
true_party = set()

for e in true:
    true_group.add(find_parent(parent, e))

for i in range(1, n+1):
    if find_parent(parent, i) in true_group:
        for party in as_people[i]:
            true_party.add(party)

print(m-len(true_party))
