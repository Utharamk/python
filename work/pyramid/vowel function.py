def count_vowels(s):
    s = s.lower()
    vowel_count = 0
    for char in s:
        if char in 'aeiou':
            vowel_count += 1
    return vowel_count
print(count_vowels("Hello World"))