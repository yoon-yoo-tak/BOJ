"""
암호 만들기
모음 1개 자음 2개
오름차순
c 개 중에 l개 고르는 조합
"""
import sys

input = sys.stdin.readline

l, c = map(int, input().split())
alpha = sorted(input().split())
vowel = 'aeiou'
selected = []
def count_vowel():
    cnt = 0
    for i in selected:
        if i in vowel:
            cnt += 1
    return cnt >= 1


def count_conso():
    cnt = 0
    for i in selected:
        if i not in vowel:
            cnt += 1
    return cnt >= 2


def rec(k, cnt):
    if k == c:
        if cnt == l:
            if count_conso() and count_vowel():
                print(''.join(selected))
    else:
        selected.append(alpha[k])
        rec(k + 1, cnt + 1)
        selected.pop()
        rec(k + 1, cnt)

rec(0, 0)