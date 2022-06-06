t = int(input())
person = []

for _ in range(t):
    x,y = map(int, input().split())
    person.append((x,y))

for man in person:
    rank = 1
    for other in person:
        if man[0] < other[0] and man[1]<other[1]:
            rank +=1

    print(rank, end=" ")

