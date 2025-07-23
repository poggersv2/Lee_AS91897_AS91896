lambda: argument("item 1", "item 2")

def argument(*args):
    l =[]
    pos = 0
    for item in args:
        pos += 1
        l.append(item)
        print(pos, item)

