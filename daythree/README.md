# Day 3: Recursion

---

## 1. Total Revenue Calculation

**Problem:**  
A grocery shop wants to calculate total revenue by summing up all the bills. Help the shopkeeper compute the total using **recursion**.

**Examples:**

- Input: `[900, 20, 450, 210, 60]` → Output: `1640`  
- Input: `[10, 20, 30]` → Output: `60`

[LeetCode: Recursive Sum of Array](https://leetcode.com/problems/sum-of-elements-in-an-array/)

---

## 2. Maximum in Array

**Problem:**  
Find the **maximum value** in an array using recursion.

**Examples:**

- Input: `[0, 4, 5, 3, 7, 2, 1]` → Output: `7`  
- Input: `[10, 15, 3, 1, 9]` → Output: `15`

---

## 3. Minimum Currency Notes

**Problem:**  
You are working on a vending machine software that dispenses change. Given an unlimited supply of currencies of different denominations (e.g., 100, 200, 500 etc.), write a recursive function to determine the **minimum number of notes** needed to make a given amount.

**Examples:**

- Input: `coins = [100, 200, 500]`, `amount = 1100` → Output: `3`  
- Input: `coins = [100, 200, 500]`, `amount = 8700` → Output: `18`

[Leetcode: Coin Change](https://leetcode.com/problems/coin-change/)

---

## 4. Prefix and Postfix Sum

**Problem:**  
Using recursion, calculate both the **prefix sum** and the **postfix sum** of a list of numbers.

**Examples:**

- Input: `[23, 12, 98, 45, 18, 45, 12, 98]`  
  - Output:  
    - Prefix Sum: `[23, 35, 133, 178, 196, 241, 253, 351]`  
    - Postfix Sum: `[351, 328, 316, 218, 173, 155, 110, 98]`

[Leetcode: Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)

---

## 5. Merge Sort

**Problem:**  
Implement **Merge Sort** using recursion.

**Examples:**

- Input: `[38, 27, 43, 3, 9, 82, 10]` → Output: `[3, 9, 10, 27, 38, 43, 82]`  
- Input: `[5, 2, 4, 6, 1, 3]` → Output: `[1, 2, 3, 4, 5, 6]`

[Leetcode: Sort an Array](https://leetcode.com/problems/sort-an-array/)

---

## 6. Inversion Count

**Problem:**  
You are working for an e-commerce company analyzing warehouse efficiency. Count the number of **inversion pairs** using recursion.  
An inversion is a case where a later order took **less time** than an earlier order.

**Examples:**

- Input: `P = [30, 45, 25, 60, 20]`  
  - Output: `6`  
  - Explanation:  
    - Inversion pairs:  
      `(30, 25)`, `(30, 20)`, `(45, 25)`, `(45, 20)`, `(60, 20)`, `(25, 20)`

- Input: `P = [10, 5, 3, 2, 1]` → Output: `10`  
- Input: `P = [1, 2, 3, 4, 5]` → Output: `0`

[Leetcode: Count Inversions (via Merge Sort)](https://leetcode.com/problems/reverse-pairs/)