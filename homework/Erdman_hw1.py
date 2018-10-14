#Monica Erdman
#Homework 1
#Python for programmers

def kaprekar(x):
    x_str = '{0:04d}'.format(x)
    x_sortUp = ''.join(sorted(x_str))
    x_sortDown = ''.join(sorted(x_str,reverse=True))
    x_Up, x_Down = (int(x_sortUp), int(x_sortDown))
    y = x_Down - x_Up

    return y

def kap_iter(x):
    x_orig = str(x)
    count = 0
    while not (x == 6174 or x == 0):
        x = kaprekar(x)
        count += 1
        print(count, x)
    print('For ', x_orig,' total loops: ',count)
    return count, x

run1 = kap_iter(8730)

run2 = kap_iter(9730)
