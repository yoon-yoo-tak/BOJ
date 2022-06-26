n = int(input())
ls = sorted(map(int, input().split()))

ans = 0

def good(target_idx):
    l, r = 0, n - 1
    target = ls[target_idx]
    while l < r:
        if l == target_idx: l += 1
        elif r == target_idx: r -= 1
        else:
            if ls[l] + ls[r] > target: r -= 1
            elif ls[l] + ls[r] < target: l += 1
            else: return True
    return False

print(len([i for i in range(n) if good(i)]))