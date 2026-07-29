import math
from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = Counter(s)
        
        # Identify the middle character if length is odd
        mid_char = ""
        half_counts = [0] * 26  # Map 'a'-'z' to indices 0-25 for faster array access
        odd_count = 0
        
        for char, count in counts.items():
            if count % 2 == 1:
                odd_count += 1
                mid_char = char
            half_counts[ord(char) - ord('a')] = count // 2
            
        # A valid palindrome can have at most one character with an odd frequency
        if odd_count > 1:
            return ""
            
        # Total characters required to form the first half
        half_len = sum(half_counts)
        
        # Precompute factorials up to the maximum possible half length
        fact = [1] * (half_len + 1)
        for i in range(1, half_len + 1):
            fact[i] = fact[i - 1] * i

        # Helper to compute unique permutations of the remaining characters from scratch
        def get_total_permutations(rem_counts, rem_len):
            denom = 1
            for count in rem_counts:
                if count > 0:
                    denom *= fact[count]
            return fact[rem_len] // denom

        # Check if k is out of total possible range initially
        total_possible = get_total_permutations(half_counts, half_len)
        if k > total_possible:
            return ""

        # Step 2: Digit-by-digit placement (Lexicographical Greedy approach)
        first_half = []
        current_len = half_len
        
        # current_total keeps track of permutations for the current remainder state
        current_total = total_possible 

        for i in range(half_len):
            # We want to find the character for the current position
            for c_idx in range(26):
                count = half_counts[c_idx]
                if count == 0:
                    continue
                
                # If we pick this character, the number of combinations left is:
                # perms = (current_total * count) // current_len
                perms_with_char = (current_total * count) // current_len
                
                if k <= perms_with_char:
                    # Target lies within this character group
                    first_half.append(chr(ord('a') + c_idx))
                    half_counts[c_idx] -= 1
                    current_total = perms_with_char
                    current_len -= 1
                    break
                else:
                    # Target is further down; skip these permutations
                    k -= perms_with_char
                        
        # Step 3: Mirror the first half to build the full palindrome
        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]