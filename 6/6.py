import functools
from collections import Counter

def hand_rank(hand):
    # Count the frequency of each card in the 
    
    count_J = hand.count("J")
    c_hand = hand.replace("J", "")

    counts = Counter(c_hand)
    freqs = sorted(counts.values(), reverse=True)

    if len(freqs) == 0:
        freqs = [0]
    freqs[0] += count_J
    # cards = sorted(hand, key=lambda x: (-counts[x], x), reverse=True)


    # Define hand types based on frequency patterns
    if freqs == [5]:
        return (8, hand)
    elif freqs == [4, 1]:
        return (7, hand)
    elif freqs == [3, 2]:
        return (6, hand)
    elif freqs == [3, 1, 1]:
        return (5, hand)
    elif freqs == [2, 2, 1]:
        return (4, hand)
    elif freqs == [2, 1, 1, 1]:
        return (3, hand)
    else:  # freqs == [1, 1, 1, 1, 1]
        return (2, hand)

def compare(x, y):
    rank_x, cards_x = hand_rank(x[0])
    rank_y, cards_y = hand_rank(y[0])
    
    # First, compare the hand types
    if rank_x == rank_y:

        # If hand types are the same, compare individual card ranks
        n = {
            "A": 1, "K": 2, "Q":3, "J":13, "T":4, "9":5, "8":6, "7":7, "6":8, "5":9, "4":10, "3":11, "2":12
        }

        for cx, cy in zip(cards_x, cards_y):
            if n[cx[0]] < n[cy[0]]:
                return 1
            elif n[cx[0]] > n[cy[0]]:
                return -1
        # If all cards are the same, the hands are equal
        return 0
    else:
        return rank_x - rank_y

# Example usage:
hand2 = "KK677"  # Five of a kind
hand1 = "KTJJT"  # Four of a kind
# print(sorted([hand1, hand2], key=functools.cmp_to_key(compare)))  # Should return 1, since hand1 is stronger
print(hand_rank("32T3K"))
print(hand_rank("KK677"))
print(hand_rank("KTJJT"))
print(hand_rank("T55J5"))
print(hand_rank("QQQJA"))
# print(compare("T55J5", "QQQJA"))
# print(compare("KTJJT", "KK677"))



# Insertion sort with custom comparator
def insertion_sort(arr, compare):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and compare(arr[j-1], arr[j]) > 0:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

# Example usage:

lines = [x.split() for x in open("6").readlines()]
# test = ["T55J5", "QQQJA", "KTJJT", "KK677"]

res = insertion_sort(lines, compare)

s = 0
for i,x in enumerate(res):
    s += int(x[1])*(i+1)

print(s)