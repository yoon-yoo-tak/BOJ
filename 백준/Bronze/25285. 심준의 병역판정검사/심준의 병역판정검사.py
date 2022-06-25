n = int(input())
hw = [list(map(int, input().split())) for _ in range(n)]

def bmi(height, weight):
    return weight / (height ** 2)

for h, w in hw:
    value = bmi(h, w) * 1e4
    if h < 140.1:
        print(6)
    elif h < 146:
        print(5)
    elif h < 159:
        print(4)
    else:
        if h < 161:
            if value < 16 or value >= 35:
                print(4)
            else:
                print(3)
        elif h < 204:
            if 20 <= value < 25:
                print(1)
            elif (18.5 <= value < 20) or (25 <= value < 30):
                print(2)
            elif (16 <= value < 18.5) or (30 <= value < 35):
                print(3)
            elif value < 16 or value >= 35:
                print(4)
        else:
            print(4)