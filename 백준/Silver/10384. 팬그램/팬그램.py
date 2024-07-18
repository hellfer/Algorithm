from collections import Counter
import string

def check_pangram(s):
    s = s.lower()
    counter = Counter(s)
    
    alphabet_count = {char: counter[char] for char in string.ascii_lowercase}
    
    min_count = min(alphabet_count.values())
    
    if min_count >= 3:
        return "Triple pangram!!!"
    elif min_count >= 2:
        return "Double pangram!!"
    elif min_count >= 1:
        return "Pangram!"
    else:
        return "Not a pangram"

t = int(input())

for i in range(t):
    x = input()
    result = check_pangram(x)
    print(f"Case {i + 1}: {result}")
