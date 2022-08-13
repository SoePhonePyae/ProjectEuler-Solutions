L = 1000000
hailstone = lambda n: 3*n + 1 if n%2 else n//2

def d(n, _={1:1}):
    if n not in _: _[n] = d(hailstone(n)) + 1
    return _[n]

print (max(range(1, L), key=d))
