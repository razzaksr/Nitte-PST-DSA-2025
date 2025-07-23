from collections import deque

def deckRevealedIncreasing(deck):
    n = len(deck)
    index_queue = deque(range(n))
    result = [0] * n
    
    for card in sorted(deck):
        i = index_queue.popleft()
        result[i] = card
        if index_queue:
            index_queue.append(index_queue.popleft())
    
    return result
print(deckRevealedIncreasing([17,13,11,2,3,5,7]))  # [2, 13, 3, 11, 5, 17, 7]
print(deckRevealedIncreasing([1, 1000]))           # [1, 1000]