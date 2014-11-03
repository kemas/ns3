import json

def load(filename):
    with open(filename) as f:
        obj = json.load(f)

    return obj

def gethubs(thold, indegrees):
    ls = []; lsidx = []

    i = 0
    for deg in indegrees:
        if deg >= thold:
            ls.append(deg)
            lsidx.append(i)
        
        i += 1

    return ls, lsidx

#if __name__ == '__main__':
#    sys.exit(main(sys.argv))
