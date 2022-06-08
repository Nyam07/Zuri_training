# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    x = [word[i] for i in range(0, len(word))]
    x.sort()

    y = [anagram[i] for i in range(0, len(anagram))]
    y.sort()

    if (x == y):
        return True
    return False

print(find_anagram('hello', 'check'))
print(find_anagram('below', 'elbow'))
