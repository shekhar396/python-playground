from math import pi,sin as m_sin
pi = 3.14
print(pi)


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))

print(m_sin(pi / 2))


