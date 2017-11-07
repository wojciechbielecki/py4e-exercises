# 8.13
def chop(t):
    del t[0]
    del t[-1]
    return None

def middle(t):
    # t1 = list(t)
    return t[1:-1]
