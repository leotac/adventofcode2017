G = dict()
with open("day19.txt") as f:
	for i,l in enumerate(f):
		for j,c in enumerate(l.strip("\n")):
			if c != ' ':
				G[i,j] = c
				if i == 0:
					start = (i,j)

pos = start
print("Start at", pos)
dir = [1, 0]
letters = "" 
count = 0
while True:
	count += 1
	pos = (pos[0] + dir[0], pos[1] + dir[1])
	if pos not in G:
		print("End at", pos)
		break
	elif G[pos] == "+":
		if dir[0] == 0:
			dir[1] = 0
			dir[0] = 1 if ((pos[0] + 1, pos[1]) in G) else -1
		else:
			dir[0] = 0
			dir[1] = 1 if ((pos[0], pos[1] + 1) in G) else -1
	elif G[pos] not in ("|","-"):
		letters += G[pos]

print(letters)
print(count)
