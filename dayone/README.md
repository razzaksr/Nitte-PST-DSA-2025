# Day 1 - Arrays

## 1. Two Sum

**Problem Statement:**  
Given a list of item prices, find indices of two items whose combined price equals a customer's gift card value.

**Example:**  
Input: `nums = [2, 7, 11, 15]`, `target = 9`  
Output: `[0, 1]`  
Explanation: 2 + 7 = 9

**Real-World Test Cases:**
```json
[
  {"expertId":123,"ctc":4,"role":"developer"},
  {"expertId":456,"ctc":9,"role":"project manager"},
  {"expertId":765,"ctc":6,"role":"devops engineer"},
  {"expertId":912,"ctc":5,"role":"system design engineer"},
  {"expertId":123,"ctc":3,"role":"sdet"}
]
```

- Target: 10 → [developer, devops engineer]  
- Target: 11 → [devops engineer, system design engineer]

**LeetCode Link:** https://leetcode.com/problems/two-sum  

---

## 2. Maximum Subarray (Kadane's Algorithm)

**Problem Statement:**  
Find the contiguous subarray (within a one-dimensional array) with the largest sum.

**Example:**  
Input: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`  
Output: `6`  
Explanation: Subarray `[4, -1, 2, 1]` has the largest sum.

**LeetCode Link:** https://leetcode.com/problems/maximum-subarray

---

## 3. Move Zeroes

**Problem Statement:**  
Rearrange a delivery queue where `0` indicates unavailable trucks. Move all zeros to the end while maintaining the order of the other elements.

**Examples:**

- Input: `[0, 1, 0, 3, 12]` → Output: `[1, 3, 12, 0, 0]`  
- Input: `[20, 0, 19, 5, 0, 3, 10, 0, 2]` → Output: `[20, 19, 5, 3, 10, 2, 0, 0, 0]`  
- Input: `[3, 0, 0, 1, 0, 5, 0, 6, 0]` → Output: `[3, 1, 5, 6, 0, 0, 0, 0, 0]`

**LeetCode Link:** https://leetcode.com/problems/move-zeroes

---

## 4. Best Time to Buy and Sell Stock

**Problem Statement:**  
Find the best day to buy and sell a stock to maximize profit.

**Examples:**

- Input: `[7, 1, 5, 3, 6, 4]` → Buy at `1`, Sell at `6`  
- Input: `[45, 12, 3, 10, 50]` → Buy at `3`, Sell at `50`  
- Input: `[-10, -5, -2, -1, 1]` → Buy at `-10`, Sell at `1`  
- Input: `[90, 40, 20, 10, 4]` → Buy at `10`, Sell at `4` (minimal loss)

**LeetCode Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock

---

## 5. Find Pivot Index

**Problem Statement:**  
Find the index where the sum of the elements to the left is equal to the sum on the right.

**Examples:**

- Input: `[1, 7, 3, 6, 5, 6]` → Output: `3`  
- Input: `[-7, 1, 5, 2, -4, 3, 0]` → Output: `3`  
- Input: `[0, -3, 5, -4, -2, 3, 1, 0]` → Output: `0`

**LeetCode Link:** https://leetcode.com/problems/find-pivot-index

---

## 6. Insert Interval

**Problem Statement:**  
Insert a new interval into an existing list of non-overlapping intervals and merge if necessary.

**Examples:**

- Input: `[[1,3],[6,9]]`, New Interval: `[2,5]`  
  Output: `[[1,5],[6,9]]`

- Input: `[[1,2],[3,5],[6,7],[8,10],[12,16]]`, New Interval: `[4,8]`  
  Output: `[[1,2],[3,10],[12,16]]`  
  Explanation: Overlaps with `[3,5],[6,7],[8,10]`

**LeetCode Link:** https://leetcode.com/problems/insert-interval
---

## 7. Sort Colors (Dutch National Flag Problem)

**Problem Statement:**  
You are part of a support team for the IRCTC app. Issues are prioritized as 0 (high), 1 (medium), and 2 (low). Rearrange the tickets in ascending order of priority.

**Examples:**

- Input: `[2, 0, 0, 1, 0, 2, 0, 1]` → Output: `[0, 0, 0, 0, 1, 1, 2, 2]`  
- Input: `[2, 0, 2, 1, 1, 0]` → Output: `[0, 0, 1, 1, 2, 2]`

**LeetCode Link:** https://leetcode.com/problems/sort-colors

---
