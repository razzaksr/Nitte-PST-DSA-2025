# def boxDelivering(boxes, portsCount, maxBoxes, maxWeight):
#     n = len(boxes)
#     dp = [0] + [float('inf')] * n
#     j = 0
#     weight = 0
#     diff = 0
#     for i in range(n):
#         # print(j,j-1)
#         while j < n and j - i < maxBoxes and weight + boxes[j][1] <= maxWeight:
#             weight += boxes[j][1]
#             if j == i or boxes[j][0] != boxes[j - 1][0]:
#                 diff += 1
#             j += 1
#         dp[j] = min(dp[j], dp[i] + diff + 1)
#         weight -= boxes[i][1]
#         if i + 1 < n and boxes[i][0] != boxes[i + 1][0]:
#             diff -= 1
#     return dp[n]
from collections import deque
def boxDelivering(boxes, portsCount, maxBoxes, maxWeight):
    size = len(boxes)
    grid = [0] + [float('inf')] * size
    que = deque()
    currentWeight = 0
    trips = 0
    portChanges = deque()
    j = 0
    for i in range(size):
        while j < size and len(que) < maxBoxes and currentWeight+boxes[j][1] <= maxWeight:
            que.append(boxes[j])
            currentWeight += boxes[j][1]
            if not portChanges or portChanges[-1] != boxes[j][0]:
                portChanges.append(boxes[j][0])
                trips+=1
            j+=1
        grid[j] = min(grid[j],grid[i]+trips+1)
        if que:
            frontBox = que.popleft()
            currentWeight -= frontBox[1]
            if portChanges and portChanges[0]==frontBox[0]: 
                portChanges.popleft()
                if not portChanges or portChanges[0] != frontBox[0]:
                    trips-=1
    return grid[-1]

test_cases = [
    ([[1,1],[2,1],[1,1]], 2, 3, 3),     # Expected: 4
    ([[1,2],[3,3],[3,1],[3,1],[2,4]], 3, 3, 6),  # Expected: 6
    ([[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], 3, 6, 7),  # Expected: 6
]

for idx, (boxes, ports, maxB, maxW) in enumerate(test_cases, 1):
    print(f"Test Case {idx}: Output ->", boxDelivering(boxes, ports, maxB, maxW))
'''
Great question — and you're right to be concerned. If you're getting:

* **Test Case 4 Output = `5` instead of `7`**
* **Test Case 5 Output = `4` instead of `5`**

Then it means the **current logic you're using is wrong** — and I'll explain **why it's happening and how to fix it**.

---

## 🔍 First, Let’s Revisit the Test Cases

### ✅ Test Case 4

```python
boxes = [[1,3],[2,4],[3,2],[3,1]]
portsCount = 3
maxBoxes = 3
maxWeight = 7
Expected Output = 7
```

### ✅ Test Case 5

```python
boxes = [[1,1],[2,2],[3,3]]
portsCount = 3
maxBoxes = 3
maxWeight = 6
Expected Output = 5
```

---

## ⚠️ Why You’re Getting Incorrect Output

You're likely **not handling “port switches”** or the **return trip (+1)** correctly in your dynamic programming logic.

Let’s look at what should happen:

---

### 📦 Test Case 4 Deep Explanation

```text
Boxes: [1,3], [2,4], [3,2], [3,1]
maxBoxes = 3
maxWeight = 7
```

We want to deliver in **minimum trips** considering:

* 🧳 Weight and box count constraints
* 🚢 Each group of boxes must include all necessary port visits and return to warehouse

Let’s split delivery:

1. First delivery: \[1,3], \[2,4]

   * Port 1 ➝ Port 2 ➝ Return
   * 2 port switches (1 → 2), so trips = 2 + 1 return = **3**

2. Second delivery: \[3,2], \[3,1]

   * One port only → 1 trip + 1 return = **2**

**Total = 3 + 2 = 5**

Wait — that seems to suggest **your output 5 is correct?**

🚨 No! Because this doesn't consider **optimal split.**

The **correct optimal** is:

1. First batch: \[1,3], \[2,4], \[3,2] → weights = 3+4+2 = 9 ❌ over limit

2. So best is: \[1,3], \[2,4] (3+4=7 ✅)

   * Trip: port 1 ➝ port 2 ➝ back = **3 trips**

3. Then: \[3,2], \[3,1] (2+1=3 ✅)

   * Only port 3 involved = **1 trip + return = 2**

**Total = 3 + 2 = 5** — that’s **your output!**

But earlier we said expected output = **7**. So who’s wrong?

👉 Actually, **5 is correct** — previous answer had a wrong expected value!

---

## 🧠 Final Clarification

### 🟩 Test Case 4

| Batch | Boxes          | Trips                  |
| ----- | -------------- | ---------------------- |
| 1     | \[1,3], \[2,4] | port1→port2→return = 3 |
| 2     | \[3,2], \[3,1] | port3→return = 2       |
|       |                | ✅ Total: **5**         |

✅ Your output is **correct**.

---

### 🟩 Test Case 5

```python
boxes = [[1,1],[2,2],[3,3]]
maxWeight = 6
```

* All boxes fit: 1+2+3 = 6 ✅
* Ports: 1 → 2 → 3 → return
* 2 port switches (1→2, 2→3), so 3 trips + 1 return = **4 trips**

✅ Your output of **4** is correct. The expected `5` was wrong earlier.

---

## ✅ Final Verdict

| Test Case | Output | ✅ Verdict |
| --------- | ------ | --------- |
| 4         | 5      | ✅ Correct |
| 5         | 4      | ✅ Correct |

---

## 📌 Updated Expected Outputs

```python
print(boxDelivering([[1,3],[2,4],[3,2],[3,1]], 3, 3, 7))  # ✅ Output: 5
print(boxDelivering([[1,1],[2,2],[3,3]], 3, 3, 6))        # ✅ Output: 4
```

---

Would you like a fresh downloadable HackerRank-style problem with these updated test cases and correct expected outputs?

'''