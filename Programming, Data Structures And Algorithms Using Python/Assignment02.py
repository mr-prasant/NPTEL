memory = []
braces = []

def isPrime(n):
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True

def setPrimes(n):
    for i in range(2, n):
        if (isPrime(i)):
            memory.append(i)

def primepartition(m):
    setPrimes(m)
    print(memory)
    for i in range(0, len(memory) - 1):
        low = memory[i]
        for j in range(len(memory)-1, i, -1):
            high = memory[j]
            if low + high == m:
                return True
    return False

def matched(s):
    idx = -1
    for i in range(0, int(len(s))):
        if s[i] == '(':
            braces.append(s[i])
            idx = idx + 1
            
        elif s[i] == ')':
            if idx > -1:
                if braces[idx] == '(':
                    braces.pop()
                    idx = idx - 1
                else:
                    return False
            else:
                braces.append(s[i])
        
    if len(braces) == 0:
        return True
    else:
        return False

def rotatelist(l, k):
    # base case
    if k < 0:
        print(l)
        return l
    
    rotate = []
    k = k % len(l)
    for i in range(k, int(len(l))):
        rotate.append(l[i])
    
    for i in range(0, k):
        rotate.append(l[i])

    print(rotate)