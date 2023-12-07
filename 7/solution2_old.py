#!/usr/bin/env python3

import re
import sys
import math
from functools import lru_cache
from collections import deque, defaultdict


data = open(0).read().strip()
lines = data.splitlines()

card_power = {
    'J': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}

card_power2 = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13,
}

def get_power(candidate_hand, hand):
    cards = {}
    for card in candidate_hand:
        if card not in cards:
            cards[card] = 0
        cards[card] += 1
    cards = sorted(cards.items(), key=lambda tup: tup[1], reverse=True)
    strength = 0
    for i, card in enumerate(hand):
        strength += 14**(len(hand) - i) * card_power[card]
    if len(cards) == 1 and cards[0][1] == 5:
        return 1e14 + strength
    elif len(cards) == 2 and cards[0][1] == 4:
        return 1e13 + strength
    elif len(cards) == 2 and cards[0][1] == 3 and cards[1][1] == 2:
        return 1e12 + strength
    elif len(cards) == 3 and cards[0][1] == 3:
        return 1e11 + strength
    elif len(cards) == 3 and cards[0][1] == 2 and cards[1][1] == 2:
        return 1e10 + strength
    elif len(cards) == 4 and cards[0][1] == 2:
        return 1e9 + strength
    elif len(cards) == 5:
        return 1e8 + strength
    return 0

n_to_card_map = {
    0: '2',
    1: '3',
    2: '4',
    3: '5',
    4: '6',
    5: '7',
    6: '8',
    7: '9',
    8: 'T',
    9: 'J',
    10: 'Q',
    11: 'K',
    12: 'A',
}

def hand_from_list(hand, N):
    js = [n_to_card_map[n] for n in N]
    hand = hand.replace('J', '<J>')
    for j in js:
        hand = hand.replace('<J>', j, 1)
    return hand

def generate_hands(hand):
    num_J = hand.count('J')
    if num_J == 0:
        yield hand
        return
    N = [0] * num_J
    MAX = [12] * num_J
    while N != MAX:
        yield hand_from_list(hand, N)
        N[-1] += 1
        for i in range(num_J - 1, 0, -1):
            if N[i] == 13:
                N[i] = 0
                N[i-1] += 1
    yield hand_from_list(hand, N)

A = []
for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    max_power = 0
    for candidate_hand in generate_hands(hand):
        power = get_power(candidate_hand, hand)
        if power > max_power:
            max_power = power
    A.append((hand, bid, max_power))
A = sorted(A, key=lambda tup: tup[2])

t = 0
for i, a in enumerate(A):
    print(i+1, a)
    t += (i+1) * a[1]

print(t)

# part 2
# wrong: 250103135
# wrong: 250055872
