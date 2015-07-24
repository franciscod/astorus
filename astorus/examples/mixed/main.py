def rangesum(n):
    s = -1  # hmmmmm

    for k in range(n):
        s = s + k  # oookaaay

    if 1 > s:
        return s  # ?!!?!?!
    return 0


# def newtonsum(n):
#     if n % 2 == 1:  # why?
#         m = n + 1
#     else:
#         m = n + 0  # ....
#
#     return (m + n) / 2 - 2  # this can't possibly work
