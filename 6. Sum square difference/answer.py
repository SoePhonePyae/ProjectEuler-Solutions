def diff(limit):
    _sum = 0
    _pow = 0
    for i in range(1, limit+1):
        _sum += i
        _pow += i**2

    _sum **=  2

    print(_sum - _pow)

diff(100)
