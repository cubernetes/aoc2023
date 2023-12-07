#!/usr/bin/env python3

import re
import sys
import math
from functools import lru_cache
from collections import deque, defaultdict


data = open(0).read().strip()
lines = data.splitlines()

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def get_hand_type(hand):
    cards = defaultdict(int)
    for card in hand:
        cards[card] += 1
    cards = sorted(cards.items(), key=lambda tup: tup[1], reverse=True)
    if cards[0][1] == 5:
        return 'five of a kind'
    elif cards[0][1] == 4:
        return 'four of a kind'
    elif cards[0][1] == 3 and cards[1][1] == 2:
        return 'full house'
    elif cards[0][1] == 3 and cards[1][1] == 1:
        return 'three of a kind'
    elif cards[0][1] == 2 and cards[1][1] == 2:
        return 'two pair'
    elif cards[0][1] == 2 and cards[1][1] == 1:
        return 'one pair'
    elif cards[0][1] == 1:
        return 'high card'

def card_from_card_id(card_id):
    return {
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
    }[card_id]

def glob_joker(hand):
    joker_count = hand.count('J')
    if joker_count == 0:
        yield hand
        return
    for n in range(13 ** joker_count):
        pattern = numberToBase(n, 13)
        pattern = [0] * (joker_count - len(pattern)) + pattern
        tmp_hand = hand.replace('J', '<J>')
        for card_id in pattern:
            tmp_hand = tmp_hand.replace('<J>', card_from_card_id(card_id), 1)
        yield tmp_hand

def hand_type_strength(hand_type):
    return {
        None: -1,
        'high card':       0,
        'one pair':        1,
        'two pair':        2,
        'three of a kind': 3,
        'full house':      4,
        'four of a kind':  5,
        'five of a kind':  6,
    }[hand_type]

def get_hand_type_with_joker(joker_hand):
    best_hand_type = None
    for candidate_hand in glob_joker(joker_hand):
        hand_type = get_hand_type(candidate_hand)
        if hand_type_strength(hand_type) > hand_type_strength(best_hand_type):
            best_hand_type = hand_type
    return best_hand_type

def card_to_digit(card):
    return {
        'J': '0',
        '2': '1',
        '3': '2',
        '4': '3',
        '5': '4',
        '6': '5',
        '7': '6',
        '8': '7',
        '9': '8',
        'T': '9',
        'Q': 'A',
        'K': 'B',
        'A': 'C',
    }[card]

def as_base_13(hand):
    to_convert = list(hand)
    num = ''
    for card in to_convert:
        num += card_to_digit(card)
    return num

sorted_cards = []
for line in lines:
    joker_hand, bid = line.split()
    bid = int(bid)
    hand_type = get_hand_type_with_joker(joker_hand)
    as_number = int(as_base_13(joker_hand), 13)
    sorted_cards.append((joker_hand, bid, hand_type, hand_type_strength(hand_type), as_number))
sorted_hands = sorted(sorted_cards, key=lambda tup: tup[3:5])

total = 0
for i, hand in enumerate(sorted_hands):
    print(i+1, hand)
    total += (i+1) * hand[1]
print(total)
