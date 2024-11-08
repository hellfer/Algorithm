first_letter = input().strip()

club_names = {
    'M': 'MatKor',
    'W': 'WiCys',
    'C': 'CyKor',
    'A': 'AlKor',
    '$': '$clear'
}

print(club_names[first_letter])