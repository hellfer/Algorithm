def can_form_mobis(s):
    required = {'M': 1, 'O': 1, 'B': 1, 'I': 1, 'S': 1}

    from collections import Counter
    count = Counter(s)
    
    for char, needed in required.items():
        if count[char] < needed:
            return "NO"
    
    return "YES"

input_string = input().strip()

print(can_form_mobis(input_string))
