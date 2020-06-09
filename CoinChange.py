from typing import List


# class Solution:
def change(amount: int, coins: List[int]) -> int:
    coins.insert(0, 0)
    rows = len(coins)
    cols = amount + 1
    state = [[0 + (0 == i) for i in range(cols)] for j in range(rows)]
    for c in range(1, rows):
        for a in range(1, cols):
            if coins[c] <= a:
                state[c][a] = state[c][a - coins[c]] + state[c - 1][a]
            else:
                state[c][a] = state[c - 1][a]
    return state[rows - 1][amount]


# Local test
coins = [0, 1, 2, 5]
amount = 50
print(change(amount, coins))
