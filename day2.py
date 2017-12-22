with open("day2.txt") as f:
    checksum = 0
    for l in f:
        v = [int(x) for x in l.split()]
        checksum += max(v) - min(v)
    print(checksum)

def check_div(a,b):
    if a > b:
        d,r = divmod(a,b)
    else:
        d,r = divmod(b,a)
    if r == 0:
        return d
    return 0

with open("day2.txt") as f:
    checksum = 0
    for l in f:
        v = [int(x) for x in l.split()]
        for i in range(len(v)-1):
            for j in range(i+1, len(v)):
                d = check_div(v[i],v[j])
                if d > 0:
                    checksum += d
                    break
    print(checksum)
