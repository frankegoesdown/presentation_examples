lst = range(1, 10002)

def chunks(l, n):
    return [l[i:i + n] for i in range(0, len(l), n)]

print(chunks(lst, 10))