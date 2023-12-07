#!/usr/bin/env python3

import re
import sys
import math
from functools import lru_cache
from collections import deque, defaultdict


data = open(0).read().strip()
lines = data.splitlines()

card_power = {
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

def get_power(hand):
    cards = {}
    for card in hand:
        if card not in cards:
            cards[card] = 0
        cards[card] += 1
    cards = sorted(cards.items(), key=lambda tup: tup[1], reverse=True)
    strength = 0
    for i, card in enumerate(hand):
        print(13**(len(hand) - i) * card_power[card])
        strength += 13**(len(hand) - i) * card_power[card]
    print(strength)
    print()
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
A = []
for line in lines:
    hand, bid = line.split()
    bid = int(bid)
    power = get_power(hand)
    A.append((hand, bid, power))
A = sorted(A, key=lambda tup: tup[2])

t = 0
for i, a in enumerate(A):
    print(i+1, a)
    t += (i+1) * a[1]

print(t)
# wrong: 249261605
# wrong: 249035233
# wrong: 248657893
# correct: 248812215
