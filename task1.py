def processLine(sin, din):
    line = sin.strip()
    words = line.split()
    for word in words:
        # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        word = word.translate(string.maketrans("",""), string.punctuation + string.digits)
        word = word.lower()
#        if word in din:
#            din[word] += 1
#        else:
#            din[word] = 1
        din[word] = 1 + din.get(word, 0)
    return din
def processFile(fin, processFunc):
    d = dict()
    try:
        myFile = open(fin, 'r')
        for line in myFile.readlines():
            processFunc(line, d)
        distinctWords = len(d) # Get a distinct word count.
        sortedDict = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
        return sortedDict, distinctWords
    except:
        e = sys.exc_info()
        print e
    finally:
        myFile.close()
if __name__ == '__main__':
    bookFile = '/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_13/Books/moby_dick.txt'
    infile = '/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_13/testtext.txt'
    words, distinctWordCount = processFile(bookFile, processLine)
    print words
    print (distinctWordCount)
