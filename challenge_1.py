with open("tables.txt", 'a') as jabber:
    for i in range(2, 13):
        for j in range(1, 13):
            print("{0:2} times {1} is {2}".format(j, i, i*j), file=jabber)


