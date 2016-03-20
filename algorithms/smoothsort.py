# Code from https://github.com/toroidal-code/smoothsort-py


def isAscending(v1, v2):
    """Comparator function"""
    return v1 <= v2


def up(vb, vc):
    temp = vb
    vb += vc + 1
    vc = temp
    return vb, vc


def down(vb, vc):
    temp = vc
    vc = vb - vc - 1
    vb = temp
    return vb, vc


def sort(A):
    """The main sort function
        Variables: q,r,p,b,c,r1,b1,c1,N
    """

    def sift():
        r0 = sort.r1
        T = A[r0]
        while sort.b1 >= 3:
            r2 = sort.r1 - sort.b1 + sort.c1

            if not isAscending(A[sort.r1 - 1], A[r2]):
                r2 = sort.r1 - 1
                sort.b1, sort.c1 = down(sort.b1, sort.c1)
            if isAscending(A[r2], T):
                sort.b1 = 1
            else:
                A[sort.r1] = A[r2]
                sort.r1 = r2
                sort.b1, sort.c1 = down(sort.b1, sort.c1)
        if sort.r1 != r0:
            A[sort.r1] = T

    def trinkle():
        p1 = sort.p
        sort.b1 = sort.b
        sort.c1 = sort.c
        r0 = sort.r1
        T = A[r0]
        while p1 > 0:
            while (p1 & 1) == 0:
                p1 >>= 1
                sort.b1, sort.c1 = up(sort.b1, sort.c1)
            r3 = sort.r1 - sort.b1
            if p1 == 1 or isAscending(A[r3], T):
                p1 = 0
            else:
                p1 -= 1
                if sort.b1 == 1:
                    A[sort.r1] = A[r3]
                    sort.r1 = r3
                elif sort.b1 >= 3:
                    r2 = sort.r1 - sort.b1 + sort.c1
                    if not isAscending(A[sort.r1 - 1], A[r2]):
                        r2 = sort.r1 - 1
                        sort.b1, sort.c1 = down(sort.b1, sort.c1)
                        p1 <<= 1
                    if isAscending(A[r2], A[r3]):
                        A[sort.r1] = A[r3]
                        sort.r1 = r3
                    else:
                        A[sort.r1] = A[r2]
                        sort.r1 = r2
                        sort.b1, sort.c1 = down(sort.b1, sort.c1)
                        p1 = 0
        if r0 != sort.r1:
            A[sort.r1] = T
        sift()

    def semitrinkle():
        sort.r1 = sort.r - sort.c
        if not isAscending(A[sort.r1], A[sort.r]):
            A[sort.r], A[sort.r1] = A[sort.r1], A[sort.r]
            trinkle()

    # Start of main function
    sort.N = len(A)
    sort.q = 1
    sort.r = 0
    sort.p = 1
    sort.b = 1
    sort.c = 1
    #building the tree
    while sort.q < sort.N:
        sort.r1 = sort.r

        if (sort.p & 7) == 3:
            sort.b1 = sort.b
            sort.c1 = sort.c
            sift()
            sort.p = (sort.p + 1) >> 2
            sort.b, sort.c = up(sort.b, sort.c)
            sort.b, sort.c = up(sort.b, sort.c)
        elif (sort.p & 3) == 1:
            if (sort.q + sort.c) < sort.N:
                sort.b1 = sort.b
                sort.c1 = sort.c
                sift()
            else:
                trinkle()
            sort.b, sort.c = down(sort.b, sort.c)
            sort.p <<= 1
            while sort.b > 1:
                sort.b, sort.c = down(sort.b, sort.c)
                sort.p <<= 1
            sort.p += 1
        sort.q += 1
        sort.r += 1

    sort.r1 = sort.r
    trinkle()

    # build the sorted array
    while sort.q > 1:
        sort.q -= 1
        if sort.b == 1:
            sort.r -= 1
            sort.p -= 1
            while (sort.p & 1) == 0:
                sort.p >>= 1
                sort.b, sort.c = up(sort.b, sort.c)
        elif sort.b >= 3:
            sort.p -= 1
            sort.r = sort.r - sort.b + sort.c
            if sort.p > 0:
                semitrinkle()
            sort.b, sort.c = down(sort.b, sort.c)
            sort.p = (sort.p << 1) + 1
            sort.r += sort.c
            semitrinkle()
            sort.b, sort.c = down(sort.b, sort.c)
            sort.p = (sort.p << 1) + 1
            # element q is done
        # element 0 is done
    return A
