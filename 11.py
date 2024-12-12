import math
from collections import Counter

stones = None

with open('11_input.txt', 'r') as file:
    for line in file:
        stones = Counter(map(int, line.split(' ')))

def blink_one_stone(stone):
    if stone > 0:
        length = int(math.log10(stone))+1

        if length % 2 == 0:
            divisor = 10 ** (length // 2)
            
            l = stone // divisor
            r = stone % divisor
            
            return [l, r]
        else:
            return [stone * 2024]
    elif stone == 0:
        return [1]

def blink_all_stones(stones):
    new_stones = Counter()

    for stone, count in stones.items():
        for new_stone in blink_one_stone(stone):
            new_stones[new_stone] += count

    return new_stones

# Change this for part1/2 (25 -> 75)
for i in range(75):
    print(i)
    stones = blink_all_stones(stones)

print(f"Total: {sum(stones.values())}")
