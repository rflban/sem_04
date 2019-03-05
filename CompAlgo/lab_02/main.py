import sys


def read_table(infile):

    x = []
    y = []

    for line in infile:

        temp = str(line).split()

        x.append(float(temp[0]))
        y.append(float(temp[1]))

    return x, y


def main():

    argv = sys.argv

    if (len(argv) < 2):

        argv.append(input("Введите имя входного файла: "))

    infile = open(argv[1], 'r')
    x, y = read_table(infile)
    infile.close()

    for i in range(len(x)):

        print(x[i], y[i])

    h = [0] * len(x)
    xi = [0] * len(x) + [0]
    eta = [0] * len(x) + [0]

    for i in range(1, len(x)):

        h[i] = x[i] - x[i - 1]

    for i in range(2, len(h)):

        Ai = h[i - 1]
        Bi = -2 * (h[i - 1] + h[i])
        Di = h[i]
        Fi = y[i]

        xi[i + 1] = Di / (Bi - Ai * xi[i])
        eta[i + 1] = (Fi + Ai * eta[i]) / (Bi - Ai * xi[i])

    a = [0] * len(x)
    b = [0] * len(x)
    c = [0] * len(x) + [0]
    d = [0] * len(x)

    for i in range(len(x) - 1, 1, -1):

        c[i] = xi[i + 1] * c[i + 1] + eta[i + 1]

    for i in range(1, len(x)):

        a[i] = y[i - 1]
        d[i] = (c[i + 1] - c[i]) / (3 * h[i])
        b[i] = (y[i] - y[i - 1]) / h[i] - 1 / 3 * h[i] * (c[i + 1] + 2 * c[i])

    xarg = float(input('Введите x: '))

    k = 0
    while (xarg > x[k]):
        k += 1
    k -= 1

    res = a[k] + b[k] * (xarg - x[k - 1]) + c[k] * (xarg - x[k - 1])**2 + d[k] * (xarg - x[k - 1])**3

    print(res)


if (__name__ == '__main__'):
    main()

