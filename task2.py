t = ['a', 'a', 'b']

def hist(x):
    hist = {}
    for item in x:
        hist[item] = hist.get(item, 0) + 1
    return hist
    
hist = hist(t)

def choose_hist(hist):
    list_ = []
    for key in hist:
        for i in range(0, hist[key]):
            list_.append(key)
    return random.choice(list_)
    
def statistics():
    a = 0
    b = 0
    for i in range(0, 10000):
        if choose_hist(hist) == 'a':
            a += 1
        else:
            b += 1
    print ("a: %.5f" % (a / 10000.0), "b: %.5f" % (b / 10000.0))
    
statistics()

