# Day-2  Arrays and Strings

# Arrays

## 1. Missing Invoice Number

**Problem:** In a supermarket, at the end of the day, identify the missing invoice number from a sequential list.

**Example:**
Input: 8, 10, 3, 1, 4, 2, 5
Output: 6
Input: 45, 91, 90, 92, 46
Output: 47
Input: 0, 1, 2, 4, 5, 6, 7
Output: 3

[LeetCode: Missing Number](https://leetcode.com/problems/missing-number)

---

## 2. Extra Debit Charges

**Problem:** For the last 10 bank transactions (positive = credit, negative = debit), apply a ₹20 charge for each debit after the first three.

**Example:**

Input: `900, 1200, 5600, 120, 450, 670, 100, 10000, 400, 120`  
Output: `900, 1200, 5600, 120, 450, 670, 100, 10000, 400, 96`

[LeetCode (Similar): Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls)

---

## 3. Distinct Digits in Array

**Problem:** Extract all unique digits present across an array of integers.

**Example:**

Input: `[131, 11, 48]`  
Output: `1 3 4 8`  

Input: `[111, 222, 333, 4444, 666]`  
Output: `1 2 3 4 6`

[LeetCode (Similar): Unique Digits](https://leetcode.com/problems/unique-length-3-palindromic-subsequences)

---

## 4. Twisted Prime

**Problem:** A number is a twisted prime if it's a prime and its reverse is also a prime.

**Example:**

Input: `97`  
Output: `1`  

Input: `43`  
Output: `0`  

[LeetCode (Similar): Reverse Integer + Prime Test](https://leetcode.com/problems/reverse-integer)

---

## 5. Least Prime Addition for Divisibility

**Problem:** Add the least prime number (within a boundary) to `arr1[i]` so that it becomes divisible by `arr2[i]`.

**Example:**

Input: `arr1 = [3, 5, 7], arr2 = [10, 15, 20]`  
Output: `7 -1 13`

Input: `arr1 = [4, 6, 8], arr2 = [5, 10, 15]`  
Output: `-1 -1 -1`

[LeetCode (Similar): Smallest Number in Infinite Set](https://leetcode.com/problems/smallest-number-in-infinite-set)

---

# Strings

## 6. Subsequence Checker

**Problem:** Check if string A is a subsequence of string B.

**Example:**

Input: `A = TCS, B = Tata Service`  
Output: `0`  

Input: `A = infy, B = infosys`  
Output: `1`  

Input: `A = cts, B = cognizant technology`  
Output: `0`  

[LeetCode: Is Subsequence](https://leetcode.com/problems/is-subsequence)

---

## 7. Minimum Moves to Convert String

**Problem:** Convert a string consisting of 'X' and 'O' to all 'O's using the fewest moves. A move consists of changing any 3 consecutive characters to 'O'.

**Example:**

Input: `XXX`  
Output: `1`  

Input: `XXOX`  
Output: `2`  

Input: `OOOO`  
Output: `0`  

[LeetCode: Minimum Moves to Convert String](https://leetcode.com/problems/minimum-moves-to-convert-string)

---

## 8. Customer Account Validation

**Problem:** Validate customer's details using regex before creating an account. Fields: Name, Password, Aadhaar, PAN, Email

**Example:**
```
Input:
Name: "Raz"
Password: "razak\$123"
Aadhaar: "765456787912"
PAN: "ABCDE1234F"
Email: "[example@mail.com](mailto:example@mail.com)"
Output: Account created

Input:
Name: "Ra"
Password: "razak\$123"
Aadhaar: "7654567"
PAN: "ABCDE1234F"
Email: "[example@mail.com](mailto:example@mail.com)"
Output: Invalid name, invalid aadhaar

Input:
Name: "Raz"
Password: "razak123"
Aadhaar: "765456787912"
PAN: "ABCDE1234F"
Email: "[example@mail.c](mailto:example@mail.c)"
Output: Invalid password, invalid email
```


[LeetCode (Similar): Validate Email & Password](https://leetcode.com/problems/valid-number)

---

## 9. Validate IPv4 Address

**Problem:** Check if a given string is a valid IPv4 address.

**Example:**
 - Input: "222.111.111.111" Output: true
  - Input: "5555..555"
   Output: false
 - Input: "0.0.0.0255" Output: false

[LeetCode: Validate IP Address](https://leetcode.com/problems/validate-ip-address)

---

## 10. Group Anagrams

**Problem:** Group words that are anagrams of each other.

**Example:**

Input: `["eat","tea","tan","ate","nat","bat"]`

Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`

[LeetCode: Group Anagrams](https://leetcode.com/problems/group-anagrams)
