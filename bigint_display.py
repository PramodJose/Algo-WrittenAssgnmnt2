string = {}


def multiply(a, b, n, id):  # n is the number of bits; and not the number of digits

    if n == 1:
        label = "@Label: " + bin(a)[2:] + " * " + bin(b)[2:]
        calc = "same"
        string[id] = "Calc: " + calc + label
        return a & b    # multiplication of two bits is basically bitwise AND. Hence, we can write (a * b) as (a & b).

    nR = (n//2)         # number of bits on the right..
    nL = n - nR         # and number of bits on the left...

    aL = a >> (n//2)
    bL = b >> (n//2)

    aR = a & ((1 << nR) - 1)
    bR = b & ((1 << nR) - 1)

    x1 = multiply(aL, bL, nL, id*3 + 1)
    x2 = multiply(aR, bR, nR, id*3 + 3)

    sumA = aL + aR
    sumB = bL + bR
    newN = max(nL, nR)

    if (sumA & (1 << newN) != 0) or (sumB & (1 << newN) != 0):
        newN += 1

    x3 = multiply(sumA, sumB, newN, id*3 + 2)

    if n & 1 != 0:      # if n is odd, then we need to shift x1 by one less place.
        n ^= 1          # same as n -= 1; but slightly faster

    retVal = (x1 << n) + ((x3 - x1 - x2) << nR) + x2

    label = "@Label: " + bin(a)[2:] + " * " + bin(b)[2:]
    calc = str(x1) + " * " + str(1 << n) + " + (" + str(x3) + " - " + str(x1) + " - " + str(x2) + ") * " + str(1 << nR) + " + " + str(x2)

    string[id] = "Calc: " + calc + label
    return retVal


print("result = " + str(multiply(211, 89, 8, 0)) + "\n")

keys = list(string.keys())
keys.sort()
for key in keys:
    text = string[key].split('@')
    print("key=", key, "\t", text[0], "\t\t\t\t", text[1], "\n")