# Identical words are forbidden
with open("day4.txt") as f:
    count = 0
    for l in f:
        words = l.strip().split()
        if len(set(words)) == len(words):
            count += 1
print(count)

# Anagrams are forbidden
with open("day4.txt") as f:
    count = 0
    for l in f:
        words = ["".join(sorted(x)) for x in l.strip().split()]
        if len(set(words)) == len(words):
            count += 1
print(count)
