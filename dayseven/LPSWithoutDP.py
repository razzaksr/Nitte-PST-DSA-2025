def max_len_palindrome(string):
    max_len =0
    for k in range(len(string)):
        # even palindrome
        i=k-1
        j=k+1
        while i>=0 and j<len(string) and string[i]==string[j]:
            max_len = max(max_len,j-i+1)
            i-=1
            j+=1
            
        # odd 
        i=k
        j=k+1
        while i>=0 and j<len(string) and string[i]==string[j]:
            max_len = max(max_len,j-i+1)
            i-=1
            j+=1
    return max_len

print(max_len_palindrome("HLHLHHL"))
print(max_len_palindrome("HHLLHH"))
print(max_len_palindrome("HHHL"))