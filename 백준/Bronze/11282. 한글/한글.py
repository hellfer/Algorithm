initial_consonants = 19
vowels = 21
final_consonants = 28

N = int(input())

N -= 1

initial_index = N // (vowels * final_consonants)
vowel_index = (N % (vowels * final_consonants)) // final_consonants
final_index = N % final_consonants

unicode_value = 44032 + (initial_index * vowels * final_consonants) + (vowel_index * final_consonants) + final_index

hangul_character = chr(unicode_value)

print(hangul_character)
