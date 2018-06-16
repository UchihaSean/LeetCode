def findIDOfWinningGuest(guests, sec):
    # WRITE YOUR CODE HERE
    link = range(guests)
    ind = 0

    for i in range(guests - 1):
        ind = (ind + sec) % len(link)

        del link[ind]
        if ind == -1: ind = 0

    print link[0]


findIDOfWinningGuest(5555,12)