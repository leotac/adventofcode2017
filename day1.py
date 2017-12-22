with open("day1.txt") as f:
    s = f.read()

l = len(s)
tot = sum(int(c) for i,c in enumerate(s) if s[i] == s[(i+1)%l])
print("1st star", tot)

tot = sum(int(c) for i,c in enumerate(s) if s[i] == s[(i+int(l/2))%l])
print("2nd star", tot)
