from collections import deque

def predictPartyVictory(senate: str) -> str:
    n, radiant, dire = len(senate), deque(), deque()
    # Initialize queues with the indices of R and D
    for i, s in enumerate(senate):
        if s == 'R': radiant.append(i)
        else: dire.append(i)
    # Simulate the rounds
    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()
        # The one with the lower index bans the other
        if r < d:
            # Radiant bans Dire, Radiant goes to the back with updated index
            radiant.append(r + n)
        else:
            # Dire bans Radiant, Dire goes to the back with updated index
            dire.append(d + n)
    return "Radiant" if radiant else "Dire"
print(predictPartyVictory("RD"))       # Radiant
print(predictPartyVictory("RDD"))      # Dire
print(predictPartyVictory("RRDDD"))    # Radiant
print(predictPartyVictory("DRRDRDRD")) # Radiant
print(predictPartyVictory("RDRDRDRD")) # Radiant