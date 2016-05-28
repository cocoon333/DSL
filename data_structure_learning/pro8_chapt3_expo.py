def expo(number, exponent):
    if exponent == 0:
        return 1
    return number *= expo(number, exponent-1)

if __name__ == '__main__':
    assert(expo(5, 3) == 125)
