from collections import defaultdict

class Program:
    def __init__(self, id, code):
        self.id = id
        self.pos = 0
        self.reg = defaultdict(int)
        self.reg['p'] = id
        self.received = []
        self.send_count = 0
        self.code = code

    def val(self, X):
        try:
            return int(X)
        except:
            return self.reg[X]

    def set_target(self, t):
        self.target = t

    def send(self, X):
        self.target.received.append(X)
        self.send_count += 1
    
    def receive(self, X, t):
        if len(self.received) > 0:
            self.reg[X] = self.received[0]
            self.received = self.received[1:]
            return 1
        else:
            return 0
    
    def execute(self, cmd, X, Y = None):
        if cmd == 'snd':
            self.send(self.val(X))
        elif cmd == 'rcv':
            return self.receive(X, self.target)
        elif cmd == 'set':
            self.reg[X] = self.val(Y)
        elif cmd == 'add':
            self.reg[X] += self.val(Y)
        elif cmd == 'mul':
            self.reg[X] *= self.val(Y)
        elif cmd == 'mod':
            self.reg[X] %= self.val(Y)
        elif cmd == 'jgz':
            if self.val(X) > 0:
                return self.val(Y)
        return 1
    
    # Run the list of instructions forever
    def run(self):
        while True:
            self.next()
    
    # Run next instruction
    def next(self):
        v = self.code[self.pos].split()
        if len(v) == 2:
            step = self.execute(v[0], v[1])
        else:
            step = self.execute(v[0], v[1], v[2])
        self.pos += step
        return step

with open("day18.txt") as f:
    code = f.readlines()
 
zero = Program(0, code)    
one = Program(1, code)
zero.set_target(one)
one.set_target(zero)

for i in range(1000000):
    s0 = zero.next()
    s1 = one.next()
    
    #print zero.id, zero.pos, zero.reg, zero.received, zero.send_count
    #print one.id, one.pos, one.reg, one.received, one.send_count
    if s0 == 0 and s1 == 0:
        print "Deadlock at iteration", i
        print "Program 1 send count:", one.send_count
        break
