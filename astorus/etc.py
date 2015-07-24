def nsplit(s):
    return [ss + '\n' for ss in s.split('\n')]


def scorediff(d):
    l_additions = 0
    c_adds = 0
    l_deletions = 0
    c_dels = 0
    lines = 0
    chars = 0

    for line in d:
        chs = len(line)
        chars += chs
        lines += 1
        if line[0] == '+':
            l_additions += 1
            c_adds += chs
        if line[0] == '-':
            l_deletions += 1
            c_dels += chs

    #return 1 / (lines + 2* l_additions + 4*l_deletions)
    return (c_dels - 100*c_adds)
