for n in range(2, 10):
    for x in range(2, n):
        #print(n,':', x, list(range(2,n)))
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        #else:
            #print(n, 'else', x)
            #break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')

