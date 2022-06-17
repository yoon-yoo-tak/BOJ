n = int(input())
people = dict()
for _ in range(n):
    a, b = input().split()
    if b == 'enter':
        people[a] = 1
    else:
        people[a] = 0
left_person = sorted([i for i in people if people[i]], reverse = True)
for i in left_person:
    print(i)

