## Day 6: 1d-DP , 2d-DP

### 1. Decode Ways 
**Problem Statement:**  
You receive a message containing digits from 1 to 9. Each digit or pair of digits can represent a letter (1 -> A, 2 -> B, ..., 26 -> Z). Determine the total number of ways to decode the message using dynamic programming.

This is commonly applied in secure communication systems and encoding/decoding protocols. 

**Examples:**  
Input: `"226"`  
Output: `3`
Explanation: "226" can be interpreted as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6)

Input: `"2007"`
Output: `0`
Explanation: 0 cannot be mapped to any letter unless paired correctly. No valid way exists.

Input: `"20007"`
Output: `0`

 [LeetCode: Decode Ways](https://leetcode.com/problems/decode-ways/)

---

## 2 Unique Paths in Grid 
**Problem Statement:**  
You're standing in the top-left corner of an m x n grid. You can only move down or right. How many unique paths exist to reach the bottom-right corner?

Used in robotics and path planning algorithms. 

**Examples:**  
Examples:

Input: `3 3`
Output: `6`
Explanation: There are 6 possible ways to move from top-left to bottom-right on a 3x3 grid.

Input: `2  2`
Output: `2`

Input: `1 5`
Output: `1`

Input: `4 3`
Output: `10`

Input: `4 1`
Output: `1`

 [LeetCode: Unique paths](https://leetcode.com/problems/unique-paths/)

---
