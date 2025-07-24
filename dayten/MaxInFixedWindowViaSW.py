from collections import deque
# Sliding window maximum
def find_max(arr, window):
    result = [0] * (len(arr) - window + 1)
    dq = deque()
    for index in range(len(arr)):
        # Remove indices that are out of this window
        if dq and dq[0] < index - window + 1: dq.popleft()
        # Remove smaller values at the end of deque
        while dq and arr[dq[-1]] <= arr[index]: dq.pop()
        # Add current index
        dq.append(index)
        # Store maximum for current window
        if index >= window - 1: result[index - window + 1] = arr[dq[0]]
    return result

# Example usage
print(find_max([70, 85, 60, 95, 82, 74, 90], 2))
print(find_max([9.2, 8.9, 7.5, 19.9, 14.5, 5.6, 10.4], 2))